import PIL.Image
import tqdm
import shutil

from functions_np import *
from printer import *
from utils import *
from perfab import *
from postprocess import *

from multiprocessing import Pool, cpu_count, Manager


## main class
class LCDSlicer:
    def __init__(self, printerInfo, settings=None):
        self.printerInfo = printerInfo
        self.objects = {}
        self.updateAABB()
        self.supportImg = perfab(printerInfo.delta[0], printerInfo.delta[1])

        self.raft = 'normal'
        self.raftNumber = 0
        self.cycleNumber = 0

    def updateAABB(self):
        self.AABB = [[inf, -inf], [inf, -inf], [0, 0]]
        for obj in self.objects.values():
            self.updateAABBbyObj(obj)

    def updateAABBbyObj(self, obj):
        self.AABB[0][0] = obj.posX
        if obj.posX + obj.width > self.AABB[0][1]:
            self.AABB[0][1] = obj.posX + obj.width

        if obj.posY < self.AABB[1][0]:
            self.AABB[1][0] = obj.posY
        if obj.posY + obj.height > self.AABB[1][1]:
            self.AABB[1][1] = obj.posY + obj.height

        if obj.depth > self.AABB[2][1]:
            self.AABB[2][1] = obj.depth
        # need assert after checking boundary

    def addObject(self, obj):
        uuid = get_uuid()
        pixelBasedObj = obj.toPixelObject(self.printerInfo.delta)
        self.objects[uuid] = pixelBasedObj

        try:
            self.updateAABB()
        except Exception as e:
            print(e)
            self.objects.pop(uuid)
            self.updateAABB()
            return None

        pixelBasedObj.uuid = uuid
        obj.uuid = uuid
        return uuid

    def init_slice(self, outFolder='out'):
        zmin, zmax = self.AABB[2][0], self.AABB[2][1]
        self.zlayers = np.arange(zmin, zmax)

    def slice_z(self, outFolder, ziidx):
        printer = self.printerInfo
        zi = self.zlayers[ziidx]

        size = (printer.voxelSize[0], printer.voxelSize[1])
        # img = Image.new("L", size, 0)
        img = np.zeros(size, dtype=np.uint8)
        for obj in self.objects.values():
            obj_img = obj.slice(zi)
            img[obj.posX:obj.posX + obj.width, obj.posY:obj.posY + obj.height] = obj_img

            if obj.supprotExtend.lower() == 'y':
                supportImg = self.supportImg.support(obj.width).T
                img[obj.posX:obj.posX + supportImg.shape[0],
                obj.posY - supportImg.height:obj.posY] = supportImg
                img[obj.posX:obj.posX + supportImg.shape[0],
                obj.posY + obj.height:obj.posY + obj.height + supportImg.shape[1]] = np.fliplr(supportImg)

            elif obj.supprotExtend.lower() == 'x':
                supportImg = np.rot90(self.supportImg.support(obj.height).T)
                img[obj.posX - supportImg.shape[0]:obj.posX,
                obj.posY:obj.posY + supportImg.shape[1]] = supportImg
                img[obj.posX + obj.width:obj.posX + obj.width + supportImg.shape[0],
                obj.posY:obj.posY + supportImg.shape[1]] = np.flipud(supportImg)

        _img = PIL.Image.fromarray(np.uint8(img.T), 'L')
        _img.save(os.path.join(outFolder, '{}.png'.format(ziidx + self.raftNumber + 1)))

    def slice_raft(self, outFolder, offset=10):
        raftDir = os.path.join('template', 'raft', self.raft)
        allRaftsPng = os.listdir(raftDir)
        allRaftsPng = [it.endswith('png') for it in allRaftsPng]
        self.raftNumber = len(allRaftsPng)
        printer = self.printerInfo

        for i in tqdm.tqdm(range(self.raftNumber), desc='raft slicer'):
            size = (printer.voxelSize[0], printer.voxelSize[1])
            img = np.zeros(size, dtype=np.uint8)

            raftTemplate = PIL.Image.open(os.path.join(raftDir, '{}.png'.format(i + 1)))
            npTemplate = np.asarray(raftTemplate).T

            for obj in self.objects.values():
                if obj.supprotExtend.lower() == 'y':
                    supportImg = self.supportImg.support(obj.width).T
                    img[obj.posX - offset:
                        obj.posX + obj.width + offset,
                        obj.posY - offset - supportImg.shape[1]:
                        obj.posY + obj.height + offset + supportImg.shape[1]] = \
                        npTemplate[obj.posX - offset:
                                   obj.posX + obj.width + offset,
                        obj.posY - offset - supportImg.shape[1]:
                        obj.posY + obj.height + offset + supportImg.shape[1]]

                    img[obj.posX:obj.posX + supportImg.shape[0],
                    obj.posY - supportImg.height:obj.posY] = \
                        np.maximum(supportImg,img[obj.posX:obj.posX + supportImg.shape[0], obj.posY - supportImg.height:obj.posY])
                    img[obj.posX:obj.posX + supportImg.shape[0],
                    obj.posY + obj.height:obj.posY + obj.height + supportImg.shape[1]] = \
                        np.maximum(np.fliplr(supportImg),img[obj.posX:obj.posX + supportImg.shape[0],
                    obj.posY + obj.height:obj.posY + obj.height + supportImg.shape[1]])

                elif obj.supprotExtend.lower() == 'x':
                    supportImg = np.rot90(self.supportImg.support(obj.height).T)
                    img[obj.posX - offset - supportImg.shape[0]:
                        obj.posX + obj.width + offset + supportImg.shape[0],
                    obj.posY - offset:
                    obj.posY + obj.height + offset] = \
                        npTemplate[obj.posX - offset - supportImg.shape[0]:
                                   obj.posX + obj.width + offset + supportImg.shape[0],
                        obj.posY - offset:
                        obj.posY + obj.height + offset]

                    img[obj.posX - supportImg.shape[0]:obj.posX,
                    obj.posY:obj.posY + supportImg.shape[1]] = np.maximum(supportImg,
                                                                      img[obj.posX - supportImg.shape[0]:obj.posX,
                                                                     obj.posY:obj.posY + supportImg.shape[1]])
                    img[obj.posX + obj.width:obj.posX + obj.width + supportImg.shape[0],
                    obj.posY:obj.posY + supportImg.shape[1]] = np.maximum(np.flipud(supportImg),
                                                                      img[obj.posX + obj.width:obj.posX + obj.width + supportImg.shape[0],
                                                                      obj.posY:obj.posY + supportImg.shape[1]])

                else:
                    img[obj.posX - offset: obj.posX + obj.width + offset,
                    obj.posY - offset: obj.posY + obj.height + offset] = \
                        npTemplate[obj.posX - offset:obj.posX + obj.width + offset,
                        obj.posY - offset:obj.posY + obj.height + offset]

            _img = PIL.Image.fromarray(np.uint8(img.T), 'L')
            _img.save(os.path.join(outFolder, '{}.png'.format(i + 1)))

    def slice_multithread(self, threeadNum, threadPoolSize, outFolder='out'):
        self.init_slice(outFolder)

        for ziidx in tqdm.tqdm(range(len(self.zlayers)), desc='layer slicer'):
            if ziidx % threadPoolSize != threeadNum:
                continue
            self.slice_z(outFolder, ziidx)

    def slice(self, outFolder='out'):
        self.init_slice(outFolder)
        if self.raft is not None:
            self.slice_raft(outFolder)

        if self.cycleNumber == 0:
            layerNumbers = len(self.zlayers)
            for ziidx in tqdm.tqdm(range(layerNumbers), desc='layer slicer'):
                self.slice_z(outFolder, ziidx)
        else:
            layerNumbers = self.cycleNumber
            for ziidx in tqdm.tqdm(range(layerNumbers), desc='layer slicer'):
                self.slice_z(outFolder, ziidx)

            for ziidx in tqdm.tqdm(range(layerNumbers, len(self.zlayers)), desc='layer copy'):
                realLayerIdx = ziidx
                realLayerIdx %= self.cycleNumber
                # print('{} => {}'.format(realLayerIdx + self.raftNumber+1, ziidx + self.raftNumber+1))
                shutil.copy('{}/{}.png'.format(outFolder, realLayerIdx + self.raftNumber + 1),
                            '{}/{}.png'.format(outFolder, ziidx + self.raftNumber + 1))

    def posprocess(self, outfile: str, target_type=''):
        gcode_settings = {
            'totalLayer': self.raftNumber + len(self.zlayers),
            'layerThickness': self.printerInfo.delta[2],
            'raftLayer': self.raftNumber,
            'cycleNumber': self.cycleNumber,
        }
        postprocess(outfile, gcode_settings)


