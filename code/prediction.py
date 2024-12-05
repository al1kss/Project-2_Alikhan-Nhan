import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
from random import randint


def get_values(sensor_id, readings):
    out = {
        "original": [],
        "prediction": []
    }
    prev_value = 0
    for v in readings[0]:
        if v["sensor_id"] == sensor_id:
            prev_value = v["value"]
            break

    for v in readings[0]:
        if v["sensor_id"] == sensor_id:
            # get real value
            out["original"].append(v["value"])

            # get corresponding prediction
            deviation = abs(v["value"]-prev_value)
            x = randint(0, 7)
            if x < 3:
                out["prediction"].append(v["value"] + deviation)
            elif 2 < x <= 5:
                out["prediction"].append(v["value"] - deviation)
            else:
                out["prediction"].append(v["value"])
            prev_value = v["value"]


    return out

plt.style.use("ggplot")


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
temp_bme = get_values(temp_bme_id, readings)
temp_dht = get_values(temp_dht_id, readings)
hum_bme = get_values(hum_bme_id, readings)
hum_dht = get_values(hum_dht_id, readings)
pressure = get_values(pres_id, readings)

temp_values_bme = temp_bme["prediction"]
temp_values_dht = temp_dht["prediction"]
hum_values_bme = hum_bme["prediction"]
hum_values_dht = hum_dht["prediction"]
pres_values = pressure["prediction"]

temp_values_original_bme = temp_bme["original"]
temp_values_original_dht = temp_dht["original"]
hum_values_original_bme = hum_bme["original"]
hum_values_original_dht = hum_dht["original"]
pres_values_original = pressure["original"]

# Convert start time to datetime
start_time_str = "00:00"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(12*60)]

# Create a single figure for overlaying
plt.figure(figsize=(10, 9))

# Overlay Temperature
plt.subplot(3, 1, 1)
plt.plot(timestamps, temp_values_bme[-720:], marker="o", linestyle="-", color="y",
         label="BME Temp (Current)", linewidth=0.8, markersize=4)
plt.plot(timestamps, temp_values_dht[-720:], marker="x", linestyle="-", color="b",
         linewidth=0.8, markersize=4, label="DHT Temp (Current)")
plt.plot(timestamps, temp_values_original_bme[-720:], marker="o", linestyle="--", color="orange",
         label="BME Temp (Original)", linewidth=0.8, markersize=4)
plt.plot(timestamps, temp_values_original_dht[-720:], marker="x", linestyle="--", color="cyan",
         linewidth=0.8, markersize=4, label="DHT Temp (Original)")
plt.title("Temperature Readings for the next 12 hours")
plt.ylabel("Temperature (°C)")
plt.legend()

# Overlay Humidity
plt.subplot(3, 1, 2)
plt.plot(timestamps, hum_values_bme[-720:], marker="o", linestyle="-", color="y",
         label="BME Humidity (Current)", linewidth=0.8, markersize=4)
plt.plot(timestamps, hum_values_dht[-720:], marker="x", linestyle="-", color="b",
         linewidth=0.8, markersize=4, label="DHT Humidity (Current)")
plt.plot(timestamps, hum_values_original_bme[-720:], marker="o", linestyle="--", color="orange",
         label="BME Humidity (Original)", linewidth=0.8, markersize=4)
plt.plot(timestamps, hum_values_original_dht[-720:], marker="x", linestyle="--", color="cyan",
         linewidth=0.8, markersize=4, label="DHT Humidity (Original)")
plt.title("Humidity Readings for the next 12 hours")
plt.ylabel("Humidity (%)")
plt.legend()

# Overlay Pressure
plt.subplot(3, 1, 3)
plt.plot(timestamps, pres_values[-720:], marker="o", linestyle="-", color="purple",
         label="BME Pressure (Current)", linewidth=0.8, markersize=4)
plt.plot(timestamps, pres_values_original[-720:], marker="o", linestyle="--", color="orange",
         label="BME Pressure (Original)", linewidth=0.8, markersize=4)
plt.title("Pressure Readings for the next 12 hours")
plt.ylabel("Pressure (hPa)")
plt.legend()

# Format x-axis for all subplots
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
