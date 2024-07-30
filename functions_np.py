from abc import ABC, abstractmethod
import numpy as np
import math


## ABC
class ImplicitFunction(ABC):
    def __init__(self, **kwargs):
        pass

    def __call__(self, **kwargs):
        pass

    def postprocess4bitmap(self, bitmap, **kwargs):
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
            value[x - xmin <= x_padding or xmax - x <= x_padding] = 255
        if y_padding > 0:
            value[y - ymin <= y_padding or ymax - y <= y_padding] = 255
        return value


class ImplicitFunctionFactory():
    pass


class Gyroid(ImplicitFunction):
    def __init__(self, cycleLayerNumber=25, **kwargs):
        super().__init__(**kwargs)
        self.savedSlicer = dict()
        self.cycleLayerNumber = cycleLayerNumber

    def __call__(self, x, y, z, zi):
        if zi < self.cycleLayerNumber:
            _x, _y, _z = x * np.pi * 2 / 2, y * np.pi * 2 / 2, z * np.pi * 2 / 2
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
            _x, _y, _z = x * np.pi * 2 / 10, y * np.pi * 2 / 10, z * np.pi * 2 / 10
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
            _x = x * np.pi * 2 / self.k
            _y = y * np.pi * 2 / self.k
            _z = z * np.pi * 2 / self.k

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
            _x = x * np.pi * 2 / self.k
            _y = y * np.pi * 2 / self.k
            _z = z * np.pi * 2 / self.k

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

            value = np.cos(2 * _x) * np.sin(_y) * np.cos(_z) + \
                    np.cos(_x) * np.cos(2 * _y) * np.sin(_z) + \
                    np.sin(_x) * np.cos(_y) * np.cos(2 * _z)
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

            value = np.cos(2 * _x) * np.sin(_y) * np.cos(_z) + \
                    np.cos(_x) * np.cos(2 * _y) * np.sin(_z) + \
                    np.sin(_x) * np.cos(_y) * np.cos(2 * _z)

            value = np.abs(value)
            bitmap = (value < self.isovalue).astype(int) * 255

            if self.cycleLayerNumber < 3000:
                self.savedSlicer[zi] = bitmap.copy()
            return bitmap

        else:
            oldz = zi % self.cycleLayerNumber
            return self.savedSlicer[oldz]


class GyroidSolidOBBRotation(TPMS):
    def __init__(self, k, isovalue, OBBSize=None, theta=math.pi / 6):
        super().__init__(k, isovalue)
        if OBBSize is None:
            self.OBBSize = np.asarray([300, 25, 300])

        self.theta = theta  # 30 degrees in radians
        sinTheta = math.sin(theta)
        cosTheta = math.cos(theta)

        # [300., 171.65063509, 272.30762114]
        self.AABBSize = np.asarray([self.OBBSize[0],
                                    self.OBBSize[2] * sinTheta + self.OBBSize[1] * cosTheta,
                                    self.OBBSize[2] * cosTheta + self.OBBSize[1] * sinTheta])

        self.R = np.array([
            [1, 0, 0],
            [0, np.cos(self.theta), np.sin(self.theta)],
            [0, -np.sin(self.theta), np.cos(self.theta)]
        ])
        self.O = np.array([0, self.OBBSize[1] * cosTheta, self.OBBSize[1] * sinTheta])

        self.k = k
        self.isovalue = isovalue

        self.OBBCenter = self.AABBSize / 2
        self.OBBLength = self.OBBSize / 2
        self.OBBAxis = self.R @ np.eye(3)

        self.Tz = k * self.OBBSize[1] / 2

    def gyroid(self, xyz):
        x, y, z = xyz[:, 0], xyz[:, 1], xyz[:, 2]
        return np.sin(x) * np.cos(y) + np.sin(y) * np.cos(z) + np.sin(z) * np.cos(x)

    def __call__(self, xx, yy, zz, zi):
        xyz = np.vstack((xx, yy, zz + np.zeros_like(xx)))  # position
        xyzNew = xyz * np.pi * 2 / self.k  # used to calculate the TPMS
        Tz = np.zeros_like(xyzNew)
        Tz[:, 1] = self.Tz
        new_xyz = self.R @ xyzNew + Tz

        xyzinObbMasked = self.are_points_in_obb(xyz.T, self.OBBCenter, self.OBBAxis, self.OBBLength)
        valueMasked = (self.gyroid(new_xyz.T[xyzinObbMasked]) > self.isovalue).astype(int) * 255

        value = np.zeros_like(xx).astype(int)  # debug for obb
        value[xyzinObbMasked] = valueMasked

        return value

    @staticmethod
    def are_points_in_axis_aligned_cuboid(points, center, lengths):
        half_lengths = lengths / 2
        # Translate points to the cuboid center
        translated_points = points - center
        # Check if points are within the half-lengths
        within_half_lengths = np.all(np.abs(translated_points) <= half_lengths, axis=1)
        return within_half_lengths

    @staticmethod
    def are_points_in_obb(points, center, axes, half_lengths):
        # Translate points to the OBB center
        translated_points = points - center

        # Initialize a boolean array to track if each point is inside the OBB
        inside = np.ones(points.shape[0], dtype=bool)

        # Check each axis
        for axis, half_length in zip(axes, half_lengths):
            # Project the local points onto the OBB's axis
            projection_lengths = np.dot(translated_points, axis)
            # Check if the projection lengths are within the half-lengths
            inside = np.logical_and(inside, np.abs(projection_lengths) <= half_length)

        return inside

    @staticmethod
    def bin_search(f, a, b, tol):
        while (b - a) / 2 > tol:
            c = (a + b) / 2
            if abs(f(c)) < tol:
                return c
            elif f(a) * f(c) < 0:
                b = c
            else:
                a = c

        return (a + b) / 2
