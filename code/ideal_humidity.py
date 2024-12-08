import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

print("Input the ideal humidity values (max, min)")
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

# Sensor IDs
hum_bme_id = 369
hum_dht_id = 368

# Retrieve values
hum_values_bme, percent_bme = get_values(hum_bme_id)
hum_values_dht, percent_dht = get_values(hum_dht_id)

print(f"The percentage of ideal humidity (BME): {percent_bme:.2f}%")
print(f"The percentage of ideal humidity (DHT): {percent_dht:.2f}%")

# Convert start time to datetime
start_time_str = "20:30"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps dynamically
num_points = len(hum_values_bme)
timestamps = [start_time + timedelta(minutes=i) for i in range(num_points)]

# Plotting
plt.style.use("seaborn-v0_8-darkgrid")
matplotlib.use("MacOSX")

# --- Humidity Graph ---
fig1, ax = plt.subplots(figsize=(12, 6))

ax.plot(timestamps[:len(hum_values_dht)], hum_values_dht, marker="x", linestyle="-", color="blue",
        label="DHT Humidity", linewidth=1.5, markersize=4)
ax.plot(timestamps, hum_values_bme, marker="o", linestyle="-", color="orange",
        label="BME Humidity", linewidth=1.5, markersize=4)

# Fill between ideal humidity range
ax.fill_between(timestamps, y_min, y_max, color='lightgreen', alpha=0.3, label="Ideal Range")

# Add threshold lines
ax.axhline(y_max, color='red', linewidth=1, linestyle='--', label=f"Max Ideal Humidity ({y_max}%)")
ax.axhline(y_min, color='red', linewidth=1, linestyle='--', label=f"Min Ideal Humidity ({y_min}%)")

# Customize plot
ax.set_title("Humidity Readings Over Time", fontsize=16)
ax.set_xlabel("Time", fontsize=12)
ax.set_ylabel("Humidity (%)", fontsize=12)

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
ax_pie_bme.set_title("BME Humidity Ideal Range %", fontsize=14)

# Pie chart for DHT sensor
pie_sizes_dht = [percent_dht, 100 - percent_dht]
ax_pie_dht.pie(pie_sizes_dht, labels=pie_labels, autopct='%1.1f%%', startangle=90, colors=pie_colors, wedgeprops={'edgecolor': 'black'})
ax_pie_dht.set_title("DHT Humidity Ideal Range %", fontsize=14)

plt.tight_layout()
plt.show()

