import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#file inputs:
input_file = r"C:\Users\taiya\anaconda3\envs\SOAR2\Lib\site-packages\MAPLEAF\Aneeshox\StaticFire\staticfire.txt"

output_file = r"C:\Users\taiya\anaconda3\envs\SOAR2\Lib\site-packages\MAPLEAF\Aneeshox\StaticFire\AegisStaticFire1.txt"

#read
with open(input_file, "r", encoding="utf-8", errors="ignore") as f:
    lines = f.readlines()

#look for thrust > 0
data_start = None

for i, line in enumerate(lines):
    if line.startswith("X_Value"):
        data_start = i
        break

if data_start is None:
    raise ValueError("Could not find X_Value header that is nonzero")

#convert headers to list of strings, removing empty headers and stripping whitespace
headers = lines[data_start].strip().split("\t")
headers = [h.strip() for h in headers if h.strip() != ""]

#parse data rows, skipping empty lines and lines with fewer columns than headers
parsed_rows = []

for line in lines[data_start + 1:]:

    line = line.strip()

    if line == "":
        continue

    cols = line.split("\t")
    cols = [c.strip() for c in cols]

    if len(cols) < len(headers):
        continue

    parsed_rows.append(cols[:len(headers)])

#using pandas to create a dataframe from the parsed rows and headers with test data

df_full = pd.DataFrame(parsed_rows, columns=headers)

#column strings:

rename_map = {
    "X_Value": "Time (s)",
    "Injector Temp": "Injector Temp (C)",
    "NOX Pressure": "NOX Pressure (PSI)",
    "Ox Tank Load Cell": "Ox Tank Load Cell (kg)",
    "Thrust Load Cell": "Thrust Load Cell (lbf)",
    "Chamber Pressure": "Chamber Pressure (PSI)",
    "Light Sensor": "Light Sensor (V)",
    "Nitrous Bottle": "Nitrous Bottle (PSI)"
}

df_full.rename(columns=rename_map, inplace=True)

#data write:

for col in df_full.columns:
    if col != "Comment":
        df_full[col] = pd.to_numeric(df_full[col], errors="coerce")

#PLOT FULL DATA FINAL
x_full = np.array(df_full["Time (s)"].tolist(), dtype=float)
y_full = np.array(df_full["Thrust Load Cell (lbf)"].tolist(), dtype=float)

plt.figure(figsize=(14, 6))

plt.plot(x_full, y_full)

plt.xlabel("Time (s)")
plt.ylabel("Thrust Load Cell (lbf)")
plt.title("Original Static Fire Data")
plt.grid(True)

plt.tight_layout()

#SECOND PLOT TEST
df = df_full.copy()

thrust_col = "Thrust Load Cell (lbf)"

test_df = df[df[thrust_col] > 1.0]

if test_df.empty:
    raise ValueError("No test region found.")

start_idx = max(test_df.index[0] - 100, 0)
end_idx = min(test_df.index[-1] + 100, len(df) - 1)

df = df.loc[start_idx:end_idx].reset_index(drop=True)

#PLOT PARSED DATA FINAL FINAL 2
x_parsed = np.array(df["Time (s)"].tolist(), dtype=float)
y_parsed = np.array(df["Thrust Load Cell (lbf)"].tolist(), dtype=float)

plt.figure(figsize=(14, 6))

plt.plot(x_parsed, y_parsed)

plt.xlabel("Time (s)")
plt.ylabel("Thrust Load Cell (lbf)")
plt.title("Parsed Static Fire Data")
plt.grid(True)

plt.tight_layout()

#COMBINED PLOT:
plt.figure(figsize=(14, 7))

plt.plot(
    x_full,
    y_full,
    label="Original",
    alpha=0.5
)

plt.plot(
    x_parsed,
    y_parsed,
    label="Parsed",
    linewidth=2
)

plt.xlabel("Time (s)")
plt.ylabel("Thrust Load Cell (lbf)")
plt.title("Original vs Parsed Static Fire")
plt.grid(True)
plt.legend()

plt.tight_layout()

#SHOW ALL PLOTS:

plt.show()

#WRITE TO CSV: git checkout Rothney-to-Mapleaf-input-StaticFire-data

df.to_csv(output_file, index=False)

print("\nFinished parsing static fire data.")
print(f"Saved cleaned file to:\n{output_file}")