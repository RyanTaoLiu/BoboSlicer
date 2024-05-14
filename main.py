import numpy as np
from PIL import Image
import os
import math
import tqdm

from multiprocessing import Pool, cpu_count
from functions import *
from printer import *
from utils import *


## main class
class LCDSlicer:
    def __init__(self, printerInfo, settings=None):
        self.printerInfo = printerInfo
        self.objects = {}
        self.updateAABB()

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

        return uuid

    def init_slice(self, outFolder='out'):
        zmin, zmax = self.AABB[2][0], self.AABB[2][1]
        self.zlayers = np.arange(zmin, zmax)

    def slice_z(self, outFolder, ziidx):
        printer = self.printerInfo
        zi = self.zlayers[ziidx]
        img = np.zeros((printer.voxelSize[0], printer.voxelSize[1]))
        for obj in self.objects.values():
            obj_img = obj.slice(zi)
            img[obj.posX:obj.posX + obj.width, obj.posY:obj.posY + obj.height] = obj_img
        im = Image.fromarray(img.T).convert("L")
        im.save(os.path.join(outFolder, '{}.png'.format(ziidx)))

    def slice_multithread(self, threeadNum, threadPoolSize, outFolder='out'):
        self.init_slice(outFolder)

        for ziidx in tqdm.tqdm(range(len(self.zlayers))):
            if ziidx % threadPoolSize != threeadNum:
                continue
            self.slice_z(outFolder, ziidx)

    def slice(self, outFolder='out'):
        self.init_slice(outFolder)

        for ziidx in tqdm.tqdm(range(len(self.zlayers))):
            self.slice_z(outFolder, ziidx)


# use mm
class printObject:
    def __init__(self, func, **kwargs):
        self.unit = 'mm'
        # object width, height
        self.width = 120 if 'x' not in kwargs else kwargs['x']
        self.height = 25 if 'y' not in kwargs else kwargs['y']
        self.depth = 120 if 'z' not in kwargs else kwargs['z']

        # object position X, Y
        self.posX = 0 if 'posX' not in kwargs else kwargs['posX']
        self.posY = 0 if 'posY' not in kwargs else kwargs['posY']

        self.func = func
        self.delta = []

        self.device = 'cpu'

    def preprocess(self):
        assert self.unit == 'pixel', 'cannot call this in mm based unit'
        x = torch.arange(self.width).to(self.device) + 0.5
        y = torch.arange(self.height).to(self.device) + 0.5
        xx, yy = torch.meshgrid((x, y), indexing="ij")
        self.xx, self.yy = xx.flatten(), yy.flatten()
        self.emptyImage = torch.zeros(self.width * self.height).to(self.device)

    def slice(self, z):
        assert self.unit == 'pixel', 'cannot call this in mm based unit'
        zz = torch.tensor([z]) * self.delta[2]
        value = self.func(self.xx * self.delta[0], self.yy * self.delta[1], zz)
        img = value.reshape((self.width, self.height))
        img_np = img.detach().cpu().numpy()
        return img_np

    def toPixelObject(self, res):
        dx, dy, dz = res
        PixelObject = printObject(self.func,
                                  width=round(self.width / dx), height=round(self.height / dy),
                                  depth=round(self.depth / dz),
                                  posX=round(self.posX / dx), posY=round(self.posY / dy))
        PixelObject.delta = res
        PixelObject.unit = 'pixel'
        PixelObject.preprocess()
        return PixelObject


@torch.no_grad()
def main_multithread(threadNum_and_poolSize):
    threadNum = threadNum_and_poolSize[0]
    poolSize = threadNum_and_poolSize[1]
    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)

    obj1 = printObject(Gyroid(), posX=5, posY=5)
    obj1Id = lcdslicer.addObject(obj1)
    lcdslicer.slice_multithread(threadNum, poolSize)

@torch.no_grad()
def main():
    printer = mega8ks()
    lcdslicer = LCDSlicer(printer)

    obj1 = printObject(Gyroid(), posX=5, posY=5)
    obj1Id = lcdslicer.addObject(obj1)
    lcdslicer.slice()

if __name__ == '__main__':
    cpu_num = cpu_count()//2
    with Pool(cpu_num) as p:
        p.map(main_multithread, [[i, cpu_num] for i in range(cpu_num)])
