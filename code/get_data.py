import requests

import time

import bme280 # pip install RPI.BME280
from smbus2 import SMBus

# set up bmp280 connection with raspberri pi

address = 0x76
bus = SMBus(1)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

# function get temp & pressure from bmp
def bmp280_get_data():
    address = 0x76
    bus = SMBus(1)
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    temperature = data.temperature
    pressure = data.pressure
    humidity = data.humidity

    dict_ = {
        'Temperature': temperature,
        "Humidity": humidity,
        'Pressure': pressure
    }
    return dict_

# class for http requests
class http:
    # initiate variable for the instance
    def __init__(self, server_ip:str, username:str, password:str, sensor_location:str):
        self.server_ip = server_ip
        self.username = username
        self.password = password
        self.sensor_location = sensor_location

        self.access_token = ""

        self.sensor_id_temperature = 0
        self.sensor_id_humidity = 0
        self.sensor_id_pressure = 0

    # method to register user
    def register(self):
        user = {"username": f'{self.username}', 'password': f'{self.password}'}
        r = requests.post(f"http://{self.server_ip}/register", json = user)
        return r.json()

    # method to get token
    def get_token(self):
        user = {"username": f'{self.username}', 'password': f'{self.password}'}
        r = requests.post(f"http://{self.server_ip}/login", json=user)

        self.access_token = r.json()["access token"] #return token for access

        return self.access_token

    #method to create new sensor and get id
    def create_new_sensor_all_type(self):
        auth = {"Authorization": f"Bearer {self.access_token}"}

        temperature_sensor = {"type": "Temperature", "location": f"{self.sensor_location}", "name": f"Temperature {self.sensor_location}", "unit": "C"}
        temperature_r = requests.post(f'http://{self.server_ip}/sensor/new', json=temperature_sensor, headers=auth)
        self.sensor_id_temperature = temperature_r.json()['id'] # update the instance's variable

        humidity_sensor = {"type": "Humidity", "location": f"{self.sensor_location}", "name": f"Humidity {self.sensor_location}", "unit": "%"}
        humidity_r = requests.post(f'http://{self.server_ip}/sensor/new', json=humidity_sensor, headers=auth)
        self.sensor_id_humidity = humidity_r.json()['id']

        pressure_sensor = {"type": "Pressure", "location": f"{self.sensor_location}", "name": f"Pressure {self.sensor_location}", "unit": "Pa"}
        pressure_r = requests.post(f'http://{self.server_ip}/sensor/new', json=pressure_sensor, headers=auth)
        self.sensor_id_pressure = pressure_r.json()['id'] # update the instance's variable

        return f'Temperature sensor ID is {self.sensor_id_temperature}, Humidity sensor id is {self.sensor_id_humidity}, Pressure sensor id is{self.sensor_id_pressure}'

    #method to update temperature
    def update_all_censor(self):
        auth = {"Authorization": f"Bearer {self.access_token}"}
#get the sensor data from get data function

        temperature_data = {'sensor_id': self.sensor_id_temperature, 'value': sensor_data['Temperature']}
        temperature_r = requests.post(f'http://{self.server_ip}/reading/new', json=temperature_data, headers=auth)

        humidity_data = {'sensor_id': self.sensor_id_humidity, 'value': sensor_data['Humidity']}
        humidity_r = requests.post(f'http://{self.server_ip}/reading/new', json=humidity_data, headers=auth)

        pressure_data = {'sensor_id': self.sensor_id_pressure, 'value': sensor_data['Pressure']}
        pressure_r = requests.post(f'http://{self.server_ip}/reading/new', json=pressure_data, headers=auth)

        return f'The temperature data sent was {temperature_r.json()}\n The Pressure data sent was {pressure_r.json()}'

    def get_readings(self):
        auth = auth = {"Authorization": f"Bearer {self.access_token}"}
        r = requests.post(f'http://{self.server_ip}/user/readings', headers=auth)
        data = r.json()
        readings = data.get("readings", [])
        values = []
        for k in readings:
            for v in k:
                if v["sensor_id"] == self.sensor_id_temperature: #for temp only NOW
                    values.append(v["value"])

        return values

#~~~~~~~~~~~~~~

server = http(server_ip='192.168.4.137', username=input("What is the username you want to choose"), password=input("What is the password that you want to use?"), sensor_location=input("Where are the censors located at?"), bmp280=bmp280)
server.register()
server.get_token()
server.create_new_sensor_all_type()

time_elapsed = 0
time_since_last_token_refresh = 0

while time_elapsed < 172800: #3600*48 seconds
    if time_since_last_token_refresh > 9000: #60*10 seconds, every 10 minutes, cuze the auth token expires in 10 minutes iirc
        server.get_token()
        time_since_last_token_refresh = 0

    server.update_all_censor()

    time.sleep(60)

    time_elapsed += 60
    time_since_last_token_refresh += 60

values = server.get_readings()
print(f"All temperature data collected so far: \n")
