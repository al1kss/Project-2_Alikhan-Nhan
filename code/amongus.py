import requests
import Adafruit_DHT
import Adafruit_SSD1306
from PIL import Image, ImageDraw
import time
from datetime import datetime


import bme280
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus

# set up bmp280 connection with raspberri pi
address = 0x76
bus = SMBus(1)
calibration_params = bme280.load_calibration_params(bus, address)
data = bme280.sample(bus, address, calibration_params)

# set up DHT


# set up the oled display
disp = Adafruit_SSD1306.SSD1306_128_64(rst=None)
disp.begin()
disp.clear()
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)
disp.display()





# function to get temp & humidity from DHT

def read_dht11_data():
    SENSOR_TYPE = Adafruit_DHT.DHT11
    pin = 4
    humidity, temperature = Adafruit_DHT.read(SENSOR_TYPE, pin)
    dict_ = {
        "Humidity": humidity,
        "Temperature": temperature
    }
    return dict_
    


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
        'Humidity': humidity,
        'Pressure': pressure
    }
    return dict_

# class for http requests
class http:
    # initiate variable for the instance
    def __init__(self, server_ip:str, username:str, password:str, i:int, sensor_location = 'hello', sensor_id_temperature_bme = 0,sensor_id_temperature_dht = 0, sensor_id_humidity_bme = 0, sensor_id_humidity_dht = 0, sensor_id_pressure = 0):
        self.server_ip = server_ip
        self.username = username
        self.password = password
        self.sensor_location = sensor_location
        self.i = i
        self.access_token = ""

        self.sensor_id_temperature_bme = sensor_id_temperature_bme
        self.sensor_id_temperature_dht = sensor_id_temperature_dht
        self.sensor_id_humidity_bme = sensor_id_humidity_bme
        self.sensor_id_humidity_dht = sensor_id_humidity_dht
        self.sensor_id_pressure = sensor_id_pressure
        
        self.previous_humidity_dht = 0
        self.previous_temperature_dht = 0

    # method to register user
    def register(self):
        user = {"username": f'{self.username}', 'password': f'{self.password}'}
        r = requests.post(f"http://{self.server_ip}/register", json = user)
        return r.json()

    # method to get token
    def get_token(self):
        user = {"username": f'{self.username}', 'password': f'{self.password}'}
        r = requests.post(f"http://{self.server_ip}/login", json=user)

        self.access_token = r.json()["access_token"] #return token for access

        return self.access_token

    #method to create new sensor and get id
    def create_new_sensor_all_type(self):
        auth = {"Authorization": f"Bearer {self.access_token}"}

        temperature_bme_sensor = {"type": "Temperature_bme", "location": f"{self.sensor_location}", "name": f"Temperature_bme {self.sensor_location}", "unit": "C"}
        temperature_bme_r = requests.post(f'http://{self.server_ip}/sensor/new', json=temperature_bme_sensor, headers=auth)
        self.sensor_id_temperature_bme = temperature_bme_r.json()['id'] # update the instance's variable
        
        temperature_dht_sensor = {"type": "Temperature_hdt", "location": f"{self.sensor_location}", "name": f"Temperature_dht {self.sensor_location}", "unit": "C"}
        temperature_dht_r = requests.post(f'http://{self.server_ip}/sensor/new', json=temperature_dht_sensor, headers=auth)
        self.sensor_id_temperature_dht = temperature_dht_r.json()['id'] # update the instance's variable
        
        humidity_dht_sensor = {"type": "Humidity", "location": f"{self.sensor_location}", "name": f"Humidity_dht {self.sensor_location}", "unit": "%"}
        humidity_dht_r = requests.post(f'http://{self.server_ip}/sensor/new', json=humidity_dht_sensor, headers=auth)
        self.sensor_id_humidity_dht = humidity_dht_r.json()['id']
        
        humidity_bme_sensor = {"type": "Humidity", "location": f"{self.sensor_location}", "name": f"Humidity_bme {self.sensor_location}", "unit": "%"}
        humidity_bme_r = requests.post(f'http://{self.server_ip}/sensor/new', json=humidity_bme_sensor, headers=auth)
        self.sensor_id_humidity_bme = humidity_bme_r.json()['id']

        pressure_sensor = {"type": "Pressure", "location": f"{self.sensor_location}", "name": f"Pressure {self.sensor_location}", "unit": "Pa"}
        pressure_r = requests.post(f'http://{self.server_ip}/sensor/new', json=pressure_sensor, headers=auth)
        self.sensor_id_pressure = pressure_r.json()['id'] # update the instance's variable

        return f't_bme is {self.sensor_id_temperature_bme}, t_hdt is {self.sensor_id_temperature_dht}, h_hdt is {self.sensor_id_humidity_dht}, h_bme is {self.sensor_id_humidity_bme}, pressure is {self.sensor_id_pressure}'
    #method to update temperature
    def update_all_censor(self):
        auth = {"Authorization": f"Bearer {self.access_token}"}
        print(datetime.now())
        bme_data = bmp280_get_data() #get the sensor data from get data function
        dht_data = read_dht11_data()
        
        temperature_data_bme = {'sensor_id': self.sensor_id_temperature_bme, 'value': bme_data['Temperature'], "datetime": str(datetime.now())}
        temperature_bme_r = requests.post(f'http://{self.server_ip}/reading/new', json=temperature_data_bme, headers=auth)
        
        
        humidity_data_bme = {'sensor_id': self.sensor_id_humidity_bme, 'value': bme_data['Humidity'], "datetime": str(datetime.now())}
        humidity_bme_r = requests.post(f'http://{self.server_ip}/reading/new', json=humidity_data_bme, headers=auth)

        if dht_data['Temperature'] is None:
            dht_data['Temperature'] = self.previous_temperature_dht
        temperature_data_dht = {'sensor_id': self.sensor_id_temperature_dht, 'value': dht_data['Temperature'], "datetime": str(datetime.now())}
        temperature_dht_r = requests.post(f'http://{self.server_ip}/reading/new', json=temperature_data_dht, headers=auth)
        self.previous_temperature_dht = dht_data['Temperature']
        
        if dht_data['Humidity'] is None:
            dht_data['Humidity'] = self.previous_humidity_dht
        humidity_data_dht = {'sensor_id': self.sensor_id_humidity_dht, 'value': dht_data['Humidity'], "datetime": str(datetime.now())}
        humidity_dht_r = requests.post(f'http://{self.server_ip}/reading/new', json=humidity_data_dht, headers=auth)
        self.previous_humidity_dht = dht_data['Humidity']
    
        pressure_data = {'sensor_id': self.sensor_id_pressure, 'value': bme_data['Pressure'], "datetime": str(datetime.now())}
        pressure_r = requests.post(f'http://{self.server_ip}/reading/new', json=pressure_data, headers=auth)
        
        with open(f'database{self.i}.csv', mode = 'a') as f:
            f.writelines(f"{bme_data['Temperature']},{dht_data['Temperature']},{bme_data['Humidity']},{dht_data['Humidity']},{bme_data['Pressure']},{datetime.now()}\n")
        return 1

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
status_ = input('Are you a new user? (y/n)')
if status_ == 'y':
    file_created = False
    j = 0
    while not file_created:
        try:
            f = open(f'database{j}.csv', 'x')
            file_created = True
        except:
            j += 1
    with open(f'database{j}.csv', mode = 'a') as f:
        f.writelines(['temperature_bme,temperature_dht,humidity_dht,humidity_dht,pressure_bme,time\n'])


    server = http(server_ip='192.168.4.137', username=input("What is the username you want to choose"), password=input("What is the password that you want to use?"), sensor_location=input("Where are the censors located at?"), i=j)
    server.register()
    server.get_token()
    print(server.create_new_sensor_all_type())
