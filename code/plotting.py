import matplotlib
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

def get_values(sensor_id):
    out = []
    for k in readings:
        for v in k:
            if v["sensor_id"] == sensor_id:
                out.append(v["value"])
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
    axs[0].plot(timestamps[-60:], temp_values_bme[-60:], marker="o", linestyle="-", color="y",
                label="BME Temp", linewidth=0.8, markersize=4)
    axs[0].plot(timestamps[-60:], temp_values_dht[-60:], marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Temp")
    axs[0].set_title("Temperature Readings")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].legend()

    # Humidity
    axs[1].plot(timestamps[-60:], hum_values_bme[-60:], marker="o", linestyle="-", color="y",
                label="BME Humidity", linewidth=0.8, markersize=4)
    axs[1].plot(timestamps[-60:], hum_values_dht[-60:], marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Humidity")
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
    axs[0].plot(timestamps, temp_values_bme, marker="o", linestyle="-", color="y",
                label="BME Temp", linewidth=0.8, markersize=4)
    axs[0].plot(timestamps[:len(temp_values_dht)], temp_values_dht, marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Temp")
    axs[0].set_title("Temperature Readings")
    axs[0].set_ylabel("Temperature (°C)")
    axs[0].legend()

    # Humidity
    axs[1].plot(timestamps, hum_values_bme, marker="o", linestyle="-", color="y",
                label="BME Humidity", linewidth=0.8, markersize=4)
    axs[1].plot(timestamps[:len(hum_values_dht)], hum_values_dht, marker="x", linestyle="-", color="b",
                linewidth=0.8, markersize=4, label="DHT Humidity")
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

'''--------------============ OLD CODE ==============--------------------'''
'''
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import matplotlib

def get_values(sensor_id):
    out = []
    for k in readings:
        for v in k:
            if v["sensor_id"] == sensor_id:
                out.append(v["value"])
    return out


plt.style.use("ggplot")
matplotlib.use("MacOSX")

server_ip = "192.168.4.137"

# Fetch data from the server
r = requests.get(f"http://{server_ip}/readings")
data = r.json()
readings = data.get("readings", [])

# Initialize lists for timestamps and temp_values_bme
temp_bme_id = 326
temp_dht_id = 327
hum_bme_id = 329
hum_dht_id = 328
pres_id = 330


temp_values_bme = get_values(temp_bme_id)
temp_values_dht = get_values(temp_dht_id)
hum_values_bme = get_values(hum_bme_id)
hum_values_dht = get_values(hum_dht_id)
pres_values = get_values(pres_id)

# Convert start time to datetime
start_time_str = "15:09"  # 8:51 PM in 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(len(temp_values_bme))]

print("It got as cold as:", min(temp_values_bme))
print("It got as hot as:", max(temp_values_bme))

x = input("Do you want temperature for the last hour, or for total? (yes/no) ").lower()

fig, ax = plt.subplots(figsize=(10, 8))
if x == "yes" or x=="y":
    # Plot the last hour's data
    ax.plot(timestamps[-60:], temp_values_bme[-60:], marker="o", linestyle="-", color="purple",
            label="BME Temp", linewidth=0.8, markersize=4)
    plt.plot(timestamps[-60:], temp_values_dht[-60:], marker="x", linestyle="-", color="b", linewidth=0.8, markersize=4, label="DHT Temp")
    ax.set_title(f"Temperature Readings from Sensor 138 / Last Hour")
else:
    # Plot the temp data
    plt.subplot(3,1,1)
    ax.plot(timestamps, temp_values_bme, marker="o", linestyle="-", color="y",
            label="BME Temp", linewidth=0.8, markersize=4)
    plt.plot(timestamps[:len(temp_values_dht)], temp_values_dht, marker="x", linestyle="-", color="b", linewidth=0.8, markersize=4, label="DHT Temp")
    ax.set_title(f"Temperature Readings")

    plt.subplot(3,1,2)
    ax.plot(timestamps, hum_values_bme, marker="o", linestyle="-", color="y",
            label="BME Humidity", linewidth=0.8, markersize=4)
    plt.plot(timestamps[:len(temp_values_dht)], hum_values_dht, marker="x", linestyle="-", color="b", linewidth=0.8,
             markersize=4, label="DHT Humidity")
    ax.set_title(f"Humidity Readings")

    plt.subplot(3, 1, 3)
    ax.plot(timestamps, pres_values, marker="o", linestyle="-", color="purple",
            label="BME Pressure", linewidth=0.8, markersize=4)



# Format the x-axis to show time in 24-hour format
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Adjust interval as needed
plt.xticks(rotation=45)


ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()

plt.show()
'''