# use mm
class printObject:
    def __init__(self, func, **kwargs):
        self.unit = 'mm'
        # object width, height
        self.width = 120 if 'width' not in kwargs else kwargs['width']
        self.height = 25 if 'height' not in kwargs else kwargs['height']
        self.depth = 120 if 'depth' not in kwargs else kwargs['depth']

        # object position X, Y
        self.posX = 0 if 'posX' not in kwargs else kwargs['posX']
        self.posY = 0 if 'posY' not in kwargs else kwargs['posY']

        self.func = func
        self.delta = []

        self.device = 'cpu'

        # only (x, y) is valid choose
        self.supprotExtend = 'None' if 'supprotExtend' not in kwargs else kwargs['supprotExtend']
        self.uuid = ''

    def preprocess(self):
        assert self.unit == 'pixel', 'cannot call this in mm based unit'
        x = np.arange(self.width) + 0.5
        y = np.arange(self.height) + 0.5
        xx, yy = np.meshgrid(x, y, indexing="ij")
        self.xx, self.yy = xx.flatten(), yy.flatten()
        self.emptyImage = np.zeros(self.width * self.height)

    def slice(self, zi):
        assert self.unit == 'pixel', 'cannot call this in mm based unit'
        zz = np.array([zi]).copy() * self.delta[2]
        value = self.func(self.xx * self.delta[0], self.yy * self.delta[1], zz, zi)
        img = value.reshape((self.width, self.height))

        img = self.func.postprocess4bitmap(img)
        return img

    def toPixelObject(self, res):
        dx, dy, dz = res
        PixelObject = printObject(self.func,
                                  width=round(self.width / dx), height=round(self.height / dy),
                                  depth=round(self.depth / dz),
                                  posX=round(self.posX / dx), posY=round(self.posY / dy))
        PixelObject.delta = res
        PixelObject.unit = 'pixel'
        PixelObject.supprotExtend = self.supprotExtend
        PixelObject.preprocess()
        return PixelObject


