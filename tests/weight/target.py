import os
import numpy as np
import pandas as pd
from scipy import signal
from datetime import datetime, timedelta
import argparse
import matplotlib.pyplot as plt

df = pd.read_csv("weight.csv", header=None)
df.dropna(inplace=True)
# Rename columns
df.columns = ["Q"]
df["Q"] = df["Q"].astype(int)
df["Index"] = range(len(df))

sampled_data_raw = df["Q"]

# Perform FFT
fft = np.fft.fft(sampled_data_raw, len(sampled_data_raw))
freq = np.fft.fftfreq(len(sampled_data_raw))

width_px = 600
height_px = 400
dpi = plt.rcParams['figure.dpi']

# Cut the FFT around the middle frequency
mid_freq = np.quantile(freq, 0.5)
bandwidth = 0.0005
cutoff_frequency = mid_freq + bandwidth
plt.figure(plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi))
plt.plot(freq, np.abs(fft))
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.xlim(np.quantile(freq, 0.5 - bandwidth * 2), np.quantile(freq, 0.5 + bandwidth * 2))
plt.axvline(cutoff_frequency, color='r', linestyle='--', label='Cutoff Frequency', linewidth=1.8)
plt.axvline(mid_freq, color='r', linestyle='--', linewidth=0.8)
plt.title('FFT')
plt.grid(True)
plt.title('FFT')
plt.grid(True)
#construct butterworth filter
nyquist_frequency = 0.5 * 1
normalized_cutoff = cutoff_frequency / nyquist_frequency
b, a = signal.butter(2, normalized_cutoff, 'low', analog=False)
filtered_signal = signal.filtfilt(b, a, sampled_data_raw)

plt.figure(plt.figure(figsize=(width_px/dpi, height_px/dpi), dpi=dpi))
plt.plot(df["Index"], sampled_data_raw, label="Raw", linewidth=0.6)
plt.plot(df["Index"], filtered_signal, label="Filtered Signal", linewidth=0.8)
plt.xlim(0, 50000)
plt.legend()
plt.grid(True)
plt.show()

# get the impulse response of the filter
print(b)
print(a)
