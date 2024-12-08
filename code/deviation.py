import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import numpy as np

def get_values(sensor_id, server_ip="192.168.4.137"):
    r = requests.get(f"http://{server_ip}/readings")
    data = r.json()
    readings = data.get("readings", [])
    out = []
    for k in readings:
        for v in k:
            if v["sensor_id"] == sensor_id:
                if sensor_id == 368 or sensor_id == 367:  # check if the sensor is humidity/temperature
                    if v["value"] > 30 or v["value"] < 15:  # check if the humidity value is high
                        try:
                            out.append(out[-1])
                        except IndexError:
                            out.append(20.0)
                    else:
                        out.append(v["value"])
                    continue
                out.append(v["value"])
    return out

plt.style.use("ggplot")
matplotlib.use("MacOSX")

# Sensor IDs
temp_bme_id = 366
temp_dht_id = 367
hum_bme_id = 369
hum_dht_id = 368
pres_id = 370

# Retrieve values
temp_values_bme = get_values(temp_bme_id)
temp_values_dht = get_values(temp_dht_id)
hum_values_bme = get_values(hum_bme_id)
hum_values_dht = get_values(hum_dht_id)
pres_values = get_values(pres_id)

# Generate deviations
temp_dev_bme = np.std(temp_values_bme)
temp_dev_dht = np.std(temp_values_dht)
hum_dev_bme = np.std(hum_values_bme)
hum_dev_dht = np.std(hum_values_dht)
pres_dev = np.std(pres_values)

# Convert start time to datetime
start_time_str = "20:30"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(len(temp_values_bme))]

print("It got as cold as:", min(temp_values_bme))
print("It got as hot as:", max(temp_values_bme))

# Plot all data
fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

# Temperature
axs[0].plot(timestamps, temp_values_dht, marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label="DHT Temp")
axs[0].fill_between(timestamps,
                    [val - temp_dev_dht for val in temp_values_dht],
                    [val + temp_dev_dht for val in temp_values_dht],
                    color="b", alpha=0.3, label="DHT Deviation")

axs[0].plot(timestamps, temp_values_bme, marker="o", linestyle="-", color="orange",
            linewidth=0.8, markersize=4, label="BME Temp")
axs[0].fill_between(timestamps,
                    [val - temp_dev_bme for val in temp_values_bme],
                    [val + temp_dev_bme for val in temp_values_bme],
                    color="orange", alpha=0.3, label="BME Deviation")
axs[0].set_title("Temperature Readings")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()

# Humidity
axs[1].plot(timestamps, hum_values_dht, marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label="DHT Humidity")
axs[1].fill_between(timestamps,
                    [val - hum_dev_dht for val in hum_values_dht],
                    [val + hum_dev_dht for val in hum_values_dht],
                    color="b", alpha=0.3, label="DHT Deviation")

axs[1].plot(timestamps, hum_values_bme, marker="o", linestyle="-", color="orange",
            linewidth=0.8, markersize=4, label="BME Humidity")
axs[1].fill_between(timestamps,
                    [val - hum_dev_bme for val in hum_values_bme],
                    [val + hum_dev_bme for val in hum_values_bme],
                    color="orange", alpha=0.3, label="BME Deviation")
axs[1].set_title("Humidity Readings")
axs[1].set_ylabel("Humidity (%)")
axs[1].legend()

# Pressure
axs[2].plot(timestamps, pres_values, marker="o", linestyle="-", color="purple",
            linewidth=0.8, markersize=4, label="BME Pressure")
axs[2].fill_between(timestamps,
                    [val - pres_dev for val in pres_values],
                    [val + pres_dev for val in pres_values],
                    color="purple", alpha=0.3, label="Pressure Deviation")
axs[2].set_title("Pressure Readings")
axs[2].set_ylabel("Pressure (hPa)")
axs[2].legend()

# Format x-axis
axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
axs[2].xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