def main_multithread(threadNum_and_poolSize):
    threadNum = threadNum_and_poolSize[0]
    poolSize = threadNum_and_poolSize[1]
    obj_zi = threadNum_and_poolSize[2]
    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)

    cycleLayerThinckness = 1

    cycleLayerNumber = int(math.floor(cycleLayerThinckness / printer.delta[2]))
    obj1 = printObject(Gyroid(cycleLayerNumber=25), posX=5, posY=5)
    obj1Id = lcdslicer.addObject(obj1)
    obj1.uuid = obj1Id
    lcdslicer.slice_multithread(threadNum, poolSize)


def main(outfile):
    remove_all_temp_files()

    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)

    cycleLayerThinckness1 = 2
    cycleLayerNumber1 = int(math.floor(cycleLayerThinckness1 / printer.delta[2]))
    obj1 = printObject(Gyroid(cycleLayerNumber=cycleLayerNumber1), posX=135, posY=5, supprotExtend='X')
    obj1Id = lcdslicer.addObject(obj1)
    obj1.uuid = obj1Id

    cycleLayerThinckness2 = 10
    cycleLayerNumber2 = int(math.floor(cycleLayerThinckness2 / printer.delta[2]))
    obj2 = printObject(Gyroid1(cycleLayerNumber=cycleLayerNumber2), posX=135, posY=55, supprotExtend='X')
    obj2Id = lcdslicer.addObject(obj2)
    obj2.uuid = obj2Id

    ## the largest common number of all images
    allcycleLayerNumber = np.lcm.reduce([cycleLayerNumber1, cycleLayerNumber2])
    lcdslicer.cycleNumber = allcycleLayerNumber
    lcdslicer.slice()
    lcdslicer.posprocess(outfile)


