# udsp module
import ctypes
import copy
import numpy as np

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
        self.lib_convolve.restype = None
        self.lib_convolve.argtypes = [ctypes.POINTER(ctypes.c_float), ctypes.POINTER(ctypes.c_float),
                     ctypes.POINTER(ctypes.c_float), ctypes.c_int, ctypes.c_int]

    def destroy(self):
        self.lib.destroy()

    def mean(self, arr):
        return self.lib_mean((ctypes.c_float * len(arr))(*arr), len(arr))

    def variance(self, arr):
        return self.lib_variance((ctypes.c_float * len(arr))(*arr), len(arr))

    def stddev(self, arr):
        return self.lib_stddev((ctypes.c_float * len(arr))(*arr), len(arr))

    def convolve(self, input_array, kernel_array):
        output_array = np.zeros(len(input_array) - len(kernel_array) + 1)
        input_ptr = (ctypes.c_float * len(input_array))(*input_array)
        kernel_ptr = (ctypes.c_float * len(kernel_array))(*kernel_array)
        output_ptr = (ctypes.c_float * len(output_array))(*output_array)

        # Call the convolve function
        self.lib_convolve(input_ptr, kernel_ptr, output_ptr, len(input_array), len(kernel_array))

        # Access the resulting output array
        output_result = [value for value in output_ptr]

        return output_result