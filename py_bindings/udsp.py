# udsp module
import ctypes

class udsp_stat:
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

        self.lib_convolve = self.lib.convolve
        self.lib_convolve.restype = ctypes.POINTER(ctypes.c_float)
        self.lib_convolve.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.POINTER(ctypes.c_float), ctypes.c_int]

    def destroy(self):
        self.lib.destroy()

    def mean(self, arr):
        return self.lib_mean((ctypes.c_float * len(arr))(*arr), len(arr))

    def variance(self, arr):
        return self.lib_variance((ctypes.c_float * len(arr))(*arr), len(arr))

    def stddev(self, arr):
        return self.lib_stddev((ctypes.c_float * len(arr))(*arr), len(arr))

    def convolve(self, arr1, arr2):
        return self.lib_convolve((ctypes.c_float * len(arr1))(*arr1), len(arr1), (ctypes.c_float * len(arr2))(*arr2), len(arr2))