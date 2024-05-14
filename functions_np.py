from abc import ABC, abstractmethod
import numpy as np
import math




## ABC
class ImplicitFunction(ABC):
    def __init__(self, **kwargs):
        pass

    def __call__(self, **kwargs):
        pass

    def bitmapPadding(self, img, x_padding=4, y_padding=0):
        if y_padding > 0:
            img[:y_padding, :] = 255
            img[-y_padding:, :] = 255
        if x_padding > 0:
            img[:, :x_padding] = 255
            img[:, -x_padding:] = 255
        return img

    def padding(self, x, y, value, x_padding, y_padding):
        xmin, xmax = x.min(), x.max()
        ymin, ymax = y.min(), y.max()

        if x_padding > 0:
            value[x-xmin <= x_padding or xmax-x <= x_padding] = 255
        if y_padding > 0:
            value[y-ymin <= y_padding or ymax-y <= y_padding] = 255
        return value

class Gyroid(ImplicitFunction):
    def __init__(self, cycleLayerNumber=25, **kwargs):
        super().__init__(**kwargs)
        self.savedSlicer = dict()
        self.cycleLayerNumber = cycleLayerNumber

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x, _y, _z = x * np.pi * 2/2, y* np.pi * 2/2, z * np.pi * 2/2
            value = np.sin(_x) * np.cos(_y) + \
                np.sin(_y) * np.cos(_z) + \
                np.sin(_z) * np.cos(_x)
            bitmap = (value > 0).astype(int) * 255
            self.savedSlicer[zi] = bitmap.copy()
            return bitmap
        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]


class Gyroid1(ImplicitFunction):
    def __init__(self, cycleLayerNumber=1e9, isovalue=0, **kwargs):
        super().__init__(**kwargs)
        self.savedSlicer = dict()
        self.cycleLayerNumber = cycleLayerNumber
        self.isovalue = isovalue

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x, _y, _z = x * np.pi * 2/10, y* np.pi * 2/10, z * np.pi * 2/10
            value = np.sin(_x) * np.cos(_y) + \
                np.sin(_y) * np.cos(_z) + \
                np.sin(_z) * np.cos(_x)
            bitmap = (value > self.isovalue).astype(int) * 255
            if self.cycleLayerNumber < 3000:
                self.savedSlicer[zi] = bitmap.copy()
            return bitmap
        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]

## ABC
class TPMS(ImplicitFunction):
    def __init__(self, k, isovalue=0, cycleLayerNumber=1e9, **kwargs):
        super().__init__(**kwargs)
        self.savedSlicer = dict()
        self.cycleLayerNumber = cycleLayerNumber
        self.k = k
        self.isovalue = isovalue

        self.x_padding_px = 0 if 'x_padding_px' not in kwargs else kwargs['x_padding_px']
        self.y_padding_px = 0 if 'y_padding_px' not in kwargs else kwargs['y_padding_px']

        self.x_padding_mm = 0 if 'x_padding_mm' not in kwargs else kwargs['x_padding_mm']
        self.y_padding_mm = 0 if 'y_padding_mm' not in kwargs else kwargs['y_padding_mm']

    def __call__(self, x, y, z, zi):
        pass

    def postprocess4bitmap(self, bitmap):
        return self.bitmapPadding(bitmap, self.x_padding_px, self.y_padding_px)

    def postprocess(self, x, y, value):
        return self.padding(x, y, value, self.x_padding_mm, self.y_padding_mm)

class GyroidSolid(TPMS):
    def __init__(self, k, isovalue=0, cycleLayerNumber=1e9, **kwargs):
        super().__init__(k, isovalue, cycleLayerNumber, **kwargs)

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x = x * np.pi * 2 /self.k
            _y = y * np.pi * 2 /self.k
            _z = z * np.pi * 2 /self.k

            value = np.sin(_x) * np.cos(_y) + \
                    np.sin(_y) * np.cos(_z) + \
                    np.sin(_z) * np.cos(_x)
            bitmap = (value > self.isovalue).astype(int) * 255

            if self.cycleLayerNumber < 3000:
                self.savedSlicer[zi] = bitmap.copy()
            return bitmap

        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]


class GyroidSheet(TPMS):
    def __init__(self, k, isovalue=0, cycleLayerNumber=1e9, **kwargs):
        super().__init__(k, isovalue, cycleLayerNumber, **kwargs)

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x = x * np.pi * 2 /self.k
            _y = y * np.pi * 2 /self.k
            _z = z * np.pi * 2 /self.k

            value = np.sin(_x) * np.cos(_y) + \
                    np.sin(_y) * np.cos(_z) + \
                    np.sin(_z) * np.cos(_x)

            value = np.abs(value)
            bitmap = (value < self.isovalue).astype(int) * 255

            if self.cycleLayerNumber < 3000:
                self.savedSlicer[zi] = bitmap.copy()
            return bitmap

        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]

class FKSSolid(TPMS):
    def __init__(self, k, isovalue=0, cycleLayerNumber=1e9, **kwargs):
        super().__init__(k, isovalue, cycleLayerNumber, **kwargs)

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x = x * np.pi * 2 / self.k
            _y = y * np.pi * 2 / self.k
            _z = z * np.pi * 2 / self.k

            value = np.cos(2 * _x) *    np.sin(_y) *        np.cos(_z) + \
                    np.cos(_x) *        np.cos(2 * _y) *    np.sin(_z) +\
                    np.sin(_x) *        np.cos(_y) *        np.cos(2 * _z)
            bitmap = (value > self.isovalue).astype(int) * 255

            if self.cycleLayerNumber < 3000:
                self.savedSlicer[zi] = bitmap.copy()
            return bitmap

        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]

class FKSSheet(TPMS):
    def __init__(self, k, isovalue=0, cycleLayerNumber=1e9, **kwargs):
        super().__init__(k, isovalue, cycleLayerNumber, **kwargs)

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x = x * np.pi * 2 / self.k
            _y = y * np.pi * 2 / self.k
            _z = z * np.pi * 2 / self.k

            value = np.cos(2 * _x) *    np.sin(_y) *        np.cos(_z) + \
                    np.cos(_x) *        np.cos(2 * _y) *    np.sin(_z) +\
                    np.sin(_x) *        np.cos(_y) *        np.cos(2 * _z)

            value = np.abs(value)
            bitmap = (value < self.isovalue).astype(int) * 255

            if self.cycleLayerNumber < 3000:
                self.savedSlicer[zi] = bitmap.copy()
            return bitmap

        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]