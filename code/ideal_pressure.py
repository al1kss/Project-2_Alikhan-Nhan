import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

print("Input the ideal pressure values (max, min)")
y_max, y_min = map(float, input("Input 2 values: ").split())

def get_values(sensor_id, server_ip="192.168.4.137"):
    r = requests.get(f"http://{server_ip}/readings")
    data = r.json()
    readings = data.get("readings", [])
    out = []
    percentage = 0

    for reading in readings:
        for v in reading:
            if v["sensor_id"] == sensor_id:
                if sensor_id == 367 or sensor_id == 368: #if the sensor is dht
                    if v["value"] > 30 or v["value"] < 15:
                        try:
                            out.append(out[-1])
                            if y_min <= out[-1] <= y_max:
                                percentage += 1
                        except IndexError:
                            out.append(20.0)
                            if y_min <= 20 <= y_max:
                                percentage += 1
                    else:
                        out.append(v["value"])
                        if y_min <= v["value"] <= y_max:
                            percentage += 1
                    continue
                out.append(v["value"])
                if y_min <= v["value"] <= y_max:
                    percentage += 1


    per_out = (percentage / len(out)) * 100 if out else 0
    return out, per_out

# Sensor ID
pres_id = 370

# Retrieve values
pres_values, percent = get_values(pres_id)

print(f"The percentage of ideal pressure: {percent:.2f}%")

# Convert start time to datetime
start_time_str = "20:30"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps dynamically
num_points = len(pres_values)
timestamps = [start_time + timedelta(minutes=i) for i in range(num_points)]

# Plotting
plt.style.use("seaborn-v0_8-darkgrid")
matplotlib.use("MacOSX")

# --- pressure Graph ---
fig1, ax = plt.subplots(figsize=(12, 6))

ax.plot(timestamps, pres_values, marker="o", linestyle="-", color="purple",
        label="BME pressure", linewidth=1.5, markersize=4)

# Fill between ideal pressure range
ax.fill_between(timestamps, y_min, y_max, color='lightgreen', alpha=0.3, label="Ideal Range")

# Add threshold lines
ax.axhline(y_max, color='red', linewidth=1, linestyle='--', label=f"Max Ideal Pressure ({y_max} hPa)")
ax.axhline(y_min, color='red', linewidth=1, linestyle='--', label=f"Min Ideal Pressure ({y_min} hPa)")

# Customize plot
ax.set_title("Pressure Readings Over Time", fontsize=16)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("Pressure (hPa)", fontsize=12)

# Dynamic x-axis tick frequency
num_ticks = 16  # Desired number of ticks
tick_interval = max(len(timestamps) // num_ticks, 1)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=tick_interval))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

plt.xticks(rotation=45, fontsize=10)

ax.legend()
plt.tight_layout()
plt.show()

# --- Pie Chart for BME---
fig2, (ax_pie_bme) = plt.subplots(1, 1, figsize=(7, 6))

pie_labels = ['Within Ideal Range', 'Outside Ideal Range']
pie_colors = ['lightgreen', 'lightcoral']

# Pie chart for BME sensor
pie_sizes_bme = [percent, 100 - percent]
ax_pie_bme.pie(pie_sizes_bme, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'black'})
ax_pie_bme.set_title("Pressure Ideal Range %", fontsize=14)

plt.tight_layout()
plt.show()

