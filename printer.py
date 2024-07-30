from abc import ABC, abstractmethod
import math


class printerInfo(ABC):
    @abstractmethod
    def __init__(self, **kwargs):
        self.delta = None
        self.maxPrintingSize = None

    @abstractmethod
    def serialize(self, outpath):
        pass

    @abstractmethod
    def unserialize(self, inputpath):
        pass


class mega8ks(printerInfo):
    def __init__(self):
        super().__init__()
        # voxel size 43um, 43um, 0.05mm
        self.delta = [0.043, 0.043, 0.05]

        # printer printing size mm
        self.maxPrintingSize = [330.24, 185.76, 300]

        self.voxelSize = [math.floor(self.maxPrintingSize[i]/self.delta[i]) for i in range(3)]
        # 7680*4320 6976

    def serialize(self, outpath):
        pass

    def unserialize(self, inputpath):
        pass
