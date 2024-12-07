![11e470e9022f4fc5b367429bcbb285bc](https://github.com/comsci-uwc-isak/unit2_2023/assets/53995212/1d14b1d3-ae39-4ef3-8ec9-3329630eacae)

# Unit 2: A Distributed Weather Station for ISAK

## Criteria A: Planning

## Problem definition
My client is a friend who wants to successfully grow a mini basil garden in their dormitory room. However, even though they have ambient space, soil rich in nutrients, and access to sunlight and water, their plants were still not growing as much as expected. He wants to find out the factors that are causing this issue. He is confident that the soil quality and watering technique is not the issue, as he was successful in growing basil plants in other locations. 

My client then requested that we, through whichever medium, provide a report on the overall climate of the dormitory, showing him the exact issue of what is happening. He also states that it is impractical for him to manually record the data of his room’s environment, as he is fully focused on school work for most of the day and cannot focus on recording the data for a period of time sufficient for insights to be made. He also said that manually collecting data and understanding the general trend is difficult, as there are times when the windows are opened, his roommate’s personal heater was on, or other irregular events that create anomalies in the data about his room; the recordings alone would not be persuasive enough to create an overview of the climate of his dorm room. Moreover, he stated that he wants data that reflects the room’s climate as close as possible, but this requires him to visualize a large amount of data and compute multiple tedious operations to find important information from this data: a task he does not have the time to do when he is busy with weekly summatives.

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
The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure values inside a dormitory for a minimum period of 48 hours. As 48 hours is 2 complete day and night cycles, this time period allows for the full recording of both the daily variations and day-to-day variations of these environmental variables. Quote from the problem definition: “recording the data for a period of time sufficient for insights to be made, …  taking as little time as possible.”

1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure values inside a dormitory for a minimum period of 48 hours. As 48 hours is 2 complete day and night cycles, this time period allows for the full recording of both the daily variations and day-to-day variations of these environmental variables. Quote from the problem definition: “recording the data for a period of time sufficient for insights to be made, …  taking as little time as possible.”

2. The local variables will be measured using a set of 5 sensors around the dormitory. These include 2 temperature sensors, 2 humidity sensors, and 1 pressure sensor. The 2 temperature sensors and humidity sensors account for any possible variation between temperature at the two ends of the mini garden, whereas only 1 pressure sensor was used because the entire mini garden is at the same elevation. The setup ensures that a sufficient amount of data and number of variables can be recorded with the least number of sensors possible. Quote from the problem definition: “as a student, he has a limited budget, and therefore wants this investigation to be as low-cost as possible”

3. The solution provides a mathematical modelling for the Humidity, temperature and atmospheric pressure levels for each Local and Remote locations. Quote from the problem definition: “understanding the general trend”.

4. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure levels for each Local and Remote locations including mean, standard deviation, minimum, maximum, and median. This displays and visualizes the raw data in a way that is understandable to my client, who is not accustomed to computer science and handling data. Quote from the problem definition: “... provide a report on the overall climate of the dormitory.”.

5. The local samples are stored in a csv file and posted to the remote server as a backup. This is to ensure that during the frequent electricity outage, data will still be saved in non-volatile memory and guarantee that the data collection process happens as swiftly as possible. Quote from the problem definition: “.. taking as little time as possible”.

6. The solution provides a prediction for the subsequent 12 hours for Humidity, temperature, and atmospheric pressure. Extrapolating the data to 12 hours beyond the recordings allows for a visualization of the overall climate of the room. Quote from the problem definition: “The recordings alone would not be persuasive enough to create an overview of the climate of his dorm room.”

7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure. This presents both the data collected and the conclusion that came from the analysis of that data in a way that can be easily understood by my client, who is not accustomed to computer science. Quote from the problem definition: “... showing him the exact issue of what is happening.”.

TOK Connection: To what extent does the use of data science in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the reliability, interpretation, and ethical implications of data-driven approaches in addressing climate change

1. How does our use of technology shape our understanding of the environment
2. What responsibilities do we have as technologists when it comes to handling personal data related to our living spaces?
3. What cultural and contextual factors might impact our interpretation of the results, especially when comparing our local readings with those from the campus? 

# Criteria B: Design
![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.1** Fig. 1 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

## Flow Charts
![image](https://github.com/user-attachments/assets/6bf09302-87ef-4376-860f-21444b7c3b35)
**Fig.2** Fig. 2 Flow Chart for the update_all_sensors() function, this function uploads sensor data to both the server and the local CSV file.

## Record of Tasks
| Task No |                              Planned Action                             |                                    Planned Outcome                                    | Time Estimated | Target Completion Date | Criterion |
|:-------:|:-----------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|:--------------:|:----------------------:|:---------:|
| 1       | Write the Problem Definition                                            | Clearly defined the problem and identified the client and situation.                  | 15 min         | Nov 25                 | A         |
| 2       | Set up Raspberry Pi                                                     | Raspberry Pi is set up with remote access and necessary updates applied.              | 30 min         | Nov 25                 | C         |
| 3       | Finish the Success Criteria                                             | Success criteria are established for evaluating the product's effectiveness.          | 20 min         | Nov 26                 | A         |
| 4       | Test BME-280                                                            | Tested BME-280 sensor and ensured it functions correctly on a breadboard.             | 70 min         | Nov 26                 | C         |
| 5       | Test DHT-11                                                             | Tested DHT-11 sensor and verified data readings.                                      | 30 min         | Nov 27                 | C         |
| 6       | Add OLED Screen                                                         | OLED screen displays real-time sensor data.                                           | 20 min         | Nov 27                 | C         |
| 7       | Start Writing Real Code on Pi                                           | Basic function to read sensor data and store it in a dictionary completed.            | 80 min         | Nov 28                 | B, C      |
| 8       | Add More Code                                                           | Server-side functions for sensor data handling and user management implemented.       | 210 min        | Nov 29                 | C         |
| 9       | Add Code for OLED Screen                                                | Established secure communication between Raspberry Pi and OLED screen.                | 25 min         | Nov 30                 | C         |
| 10      | Establish Data Collection and File Saving using CSV                     | Integrated CSV file storage for sensor data collection.                               | 30 min         | Nov 30                 | B         |
| 11      | Modify Main Code on Raspberry Pi                                        | Debugged and optimized main code.                                                     | 40 min         | Dec 1                  | C         |
| 12      | Code Comparative Analysis Graphs of Temperature, Humidity, and Pressure | Added functionality to generate comparative graphs for the sensor data over 48 hours. | 40 min         | Dec 2                  | C         |
| 13      | Code for Graph Smoothing                                                | Refined sensor data visualization by applying smoothing techniques.                   | 20 min         | Dec 2                  | C         |
| 14      | Code 12-Hour Prediction Graph for Temperature, Humidity, and Pressure   | Developed predictive graph based on polynomial functions and past 48-hour data.       | 45 min         | Dec 4                  | C         |
| 15      | Code a Model Showing Ideal Growth Conditions for Basil                  | Added code and pie charts to analyze ideal temperature conditions for basil growth.   | 30 min         | Dec 4                  | C         |
| 16      | Work on Documentation on GitHub                                         | Documented methodology, success criteria, and explained tools and setup.              | 70 min         | Dec 5                  | A, B, C   |
| 17      | Continue Working on Criterion C                                         | Detailed tools used and added citations for research sources.                         | 40 min         | Dec 6                  | C         |
| 18      | Export CSV File and Finalize Data                                       | Exported CSV data and organized final results.                                        | 20 min         | Dec 6                  | C         |
| 19      | Continue Working on Documentation                                       | Completed the test plan, noted project limitations, and finalized documentation.      | 50 min         | Dec 6                  | B, C      |
| 20      | Create Science Poster                                                   | Developed a science poster covering introduction, methods, results, and conclusion.   | 115 min        | Dec 7                  | D         |
| 21      | Finalize Science Poster                                                 | Reviewed and refined the poster for clarity and accuracy.                             | 25 min         | Dec 8                  | D         |
| 22      | Film the Demonstration Video                                            | Created a 6-7 minute video demonstrating product functionality and code.              | 45 min         | Dec 8                  | D         |
## Test Plan

# Criteria C: Development
## Existing Tools:
| Software\ Development Tools |
|-----------------------------|
| Python                      |
| PyCharm                     |
| Raspberry Pi                |
| ISAK Weather API            |

| Libraries        |
|------------------|
| ADAfruit_SSD1306 |
| ADAfruit_DHT     |
| bme280           |
| datetime         |
| matplotlib       |
| numpy            |
| time             |
| PIL              |

## List of techniques used
1. Classes (Classes allow easy implementation of API requests for both new and existing users by creating different instances)
2. Functions (Functions allow higher code-readability and allows for the reuse of code)
3. Moving Average (To smooth the data and provides a more dataset more reflective of the environment)
4. Polynomial Fit (To provide deeper understand of the data and allows for prediction based on the sensors' data)
5. Writing Files Using Python (To keep track of the sensor's data and add redundancy to ensure the swiftness of the data-recording process)
6. HTTP Requests (To keep track of the sensor's data and add redundancy to ensure the swiftness of the data-recording process)
   
## Development
### Uploading Data to Server (Success Criteria 5)
```.py
# The 3 lines of code below is to check whether or not the user is new
status = ''
while status != 'y' and status != 'n':
    status = input('Are you a new user? (enter only y or n)')

# If the user is new
if status == 'y':
    file_created = False
    j = 0
    while not file_created: #while the file is not created
        try: # Try creating the database file numbered j
            f = open(f'database{j}.csv', mode = 'x')
            file_created = True
        except: #  Add 1 to the CSV number if it already exists
            j += 1
    with open(f'database{j}', mode = 'a') as f: # add headers to the new csv file
        f.writelines(['temperature_bme, temperature_dht, humidity_bme, humidity_dht, pressure_bme, time\n'])

    # create an instance of an object that we created that can send requests to ISAK Weather API
    server = http(server_ip = '192.168.4.137', username = input("What is the username you want to choose?"), password = input("What is the password that you want to use?"), sensor_location = input("Where are the censors located at?"), i = j)
    server.register() # this method registers the user

    server.get_token() # this method retrieves an authorization token from the API server
    print(server.create_new_sensor_all_type()) # create new sensors using the username provided and token generated
else:
    # create an instance of an object that we created that can send requests to ISAK Weather API using the existing user's credential
    server = http(server_ip = '192.168.4.137', username = input("What is your username?"), password = input("What is your password?"), i = input('What is your CSV file number?'))

while True:
    # in an infinite loop
    server.get_token() # this method retrieves an authorization token from the API server
    print(server.update_all_censor()) # this method sends a post request to the server to update the sensor's data both on the server and CSV backup

    time.sleep(60) # stop the program for 60 seconds
```
To fulfill criterion 5 and ensure that the data collection process goes as smoothly as possible, the code block above was needed. It describes the main code of our data collection code. It consists of an if statement that checks if the user is a new or returning and do exectutes the corresponding initial block of code. If the user is new, it creates a new CSV file to write the data, then it asks for a `username`, `password`, `sensor_location`, and use the CSV file number `j` as input to the instance variable `i` and creates an instance of the object `http`. `http` is an object we created to send various API requests to the ISAK weather API server.
    
Otherwise, if the user is not new, it will ask for a `username`, `password`, that user's sensor ID, and use CSV file number `j` as input to the instance variable `i` to create an instance of the class `http`.
    
Once the setup if statement finishes, a `while True:` loops repeats every 60 seconds (using the 'time' module). In one cycle, the code will use the `get_token()` method to get the authorization key, then the `update_all_sensors()`, which flow chart is described in section B, will use the key to upload the sensor recordings to the server and add it to the CSV. The while True loop here is justified because the loop continuing for more than 48 hours does not affect the results, and adding additional comparison into the while statement would take unecessary computation and more possible points of failure.
    
This code allows the swift resumption of recording if there is an error with the server or the sensors disconnecting, thereby allowing the recording process to take as less time as possible. Addtionally, it also adds redundancy to the data by both saving it locally in a CSV and the ISAK Weather API.
    
### Polynomial Prediction Generator (Success Criterion 3 & 6)
```.py
def gen_polynomial_graph(x: list, y: list, deg: int, window_size: int) -> tuple:
    """
    :param x: the list of x-values
    :param y: the list of y-values
    :param deg: the degree of the polynomial generated
    :param window_size: the size of the window for the moving average
    :return x_graph, y_graph: a tuple that has a list of the x-values of the generated polynomial in the first index and y-values of the generated polynomial in the second index
    """
    y_smoothed = [] #list to store results

    # the following loop repeats until it is not possible to create windows of size window_size
    for i in range(0, len(y) - window_size + 1):
        y_section = y[i:i + window_size] # Create a list with value of y at index i up until i + window_size, this list has length of window_size.
        y_section_average = sum(y_section) / window_size # Calculate the average value of the elements in the list, the window's average
        y_smoothed.append(y_section_average) # Append the calculated average to the smoothened results

    # the following loop starts from the index next to the index that the previous ended on until the last value of the list
    for i in range(len(y) - window_size + 1, len(y)):
        y_section = y[i:] # Create a list with value of y at index i up until the last element of y, this is also the biggest window possible for that index
        y_section_average = sum(y_section) / len(y_section) # Calculate the average value of the elements in the list, the window's average and
        y_smoothed.append(y_section_average) # Append the calculated average to the smoothened results

    coefficients = np.polyfit(x, y_smoothed, deg) # Generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients)  # Create an object that acts like a polynomial

    # Generate the x-values of the polynomial graph
    x_graph = np.linspace(min(x), max(x), num=len(x)) # by creating a list that has len(x) of evenly spaced values between the x-values starting point (lowest value) and the x-value stopping point (highest value)

    # Generate the y-values of the polynomial graph 
    y_graph = polynomial(x_graph) # by creating a list that has values which are the value of the elements of x_graph inputted into the polynomial

    return x_graph, y_graph # Return the x-values and y-values of the polynomial's graph
```
  As the data is collected, rather than mathematically generated, the team's predetermining whether to use a linear, quadratic, cubic, or polynomial of a specific n-degree would not be scientifically reasonable, as we will therefore be presuming the overall trend of the data. Therefore, multiple types of predictions need to be generated to determine the most suitable. The code block above is a function that returns the x and y values of the graph of a prediction polynomial fit of degree-deg, where deg is a function input. 
  
  Its first step is to smooth the raw data. This step is needed because the data is recorded every minute, not continuous, potentially exaggerating the variation between recordings, making the final polynomial prediction's not as predictable and accurate. Furthermore, as both the DHT11 and BME sensors are relatively cheap and prone to inaccurate readings, this step is necessary.

  Calculating the smoothed raw data has two phases, represented by two for loops. The first loop iterates through the list, each time calculating the average of a window, a list that is a part taken from the raw data list that has size of window-size and starts at the current index the loop is at, then appends the value into a list. This process will stop when the current index the loop is at is too high to create a window of size window-size. Once this happens, the loop exits and the next loop starts at the next index; this loop instead calculates the average of a window that starts from the index the loop is at and ends at the highest possible index of the list and appends it to the results. It does not take data from the previous indices because the average would then be repeated.
  
  The second step is to use the numpy library to, from the smoothed data, generate the coefficients of the polynomial fit of degree deg, then use these coefficients in the poly1d method to create an object that can return the value of that polynomial given an input, which is also the x-value of the graph. Once that is established, a list of inputs for the polynomial function is generated by the linspace method; then the function uses each of these inputs into the polynomial object and append the results into a list that will be used as the y-values for the polynomial graph. Finally, the function returns the lists of x-values and y-values as a tuple.

  The key feature of this function is that it allows the generation of polynomial fit of any degree. This allows for rapid testing of multiple types of polynomial fit to determine the most suitable. It was significant in fulfilling success criteria 3 and 6.


# Criteria D: Functionality

A 7 min video demonstrating the proposed solution with narration
