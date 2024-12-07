import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def get_values(sensor_id, server_ip = "192.168.4.137"):
    r = requests.get(f"http://{server_ip}/readings")
    data = r.json()
    readings = data.get("readings", [])
    out = []
    for k in readings:
        for v in k:
            if v["sensor_id"] == sensor_id:
                if sensor_id == 368 or sensor_id == 367: #check if the sensor is the humidity/temperature
                    if v["value"] > 30 or v["value"] < 15: #check if the humidirt value is high
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

# Convert start time to datetime
start_time_str = "20:30"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(len(temp_values_bme))]

print("It got as cold as:", min(temp_values_bme))
print("It got as hot as:", max(temp_values_bme))

x = input("Do you want temperature for the last hour, or for total? (yes/no) ").lower()

if x == "yes" or x == "y":
    fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

    # Temperature
    axs[0].plot(timestamps[-60:], temp_values_dht[-60:], marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Temp")
    axs[0].plot(timestamps[-60:], temp_values_bme[-60:], marker="o", linestyle="-", color="orange",
                label="BME Temp", linewidth=0.8, markersize=4)
    axs[0].set_title("Temperature Readings")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].legend()

    # Humidity
    axs[1].plot(timestamps[-60:], hum_values_dht[-60:], marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Humidity")
    axs[1].plot(timestamps[-60:], hum_values_bme[-60:], marker="o", linestyle="-", color="orange",
                label="BME Humidity", linewidth=0.8, markersize=4)
    axs[1].set_title("Humidity Readings")
    axs[1].set_ylabel("Humidity (%)")
    axs[1].legend()

    # Pressure
    axs[2].plot(timestamps[-60:], pres_values[-60:], marker="o", linestyle="-", color="purple",
                label="BME Pressure", linewidth=0.8, markersize=4)
    axs[2].set_title("Pressure Readings")
    axs[2].set_ylabel("Pressure (hPa)")
    axs[2].legend()

    # Format x-axis
    axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    axs[2].xaxis.set_major_locator(mdates.HourLocator(interval=1))
    plt.xticks(rotation=45)
else:
    # Create subplots for all data
    fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

    # Temperature
    axs[0].plot(timestamps[:len(temp_values_dht)], temp_values_dht, marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Temp")
    axs[0].plot(timestamps, temp_values_bme, marker="o", linestyle="-", color="orange",
                label="BME Temp", linewidth=0.8, markersize=4)
    axs[0].set_title("Temperature Readings")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].legend()

    # Humidity
    axs[1].plot(timestamps[:len(hum_values_dht)], hum_values_dht, marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Humidity")
    axs[1].plot(timestamps, hum_values_bme, marker="o", linestyle="-", color="orange",
                label="BME Humidity", linewidth=0.8, markersize=4)
    axs[1].set_title("Humidity Readings")
    axs[1].set_ylabel("Humidity (%)")
    axs[1].legend()

    # Pressure
    axs[2].plot(timestamps, pres_values, marker="o", linestyle="-", color="purple",
                label="BME Pressure", linewidth=0.8, markersize=4)
    axs[2].set_title("Pressure Readings")
    axs[2].set_ylabel("Pressure (hPa)")
    axs[2].legend()

    # Format x-axis
    axs[2].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    axs[2].xaxis.set_major_locator(mdates.HourLocator(interval=1))
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
