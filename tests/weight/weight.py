import os
import numpy as np
import pandas as pd
import udsp
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

stat = udsp.stat(script_dir + "/libudsp.so")

df = pd.read_csv("data/weight.csv", header=None)

#rename columns
df.columns = ["Time", "Q", "R", "S"]
df["Q"] = df["Q"].astype(float)
df["R"] = df["R"].astype(float)
df["S"] = df["S"].astype(float)
df["Q_shifted_1"] = df["Q"].shift(1).astype(float)
df["R_shifted_1"] = df["R"].shift(1).astype(float)
df["S_shifted_1"] = df["S"].shift(1).astype(float)
df["Q_shifted_2"] = df["Q"].shift(2).astype(float)
df["R_shifted_2"] = df["R"].shift(2).astype(float)
df["S_shifted_3"] = df["S"].shift(2).astype(float)
df["Q_shifted_3"] = df["Q"].shift(3).astype(float)
df["R_shifted_3"] = df["R"].shift(3).astype(float)
df["S_shifted_3"] = df["S"].shift(3).astype(float)

df.dropna(inplace=True)

df['C'] = df.apply(lambda x: stat.mean([x["Q"], x["Q_shifted_1"], x["Q_shifted_2"], x["Q_shifted_3"]]), axis=1)

plt.plot(df["Time"], df["Q"], label="Q")
plt.plot(df["Time"], df["R"], label="R")
plt.plot(df["Time"], df["S"], label="S")
plt.plot(df["Time"], df["C"], label="C")
plt.legend()
plt.show()