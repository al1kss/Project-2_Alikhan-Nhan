import matplotlib
import numpy as np
import requests
from matplotlib import pyplot as plt


def get_values(sensor_id, server_ip = "192.168.4.137"):
    # Fetch data from the server
    r = requests.get(f"http://{server_ip}/readings")
    data = r.json()
    readings = data.get("readings", [])
    out = []
    for k in readings:
        for v in k:
            if v["sensor_id"] == sensor_id:
                if sensor_id == 367:  # if the sensor is dht
                    if v["value"] < 14:
                        try:
                            out.append(out[-1])
                        except IndexError:
                            out.append(20.0)
                    else:
                        out.append(v["value"])
                    continue
                out.append(v["value"])
    return out

def gen_polynomial_graph(x: list, y: list, deg: int):
    coefficients = np.polyfit(x, y, deg) #generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients) #generate polynomial as an object
    x_graph = np.linspace(min(x), max(x))
    y_graph = polynomial(x_graph)
    return x_graph, y_graph

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

deg = 70

x_ = list(range(0,720))
x, y = gen_polynomial_graph(x_, temp_values_bme[-720:],deg)

fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

# Temperature
axs[0].plot(x, y, marker="o", linestyle="-", color="orange",
            label=f"BME Temp, {deg} degree", linewidth=0.8, markersize=4)

x, y = gen_polynomial_graph(x_, temp_values_dht[-720:],deg)
axs[0].plot(x, y, marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label=f"DHT Temp, {deg} degree")
axs[0].set_title("Temperature Readings for the next 12 hours")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()

# Humidity
x, y = gen_polynomial_graph(x_, hum_values_bme[-720:],deg)
axs[1].plot(x, y, marker="o", linestyle="-", color="orange",
            label="BME Humidity", linewidth=0.8, markersize=4)

x, y = gen_polynomial_graph(x_, hum_values_dht[-720:],deg)

axs[1].plot(x, y, marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label="DHT Humidity")
axs[1].set_title("Humidity Readings for the next 12 hours")
axs[1].set_ylabel("Humidity (%)")
axs[1].legend()

# Pressure
x, y = gen_polynomial_graph(x_, pres_values[-720:],deg)
axs[2].plot(x, y, marker="o", linestyle="-", color="purple",
            label="BME Pressure", linewidth=0.8, markersize=4)
axs[2].set_title("Pressure Readings for the next 12 hours")
axs[2].set_ylabel("Pressure (hPa)")
axs[2].legend()


# Define hourly labels for the x-axis
hours = [f"Hour {i}" for i in range(1, 13)]  # 'Hour 1' to 'Hour 12'
hour_positions = [i * 60 for i in range(12)]  # Corresponding positions (every 60 minutes)
# Set the x-axis labels
plt.xticks(hour_positions, hours, rotation=45)

plt.tight_layout()
plt.show()
