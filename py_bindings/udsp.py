# udsp module
import ctypes

class stat:
    def __init__(self, lib_path):
        self.lib = ctypes.cdll.LoadLibrary(lib_path)
        
        self.lib_mean = self.lib.mean
        self.lib_mean.restype = ctypes.c_float
        self.lib_mean.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]

        self.lib_variance = self.lib.variance
        self.lib_variance.restype = ctypes.c_float
        self.lib_variance.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]

        self.lib_stddev = self.lib.stddev
        self.lib_stddev.restype = ctypes.c_float
        self.lib_stddev.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int]

    def mean(self, arr):
        return self.lib_mean((ctypes.c_float * len(arr))(*arr), len(arr))

    def variance(self, arr):
        return self.lib_variance((ctypes.c_float * len(arr))(*arr), len(arr))

    def stddev(self, arr):
        return self.lib_stddev((ctypes.c_float * len(arr))(*arr), len(arr))