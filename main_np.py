import PIL.Image
import tqdm
import shutil

from functions_np import *
from printer import *
from utils import *
from perfab import *
from postprocess import *

from multiprocessing import Pool, cpu_count, Manager

from testMain import *
from settings import *



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

def main_test_rot(outpath):
    # do not change below
    remove_all_temp_files()

    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)

    # set implicit function
    func = GyroidSolidOBBRotation(k=10, isovalue=0.6163)

    AABB = [300., 171.65063509, 272.30762114]
    obj1 = printObject(func, width=AABB[0], height=AABB[1], depth=AABB[2],
                       posX=15, posY=8, supprotExtend='None')
    obj1Id = lcdslicer.addObject(obj1)
    obj1.uuid = obj1Id

    lcdslicer.slice()

def main_test_300x25x300(outpath):
    # do not change below
    remove_all_temp_files()

    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)

    k = 4
    gyroidCycleLayerThickness = k
    cycleLayerNumber = int(math.floor(gyroidCycleLayerThickness / printer.delta[2]))
    # set implicit function
    func = FKSSheet(k=k, isovalue=0.3046, x_padding_px=4)

    obj1 = printObject(func, width=300, height=25, depth=300,
                       posX=15, posY=77.5, supprotExtend='X')
    obj1Id = lcdslicer.addObject(obj1)
    obj1.uuid = obj1Id

    lcdslicer.cycleNumber = cycleLayerNumber
    lcdslicer.slice()


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

    # mainIOExcel('TPMS-param.xlsx')
    # main_test_rot('results/AN_test_rot30.prz')
    main_test_300x25x300('results/AN_test_rot30.prz')


