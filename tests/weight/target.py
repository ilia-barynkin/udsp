import os
import numpy as np
import pandas as pd
from scipy import signal
import matplotlib.pyplot as plt
import udsp

# Set the current directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Read and preprocess the data
df = pd.read_csv("weight.csv", header=None)
df.dropna(inplace=True)
df.columns = ["Q"]
df["Q"] = df["Q"].astype(int)
df["Index"] = range(len(df))
sampled_data_raw = np.array(df["Q"])

# Perform FFT
fft = np.fft.fft(sampled_data_raw)
freq = np.fft.fftfreq(len(sampled_data_raw))

# Set plot parameters
width_px = 600
height_px = 400
dpi = plt.rcParams['figure.dpi']

# Cut the FFT around the middle frequency
mid_freq = np.quantile(freq, 0.5)
bandwidth = 0.000001
cutoff_frequency = mid_freq + bandwidth

# Construct Butterworth filter
nyquist_frequency = 0.5 * 1
normalized_cutoff = cutoff_frequency / nyquist_frequency
b, a = signal.butter(2, normalized_cutoff, 'low', analog=False)
b1, a1 = signal.butter(2, normalized_cutoff, 'low', analog=False)
kernel_iir = signal.convolve(b, b1)
filtered_iir = signal.filtfilt(b, a, sampled_data_raw)

# fir
fir_order = 40
kernel_fir = signal.firwin(fir_order, cutoff_frequency, window='hann')
filtered_fir = signal.lfilter(kernel_fir, [1.0], sampled_data_raw)

# Convert IIR kernel to FIR kernel
kernel = kernel_fir

stat = udsp.udsp_stat(script_dir + "/libudsp.so")
convolved = stat.convolve(sampled_data_raw, kernel)

# Convolve the sampled data with the impulse response using scipy

convolved_scipy = signal.convolve(sampled_data_raw, kernel, mode='same')

# Print the resampled impulse response
print(','.join(map(str, kernel)))

# Plot the resampled impulse response
plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi)
plt.plot(kernel)
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Impulse Response')
plt.grid(True)

x_gap_start = 1000
x_gap_finish = 20000

# Plot the filtered signal IIR
plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi)
plt.plot(np.linspace(0, len(sampled_data_raw) - 1, len(sampled_data_raw)), sampled_data_raw, label="Raw", color='blue', linewidth=0.6)
plt.plot(np.linspace(0, len(filtered_iir) - 1, len(filtered_iir)), filtered_iir, label="Filtered Signal", color='red', linewidth=0.8)
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Filtered Signal (IIR)')
plt.xlim(x_gap_start, x_gap_finish)
plt.legend()

# Plot the filtered signal FIR
plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi)
plt.plot(np.linspace(0, len(sampled_data_raw) - 1, len(sampled_data_raw)), sampled_data_raw, label="Raw", color='blue', linewidth=0.6)
plt.plot(np.linspace(0, len(filtered_fir) - 1, len(filtered_fir)), filtered_fir, label="Filtered Signal", color='red', linewidth=0.8)
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Filtered Signal (FIR)')
plt.xlim(x_gap_start, x_gap_finish)
plt.legend()

plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi)
plt.plot(np.linspace(0, len(sampled_data_raw) - 1, len(sampled_data_raw)), sampled_data_raw, label="Raw", color='blue', linewidth=0.6)
plt.plot(np.linspace(0, len(convolved) - 1, len(convolved)), convolved, label="Convolved", linewidth=0.8, color='orange')
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Filtered Signal (UDSP)')
plt.xlim(x_gap_start, x_gap_finish)
plt.legend()

plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi)
plt.plot(np.linspace(0, len(sampled_data_raw) - 1, len(sampled_data_raw)), sampled_data_raw, label="Raw", color='blue', linewidth=0.6)
plt.plot(np.linspace(0, len(convolved_scipy) - 1, len(convolved_scipy)), convolved_scipy, label="Convolved by scipy", linewidth=0.8, color='green')
plt.xlabel('Index')
plt.ylabel('Magnitude')
plt.title('Filtered Signal (scipy)')
plt.xlim(x_gap_start, x_gap_finish)
plt.legend()

plt.grid(True)

plt.show()

# Print the coefficients of the Butterworth filter
print(b)
print(a)