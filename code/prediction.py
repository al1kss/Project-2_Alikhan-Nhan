import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from random import randint


def get_values(sensor_id, prev_value):
    out = []
    avg_dev = []
    for k in readings:
        for v in k:
            if v["sensor_id"] == sensor_id:
                deviation = abs(v["value"]-prev_value)
                avg_dev.append(deviation)
                x = randint(0, 7)
                if x < 3:
                    out.append(v["value"] + deviation)
                elif 2 < x <= 5:
                    out.append(v["value"] - deviation)
                else:
                    out.append(v["value"])
                prev_value = v["value"]
    return out

plt.style.use("ggplot")
matplotlib.use("MacOSX")

server_ip = "192.168.4.137"

# Fetch data from the server
r = requests.get(f"http://{server_ip}/readings")
data = r.json()
readings = data.get("readings", [])

# Sensor IDs
temp_bme_id = 326
temp_dht_id = 327
hum_bme_id = 329
hum_dht_id = 328
pres_id = 330

# Retrieve values
temp_values_bme = get_values(temp_bme_id, 19.0)
temp_values_dht = get_values(temp_dht_id, 19.0)
hum_values_bme = get_values(hum_bme_id, 25.0)
hum_values_dht = get_values(hum_dht_id, 25.0)
pres_values = get_values(pres_id, 870)

# Convert start time to datetime
start_time_str = "00:00"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(12*60)]

fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

# Temperature
axs[0].plot(timestamps, temp_values_bme[-720:], marker="o", linestyle="-", color="y",
            label="BME Temp", linewidth=0.8, markersize=4)
axs[0].plot(timestamps, temp_values_dht[-720:], marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label="DHT Temp")
axs[0].set_title("Temperature Readings for the next 12 hours")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()

# Humidity
axs[1].plot(timestamps, hum_values_bme[-720:], marker="o", linestyle="-", color="y",
            label="BME Humidity", linewidth=0.8, markersize=4)
axs[1].plot(timestamps, hum_values_dht[-720:], marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label="DHT Humidity")
axs[1].set_title("Humidity Readings for the next 12 hours")
axs[1].set_ylabel("Humidity (%)")
axs[1].legend()

# Pressure
axs[2].plot(timestamps, pres_values[-720:], marker="o", linestyle="-", color="purple",
            label="BME Pressure", linewidth=0.8, markersize=4)
axs[2].set_title("Pressure Readings for the next 12 hours")
axs[2].set_ylabel("Pressure (hPa)")
axs[2].legend()

# Format x-axis
axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
axs[2].xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
