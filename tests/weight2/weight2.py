import os
import numpy as np
import pandas as pd
from scipy import signal
from datetime import datetime, timedelta
import argparse
import matplotlib.pyplot as plt

# Set working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Read data from CSV
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
fft_quantiles = np.quantile(np.abs(fft), [0.25, 0.5, 0.75])
freq_quantiles = np.quantile(freq, [0.25, 0.5, 0.75])

# Plot FFT
plt.figure()
plt.plot(freq, np.abs(fft))
plt.plot(freq_quantiles, fft_quantiles, 'ro')
plt.xlabel('Frequency')
plt.ylabel('Magnitude')
plt.title('FFT')
plt.grid(True)

# Apply Butterworth filter
cutoff_frequency = 0.01
nyquist_frequency = 0.5 * 1
normalized_cutoff = cutoff_frequency / nyquist_frequency
b, a = signal.butter(4, normalized_cutoff, 'low', analog=False)
#zi = signal.lfilter_zi(b, a)
#filtered_signal, _ = signal.lfilter(b, a, sampled_data_raw, zi=zi*sampled_data_raw[0])
#filtered_signal = signal.filtfilt(b, a, sampled_data_raw, zi=zi*sampled_data_raw[0])
filtered_signal = signal.filtfilt(b, a, sampled_data_raw)
np.array2string(b, separator=', ')

with open("impulse_response", "w") as f:
    f.write(np.array2string(b, separator=', '))

# Plot filtered signal
plt.figure()
plt.plot(df["Index"], sampled_data_raw, label="Raw", linewidth=0.6)
plt.plot(df["Index"], filtered_signal, label="Filtered Signal", linewidth=0.8)
plt.grid(True)
plt.legend()

# Show plots
plt.show()