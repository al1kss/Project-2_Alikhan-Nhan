from collections import defaultdict
import requests
from matplotlib import pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta
import matplotlib

plt.style.use("ggplot")
matplotlib.use("MacOSX")

server_ip = "192.168.4.137"

# Fetch data from the server
r = requests.get(f"http://{server_ip}/readings")
data = r.json()
readings = data.get("readings", [])

# Initialize lists for timestamps and values
timestamps = []
values = []

# Extract data for sensor_id 138
for k in readings:
    for v in k:
        if v["sensor_id"] == 138:
            values.append(v["value"])

# Convert start time to datetime
start_time_str = "20:51"  # 8:51 PM in 24-hour format
start_time = datetime.strptime(start_time_str, "%H:%M")

# Generate timestamps as datetime objects
timestamps = [start_time + timedelta(minutes=i) for i in range(len(values))]

print("It got as cold as:", min(values))
print("It got as hot as:", max(values))

fig, ax = plt.subplots(figsize=(12, 6))
x = input("Do you want temperature for the last hour, or for total? (yes/no) ").lower()

if x == "yes" or x=="y":
    # Plot the last hour's data
    ax.plot(timestamps[-60:], values[-60:], marker="o", linestyle="-", color="purple",
            label="Sensor 138 Temperature", linewidth=0.8, markersize=4)
    ax.set_title("Temperature Readings from Sensor 138 / Last Hour")
else:
    # Plot the total data
    ax.plot(timestamps, values, marker="o", linestyle="-", color="y",
            label="Sensor 138 Temperature", linewidth=0.8, markersize=4)
    ax.set_title("Temperature Readings from Sensor 138")

# Format the x-axis to show time in 24-hour format
ax.xaxis.set_major_formatter(mdates.DateFormatter("%H:%M"))
ax.xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Adjust interval as needed
plt.xticks(rotation=45)


ax.set_xlabel("Time")
ax.set_ylabel("Temperature")
ax.legend()

plt.show()
