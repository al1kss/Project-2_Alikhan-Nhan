#mean of 2 sensors
import matplotlib
import numpy as np
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
average_temp = get_values(temp_bme_id)
temp_values_dht = get_values(temp_dht_id)
average_hum = get_values(hum_bme_id)
hum_values_dht = get_values(hum_dht_id)
pres_values = get_values(pres_id)

average_temp = [(average_temp[i]+temp_values_dht[i])/2.0 for i in range(len(average_temp))]
average_hum = [(average_hum[i]+hum_values_dht[i])/2.0 for i in range(len(average_hum))]

# Convert start time to datetime
start_time_str = "20:30"  # 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(len(average_temp))]

print("It got as cold as:", min(average_temp))
print("It got as hot as:", max(average_temp))

x = input("Do you want temperature for the last hour, or for total? (yes/no) ").lower()

if x == "yes" or x == "y":
    fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    # Temperature
    axs[0].plot(timestamps[-60:], average_temp[-60:], marker="o", linestyle="-", color="green",
                linewidth=0.8, markersize=4, label="Average of Sensors")
    axs[0].set_title("Average Temperature Readings of 2 sensors")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].legend()

    # Humidity
    axs[1].plot(timestamps[-60:], average_hum[-60:], marker="o", linestyle="-", color="red",
                linewidth=0.8, markersize=4, label="Average of Sensors")
    axs[1].set_title("Average Humidity Readings of 2 sensors")
    axs[1].set_ylabel("Humidity (%)")
    axs[1].legend()

    # Format x-axis
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    axs[1].xaxis.set_major_locator(mdates.HourLocator(interval=1))
    plt.xticks(rotation=45)
else:
    # Create subplots for all data
    fig, axs = plt.subplots(2, 1, figsize=(10, 6), sharex=True)

    # Temperature
    axs[0].plot(timestamps, average_temp, marker="o", linestyle="-", color="green",
                linewidth=0.8, markersize=4, label="Average of Sensors")
    axs[0].set_title("Average Temperature Readings of 2 sensors")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].axhline(max(average_temp), color='black', linewidth=1, linestyle='--', label=f"Max Temp ({max(average_temp):.1f}°C)")
    axs[0].axhline(min(average_temp), color='black', linewidth=1, linestyle='--',
                   label=f"Max Temp ({min(average_temp):.1f}°C)")
    temp_median_bme = np.median(average_temp)
    axs[0].axhline(temp_median_bme, color='green', linewidth=1, linestyle='--',
                   label=f"Median Temp ({temp_median_bme:.1f}°C)")
    axs[0].legend()

    # Humidity
    axs[1].plot(timestamps, average_hum, marker="o", linestyle="-", color="red",
                label="Average of Sensors", linewidth=0.8, markersize=4)
    axs[1].set_title("Average Humidity Readings of 2 sensors")
    axs[1].set_ylabel("Humidity (%)")
    axs[1].axhline(max(average_hum), color='black', linewidth=1, linestyle='--', label=f"Max Hum ({max(average_hum):.1f} %)")
    axs[1].axhline(min(average_hum), color='black', linewidth=1, linestyle='--',
                   label=f"Max Hum ({min(average_hum):.1f} %)")
    hum_median_bme = np.median(average_hum)
    axs[1].axhline(hum_median_bme, color='green', linewidth=1, linestyle='--',
                   label=f"Median Hum ({hum_median_bme:.1f} %)")
    axs[1].legend()


    # Format x-axis
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
    axs[1].xaxis.set_major_locator(mdates.HourLocator(interval=1))
    plt.xticks(rotation=45)

plt.tight_layout()
plt.show()