def main_test_all(outfile):
    # input all need parameters
    k_list = [10,1,10,3,10,2,10,4]
    isovalue_list = [0.6163,0.6163,0.4038,0.4038,0.4641,0.4641,0.3046,0.3046]
    posx_list = [25,25,25,25,185,185,185,185]
    posy_list = [25,60,95,130,25,60,95,130]
    type_list = ['gyroidsolid','gyroidsolid','fkssolid','fkssolid','gyroidsheet','gyroidsheet','fkssheet','fkssheet']

    # do not change below
    remove_all_temp_files()

    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)
    cycleLayerNumberList = []

    for objid in range(len(k_list)):
        k, isovalue = k_list[objid], isovalue_list[objid]
        posx, posy = posx_list[objid], posy_list[objid]

        # calculate cycle layer number, fks and gyroid is equals k
        gyroidCycleLayerThickness = k
        cycleLayerNumber = int(math.floor(gyroidCycleLayerThickness / printer.delta[2]))
        cycleLayerNumberList.append(cycleLayerNumber)

        # set implicit function
        if type_list[objid].lower() == 'gyroidsolid':
            func = GyroidSolid(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber)
        elif type_list[objid].lower() == 'gyroidsheet':
            func = GyroidSheet(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber)
        elif type_list[objid].lower() == 'fkssolid':
            func = FKSSolid(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber)
        elif type_list[objid].lower() == 'fkssheet':
            func = FKSSheet(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber)
        else:
            assert 'No kinds of this implicit function'
            exit(-1)

        obj1 = printObject(func, posX=posx, posY=posy, supprotExtend='X')
        obj1Id = lcdslicer.addObject(obj1)
        obj1.uuid = obj1Id

    # get the largest common number(lcm) of all function cycle
    # for all z > lcm; we could copy the image directly
    allcycleLayerNumber = np.lcm.reduce(cycleLayerNumberList)
    lcdslicer.cycleNumber = allcycleLayerNumber
    lcdslicer.slice()
    lcdslicer.posprocess(outfile)

