## main class
import PIL.Image
import tqdm
import shutil

from functions_np import *
from printer import *
from utils import *
from perfab import *
from postprocess import *

from multiprocessing import Pool, cpu_count, Manager


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

        allVolume = []
        occupyVolume = []

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

            allVolume.append(obj.width * obj.height)
            occupyVolume.append(obj_img.sum()/255)

        _img = PIL.Image.fromarray(np.uint8(img.T), 'L')
        _img.save(os.path.join(outFolder, '{}.png'.format(ziidx + self.raftNumber + 1)))
        return np.array(allVolume), np.array(occupyVolume)

    def slice_raft(self, outFolder='out', offset=10):
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
        layerNumbers = len(self.zlayers)
        for ziidx in tqdm.tqdm(range(layerNumbers), desc='layer slicer'):
            if ziidx % threadPoolSize != threeadNum:
                continue
            self.slice_z(outFolder, ziidx)


    def slice(self, outFolder='out'):
        self.init_slice(outFolder)
        if self.raft is not None:
            self.slice_raft(outFolder)

        if self.cycleNumber == 0:
            layerNumbers = len(self.zlayers)

            # calculate volume
            all_volume = np.zeros((layerNumbers, len(self.objects)))
            occupy_volume = np.zeros((layerNumbers, len(self.objects)))

            for ziidx in tqdm.tqdm(range(layerNumbers), desc='layer slicer'):
                all_volume[ziidx], occupy_volume[ziidx] = self.slice_z(outFolder, ziidx)

        else:
            layerNumbers = self.cycleNumber

            # calculate volume
            all_volume = np.zeros((len(self.zlayers), len(self.objects)))
            occupy_volume = np.zeros((len(self.zlayers), len(self.objects)))

            for ziidx in tqdm.tqdm(range(layerNumbers), desc='layer slicer'):
                all_volume[ziidx], occupy_volume[ziidx] = self.slice_z(outFolder, ziidx)

            for ziidx in tqdm.tqdm(range(layerNumbers, len(self.zlayers)), desc='layer copy'):
                realLayerIdx = ziidx % self.cycleNumber
                all_volume[ziidx] = all_volume[realLayerIdx]
                occupy_volume[ziidx] = occupy_volume[realLayerIdx]
                # print('{} => {}'.format(realLayerIdx + self.raftNumber+1, ziidx + self.raftNumber+1))
                shutil.copy('{}/{}.png'.format(outFolder, realLayerIdx + self.raftNumber + 1),
                            '{}/{}.png'.format(outFolder, ziidx + self.raftNumber + 1))
        print('The volume fraction of each object is ', occupy_volume.sum(0) / all_volume.sum(0))

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

