import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

print("Input the ideal temperature values (max, min)")
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
                if sensor_id == 367: #if the sensor is dht
                    if v["value"] < 14:
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

# Sensor IDs
temp_bme_id = 366
temp_dht_id = 367

# Retrieve values
temp_values_bme, percent_bme = get_values(temp_bme_id)
temp_values_dht, percent_dht = get_values(temp_dht_id)

print(f"The percentage of ideal temperature (BME): {percent_bme:.2f}%")
print(f"The percentage of ideal temperature (DHT): {percent_dht:.2f}%")

# Convert start time to datetime
start_time_str = "20:30"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps dynamically
num_points = len(temp_values_bme)
timestamps = [start_time + timedelta(minutes=i) for i in range(num_points)]

# Plotting
plt.style.use("seaborn-v0_8-darkgrid")
matplotlib.use("MacOSX")

# --- Temperature Graph ---
fig1, ax = plt.subplots(figsize=(12, 6))

ax.plot(timestamps[:len(temp_values_dht)], temp_values_dht, marker="x", linestyle="-", color="blue",
        label="DHT Temp", linewidth=1.5, markersize=4)
ax.plot(timestamps, temp_values_bme, marker="o", linestyle="-", color="orange",
        label="BME Temp", linewidth=1.5, markersize=4)

# Fill between ideal temperature range
ax.fill_between(timestamps, y_min, y_max, color='lightgreen', alpha=0.3, label="Ideal Range")

# Add threshold lines
ax.axhline(y_max, color='red', linewidth=1, linestyle='--', label=f"Max Ideal Temp ({y_max}°C)")
ax.axhline(y_min, color='red', linewidth=1, linestyle='--', label=f"Min Ideal Temp ({y_min}°C)")

# Customize plot
ax.set_title("Temperature Readings Over Time", fontsize=16)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("Temperature (°C)", fontsize=12)

# Dynamic x-axis tick frequency
num_ticks = 16  # Desired number of ticks
tick_interval = max(len(timestamps) // num_ticks, 1)
ax.xaxis.set_major_locator(mdates.MinuteLocator(interval=tick_interval))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))

plt.xticks(rotation=45, fontsize=10)

ax.legend()
plt.tight_layout()
plt.show()

# --- Pie Chart for BME and DHT Together ---
fig2, (ax_pie_bme, ax_pie_dht) = plt.subplots(1, 2, figsize=(14, 6))

pie_labels = ['Within Ideal Range', 'Outside Ideal Range']
pie_colors = ['lightgreen', 'lightcoral']

# Pie chart for BME sensor
pie_sizes_bme = [percent_bme, 100 - percent_bme]
ax_pie_bme.pie(pie_sizes_bme, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'black'})
ax_pie_bme.set_title("BME Temp Ideal Range %", fontsize=14)

# Pie chart for DHT sensor
pie_sizes_dht = [percent_dht, 100 - percent_dht]
ax_pie_dht.pie(pie_sizes_dht, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'black'})
ax_pie_dht.set_title("DHT Temp Ideal Range %", fontsize=14)

plt.tight_layout()
plt.show()
