import os
import numpy as np
import pandas as pd
from scipy import signal
from datetime import datetime, timedelta
import argparse
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Parse command line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--time_start")
parser.add_argument("--time_end")
parser.add_argument("--cutoff_frequency")
args = parser.parse_args()

time_start = args.time_start or datetime.strptime('06:42:11.000', '%H:%M:%S.%f')
time_end = args.time_end or datetime.strptime('06:42:14.080', '%H:%M:%S.%f')
#cutoff_frequency = args.cutoff_frequency or 0.01
time_format = '%H:%M:%S.%f'
date_format = mdates.DateFormatter('%H:%M:%S')

# Set working directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Read data from CSV
df = pd.read_csv("weight.csv", header=None)
df.dropna(inplace=True)

# Rename columns
df.columns = ["Time", "Q", "R", "S"]
df["Time"] = pd.to_datetime(df["Time"], format=time_format)
df["Q"] = df["Q"].astype(float)
df["R"] = df["R"].astype(float)
df["S"] = df["S"].astype(float)

# Filter data based on time range
if time_start is not None:
    df = df[df.iloc[:, 0] >= time_start].reset_index(drop=True)
if time_end is not None:
    df = df[df.iloc[:, 0] <= time_end]

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
fs = len(df.iloc[0:,0]) / (df.iloc[-1,0] - df.iloc[0, 0]).total_seconds()
cutoff_frequency = args.cutoff_frequency or 0.1
b, a = signal.butter(4, cutoff_frequency, 'low', analog=False, fs = fs)
zi = signal.lfilter_zi(b, a)
filtered_signal, _ = signal.lfilter(b, a, sampled_data_raw, zi=zi*sampled_data_raw[0])
filtered_signal = signal.filtfilt(b, a, sampled_data_raw)

# Plot filtered signal
plt.figure()
plt.plot(df["Time"], sampled_data_raw, label="Raw")
plt.plot(df["Time"], df["R"], label="VB Filter 0")
plt.plot(df["Time"], df["S"], label="VB Filter 1")
plt.plot(df["Time"], filtered_signal, label="Filtered Signal")
plt.grid(True)
plt.legend()
plt.gca().xaxis.set_major_formatter(date_format)

# Show plots
plt.show()