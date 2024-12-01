![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
My client is a friend who wants to successfully grow a mini garden in their dorm room. However, even though they have ambient space, soil rich in nutrients, and access to sunlight and water, their plants were still not growing as much as expected. He wants to find out the environmental factor that is causing this issue. [add a few here with sources]. However, the crux of his problem is that he does not know how to deduce which factors among these are causing the plants’ issue.

My client says that it is impractical for him to record the data of his room, as he is fully focused on school work for most of the day and cannot focus on recording the data for a period of time sufficient for insights to be made.

He also said that manually collecting data and understanding the general trend is difficult, as there are times when the windows are opened, his roommate’s personal heater was on, or other irregular events that create anomalies in the data about his room, the recordings alone would not be persuasive enough to create an overview of the climate of his dorm room. Moreover, he stated that he wants data that reflects the room’s climate as close as possible, but this requires him to visualize a large amount of data and compute multiple tedious operations to find important information from this data: a task he does not have the time to do when he is busy with weekly summatives.

Additionally, as a student, he has a limited budget, and therefore wants this investigation to be as low-cost as possible, as well as taking as little time as possible, because he needs to focus on other things in his life also.

## Proposed Solution
Considering the client requirements an adequate solution includes a low cost sensing device for humidity and temperature and a custom data script that process and anaysis the samples acquired. For a low cost sensing device an adequate alternative is the DHT11 sensor[^1] which is offered online for less than 5 USD and provides adequare precision and range for the client requirements (Temperature Range: 0°C to 50°C, Humidity Range: 20% to 90%). Similar devices such as the DHT22, AHT20 or the AM2301B [^2] have higher specifications, however the DHT11 uses a simple serial communication (SPI) rather than more eleborated protocols such as the I2C used by the alternatives. For the range, precision and accuracy required in this applicaiton the DHT11 provides the best compromise. Connecting the DHT11 sensor to a computer requires a device that provides a Serial Port communication. A cheap and often used alternative for prototyping is the Arduino UNO microcontroller [^3]. "Arduino is an open-source electronics platform based on easy-to-use hardware and software"[^4]. In additon to the low cost of the Arduino (< 6USD), this devide is programable and expandable[^1]. I considered alternatives such diffeerent versions of the original Arduino but their size and price make them a less adequate solution.

Considering the budgetary constrains of the client and the hardware requirements, the software tool that I proposed for this solution is Python. Python's open-source nature and platform independence contribute to the long-term viability of the system. The use of Python simplifies potential future enhancements or modifications, allowing for seamless scalability without the need for extensive redevelopment [^5][^6]. In comparison to the alternative C or C++, which share similar features, Python is a High level programming language (HLL) with high abstraction [^7]. For example, memory management is automatic in Python whereas it is responsability of the C/C++ developer to allocate and free up memory [^7], this could result in faster applications but also memory problems. In addition a HLL language will allow me and future developers extend the solution or solve issues proptly.  


## Success Criteria
[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure values inside a dormitory for a minimum period of 48 hours. As 48 hours is 2 complete day and night cycles, this time period allows for the full recording of both the daily variations and day-to-day variations of these environmental variables.

2. The local variables will be measured using a set of 5 sensors around the dormitory. These include 2 temperature sensors, 2 humidity sensors, and 1 pressure sensor. The 2 temperature sensors and humidity sensors account for any possible variation between temperature at the two ends of the mini garden, whereas only 1 pressure sensor was used because the entire mini garden is at the same elevation. The setup ensures that a sufficient amount of data and number of variables can be recorded with the least number of sensors possible.

3. The solution provides a mathematical modelling for the Humidity, temperature and atmospheric pressure levels for each Local and Remote locations. The model allows anomalies in the data to be identified.

4. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure (HL) levels for each Local and Remote locations including mean, standard deviation, minimum, maximum, and median. This displays and visualizes the raw data in a way that is understandable to my client, who is not accustomed to computer science and handling data.

5. The Local samples are stored in a csv file and posted to the remote server as a backup. This is to ensure that during the frequent electricity outage, data will still be saved in non-volatile memory and guarantee that the data collection process happens as swiftly as possible.

6. The solution provides a prediction for the subsequent 12 hours for Humidity, temperature, and atmospheric pressure. Extrapolating the data to 12 hours beyond the recordings allows for a visualization of the overall climate of the room.

7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure. This presents both the data collected and the conclusion that came from the analysis of that data in a way that can be easily understood by my client, who is not accustomed to computer science.

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design

## System Diagram **SL**

![System Diagrams unit 2](https://github.com/user-attachments/assets/719228e9-3e4b-4e92-89a1-4a5887e0c73d)

**Fig.1** System diagram for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with the sensor DHT11 locally on an Arduino and remotely with a raspberry Pi. The latter implements an API (192.162.4.61/readings) providing access to remotely sensed data via ISAK-S network.


![System Diagrams unit 2 (1)](https://github.com/user-attachments/assets/7ec53d20-7afa-4279-8ac2-b5798e38f4db)

**Fig.2** System diagram (HL) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally. A remote server provides and API for remote monitoring and storage via the ISAK-S network. 

![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.3** Fig. 3 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

## Record of Tasks
| Task No | Planned Action                                                | Planned Outcome                                                                                                 | Time estimate | Target completion date | Criterion |
|---------|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------|------------------------|-----------|
| 1       | Write the Problem context                        | 10min         | Nov 22                 | A         |

## Test Plan

# Criteria C: Development

## List of techniques used

## Development


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