def main_test_all_withpadding(outfile):
    # input all need parameters
    k_list = [10,2,10,4,10,2,10,4]
    isovalue_list = [0.6163,0.6163,0.4038,0.4038,0.4641,0.4641,0.3046,0.3046]
    posx_list = [25,25,25,25,185,185,185,185]
    posy_list = [25,60,95,130,25,60,95,130]
    type_list = ['gyroidsolid','gyroidsolid','fkssolid','fkssolid','gyroidsheet','gyroidsheet','fkssheet','fkssheet']

    # do not change below
    remove_all_temp_files()

    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)
    cycleLayerNumberList = []

    for objid in range(len(k_list)):
        k, isovalue = k_list[objid], isovalue_list[objid]
        posx, posy = posx_list[objid], posy_list[objid]

        # calculate cycle layer number, fks and gyroid is equals k
        gyroidCycleLayerThickness = k
        cycleLayerNumber = int(math.floor(gyroidCycleLayerThickness / printer.delta[2]))
        cycleLayerNumberList.append(cycleLayerNumber)

        # set implicit function
        if type_list[objid].lower() == 'gyroidsolid':
            func = GyroidSolid(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber, x_padding_px=4)
        elif type_list[objid].lower() == 'gyroidsheet':
            func = GyroidSheet(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber, x_padding_px=4)
        elif type_list[objid].lower() == 'fkssolid':
            func = FKSSolid(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber, x_padding_px=4)
        elif type_list[objid].lower() == 'fkssheet':
            func = FKSSheet(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber, x_padding_px=4)
        else:
            assert 'No kinds of this implicit function'
            exit(-1)

        obj1 = printObject(func, posX=posx, posY=posy, supprotExtend='X')
        obj1Id = lcdslicer.addObject(obj1)
        obj1.uuid = obj1Id

    # get the largest common number(lcm) of all function cycle
    # for all z > lcm; we could copy the image directly
    allcycleLayerNumber = np.lcm.reduce(cycleLayerNumberList)
    lcdslicer.cycleNumber = allcycleLayerNumber
    lcdslicer.slice()
    lcdslicer.posprocess(outfile)


def mainIOExcel(excelPath):
    sheets_name, sheets_dict = excel2list(excelPath)

    for sheetidx, sheet_name in enumerate(sheets_name):
        print('*'*10+ 'task:{} - {}'.format(sheetidx, sheet_name)+'*'*10)

        remove_all_temp_files()
        printer = mega8ks()
        lcdslicer = LCDSlicer(printer)
        cycleLayerNumberList = []
        sheet_data = sheets_dict[sheetidx]['data']

        print(sheet_data)
        print('*'*30)

        for _obj in sheet_data:
            type, k, isovalue, posx, posy, xpadding, ypadding = _obj[1:]

            # calculate cycle layer number, fks and gyroid is equals k
            gyroidCycleLayerThickness = k
            cycleLayerNumber = int(math.floor(gyroidCycleLayerThickness / printer.delta[2]))
            cycleLayerNumberList.append(cycleLayerNumber)

            # set implicit function
            if type.lower() == 'gyroidsolid':
                func = GyroidSolid(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber,
                                   x_padding_px=xpadding, y_padding_px=ypadding)
            elif type.lower() == 'gyroidsheet':
                func = GyroidSheet(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber,
                                   x_padding_px=xpadding, y_padding_px=ypadding)
            elif type.lower() == 'fkssolid':
                func = FKSSolid(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber,
                                x_padding_px=xpadding, y_padding_px=ypadding)
            elif type.lower() == 'fkssheet':
                func = FKSSheet(k=k, isovalue=isovalue, cycleLayerNumber=cycleLayerNumber,
                                x_padding_px=xpadding, y_padding_px=ypadding)
            else:
                assert 'No kinds of this implicit function'

            obj = printObject(func, posX=posx, posY=posy, supprotExtend='X')
            objId = lcdslicer.addObject(obj)
            obj.uuid = objId

        allcycleLayerNumber = np.lcm.reduce(cycleLayerNumberList)
        lcdslicer.cycleNumber = allcycleLayerNumber
        lcdslicer.slice()
        lcdslicer.posprocess('results/{}.prz'.format(sheet_name))

        print('*'*10 + 'task - end: {}'.format('results/{}.prz'.format(sheet_name))+'*'*10)



if __name__ == '__main__':
    # with Manager() as manager:
    #    obj_zi = manager.dict()
    #    cpu_num = cpu_count()//2
    #    with Pool(cpu_num) as p:
    #        p.map(main_multithread, [(i, cpu_num, obj_zi) for i in range(cpu_num)])

    # main('results/out1.prz')

    # test for AN real result for printing
    # main_test_all('results/AN_test2.prz')
    # main_test_all_withpadding('results/AN_test_wi_padding.prz')
    mainIOExcel('TPMS-param.xlsx')

