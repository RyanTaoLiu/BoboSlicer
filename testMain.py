import PIL.Image
import tqdm
import shutil

from functions_np import *
from printer import *
from utils import *
from perfab import *
from postprocess import *

from multiprocessing import Pool, cpu_count, Manager
from settings import *


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