else:
    server = http(server_ip='192.168.4.137', username=input("What is your userame?"), password=input("What is your password?"), i=int(input('What is your csv file number')), sensor_id_temperature_bme = int(input('Your temperature bme sensor id:')),sensor_id_temperature_dht = int(input('Your temperture dht sensor id:')), sensor_id_humidity_bme = int(input('Your humidity bme sensor id:')), sensor_id_humidity_dht = int(input('Your humidity dht sensor id:')), sensor_id_pressure = int(input('Your pressure sensor id:')))

while True:
    server.get_token()

    print(server.update_all_censor())
    temp = read_dht11_data()
    print(temp)
    
    calibration_params = bme280.load_calibration_params(bus, address)
    data = bme280.sample(bus, address, calibration_params)
    disp.clear()
    disp.display()
    draw.rectangle((0,0,width,height), outline=0, fill=0)
    draw.text((5,0), f"Temperature:",fill=255)
    draw.text((5,15),f"{data.temperature:.2f} C", fill=255)
    draw.text((5,30),f"Humidity:",fill=255)
    draw.text((5,45),f"{data.humidity:.2f} %", fill=255)
    draw.text((90,45), f"{temp} C", fill=255)
    disp.image(image)
    disp.display()

    time.sleep(60)


values = server.get_readings()
print(f"All temperature data collected so far: \n {values}")
