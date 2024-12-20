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

Moreover, please check appendix A for evidence of client consultation.


## Success Criteria
[^1]: Industries, Adafruit. “DHT11 Basic Temperature-Humidity Sensor + Extras.” Adafruit Industries Blog RSS, https://www.adafruit.com/product/386. 
[^2]: Nelson, Carter. “Modern Replacements for DHT11 and dht22 Sensors.” Adafruit Learning System, https://learn.adafruit.com/modern-replacements-for-dht11-dht22-sensors/what-are-better-alternatives.   
[^3]:“How to Connect dht11 Sensor with Arduino Uno.” Arduino Project Hub, https://create.arduino.cc/projecthub/pibots555/how-to-connect-dht11-sensor-with-arduino-uno-f4d239.  
[^4]:Team, The Arduino. “What Is Arduino?: Arduino Documentation.” Arduino Documentation | Arduino Documentation, https://docs.arduino.cc/learn/starting-guide/whats-arduino.  
[^5]:Tino. “Tino/PyFirmata: Python Interface for the Firmata (Http://Firmata.org/) Protocol. It Is Compliant with Firmata 2.1. Any Help with Updating to 2.2 Is Welcome. the Capability Query Is Implemented, but the Pin State Query Feature Not Yet.” GitHub, https://github.com/tino/pyFirmata. 
[^6]:Python Geeks. “Advantages of Python: Disadvantages of Python.” Python Geeks, 26 June 2021, https://pythongeeks.org/advantages-disadvantages-of-python/. 
[^7]: Real Python. “Python vs C++: Selecting the Right Tool for the Job.” Real Python, Real Python, 19 June 2021, https://realpython.com/python-vs-cpp/#memory-management. 
The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure values inside a dormitory for a minimum period of 48 hours. As 48 hours is 2 complete day and night cycles, this time period allows for the full recording of both the daily variations and day-to-day variations of these environmental variables. Problem tackled: “recording the data for a period of time sufficient for insights to be made, …  taking as little time as possible.”
[^8]: MatplotLib.org. "subplots - documentation", https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.subplots.html

1. The solution provides a visual representation of the Humidity, Temperature and atmospheric pressure values inside a dormitory for a minimum period of 48 hours. As 48 hours is 2 complete day and night cycles, this time period allows for the full recording of both the daily variations and day-to-day variations of these environmental variables. Problem tackled: “recording the data for a period of time sufficient for insights to be made, …  taking as little time as possible.”

2. The local variables will be measured using a set of 5 sensors around the dormitory. These include 2 temperature sensors, 2 humidity sensors, and 1 pressure sensor. The 2 temperature sensors and humidity sensors account for any possible variation between temperature at the two ends of the mini garden, whereas only 1 pressure sensor was used because the entire mini garden is at the same elevation. The setup ensures that a sufficient amount of data and number of variables can be recorded with the least number of sensors possible. Problem tackled: “as a student, he has a limited budget, and therefore wants this investigation to be as low-cost as possible”

3. The solution provides a mathematical modelling for the Humidity, temperature and atmospheric pressure levels for each Local and Remote locations. Problem tackled: “understanding the general trend”.

4. The solution provides a comparative analysis for the Humidity, Temperature and atmospheric pressure levels for each Local and Remote locations including mean, standard deviation, minimum, maximum, and median. This displays and visualizes the raw data in a way that is understandable to my client, who is not accustomed to computer science and handling data. Problem tackled: “... provide a report on the overall climate of the dormitory.”.

5. The local samples are stored in a csv file and posted to the remote server as a backup. This is to ensure that during the frequent electricity outage, data will still be saved in non-volatile memory and guarantee that the data collection process happens as swiftly as possible. Problem tackled: “... taking as little time as possible”.

6. The solution provides a prediction for the subsequent 12 hours for Humidity, temperature, and atmospheric pressure. Extrapolating the data to 12 hours beyond the recordings allows for a visualization of the overall climate of the room. Problem tackled: “The recordings alone would not be persuasive enough to create an overview of the climate of his dorm room.”

7. The solution includes a poster summarizing the visual representations, model and analysis created. The poster includes a recommendation about healthy levels for Humidity, Temperature and atmospheric pressure. This presents both the data collected and the conclusion that came from the analysis of that data in a way that can be easily understood by my client, who is not accustomed to computer science. Problem tackled: “... showing him the exact issue of what is happening.”.

TOK Connection: To what extent does the use of data science in climate research influence our understanding of environmental issues, and what knowledge questions arise regarding the reliability, interpretation, and ethical implications of data-driven approaches in addressing climate change

1. Technology and Environmental Understanding
   
The sensors allowed the research group to gather an enormous amount of data that would be extremely tedious to manually collect to great accuracy. A limitation is that sometimes errors can occur, and the only way to identify this error is to add a reference, such as an additional sensor. Even then, there is a chance that both sensors are incorrect, then it would be up to the human analysis to provide an accurate understanding from the data. A prime example of this is our DHT11 returning 138% humidity and only returning natural numbers instead of floats.

3. Responsibilities in Handling Personal Data
   
Personal data needs consent to be shared and handled. However, an important property of digital data is that it can be easily duplicated when shared. Therefore, as we have ethics, it is our responsibility to ensure the safety of the data recorded to honor the consent of the person being recorded.

5. Cultural and Contextual Factors in Data Interpretation
   
Cultural and contextual factors greatly influence our interpretation of sensor data. A data recording can be deemed in analysis as an anomoly and wrong recording based on the analyzer's perspective. If one has the prior knowledge and expectation about the data, they might subconsciously have a favor towards certain data values, therefore creating a dataset or conclusion that vastly differs from the truth.
# Criteria B: Design
![System Diagrams unit 2 (2)](https://github.com/user-attachments/assets/36775cba-6730-45d3-bccb-57b4d8a8179d)

**Fig.1** Fig. 1 System diagram (HL+) for the proposed system to visualize and analyze temperature and humidity data in our campus. Physical variables measured with a network of DHT11/BMP280 sensors locally on a Raspberry Pi. A remote server provides and API for remote monitoring and storage (192.162.6.142) via the ISAK-S network. A laptop for remote work is included.

## Flow Charts
![CompScience FlowDiagrams - Page 1 (2)](https://github.com/user-attachments/assets/45eba9f6-f9a7-4c86-9985-5d227e15d1ee)
**Fig.2** Fig. 2 Flow Chart for the update_all_sensors() function, this function uploads sensor data to both the server and the local CSV file.

![CompScience FlowDiagrams - Page 1 (1)](https://github.com/user-attachments/assets/766320c2-015d-4ce9-bc76-b26a7d86cbcd)

**Fig.3** Fig. 3 Flow Chart for the prediction.py, this code makes the prediction of the temperature, humidity, and pressure for the 12 hours based on the analysis of the 48-hour data. 

![CompScience FlowDiagrams - Page 1](https://github.com/user-attachments/assets/ab04dbe6-d416-46f5-b406-15791124001b)
**Fig.4** Fig. 4 Flow Chart for the ideal_temperature.py, this code shows the perfect temperature for basil's growth



## Record of Tasks
| Task No |                                               Planned Action                                              |                                     Planned Outcome                                    | Time Estimated | Target Completion Date | Criterion |
|:-------:|:---------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|:--------------:|:----------------------:|:---------:|
|    1    |                                        Write the Problem Definition                                       |          Clearly defined the problem and identified the client and situation.          |     15 min     |         Nov 25         |     A     |
|    2    |                                            Set up Raspberry Pi                                            |        Raspberry Pi is set up with remote access and necessary updates applied.        |     30 min     |         Nov 25         |     C     |
|    3    |          Establish the clearly defined Success Criteria, with precise and comprehensible criteria         |      Success criteria are established for evaluating the product's effectiveness.      |     20 min     |         Nov 26         |     A     |
|    4    |   Test BME-280 sensor to make sure it works. Install all required libraries, work with the documentation  |        Tested BME-280 sensor and ensured it functions correctly on a breadboard.       |     70 min     |         Nov 26         |     C     |
|    5    |   Test DHT-11 sensor to make sure it works. Install all required libraries, work with the documentation   |                    Tested DHT-11 sensor and verified data readings.                    |     30 min     |         Nov 27         |     C     |
|    6    |                             Start Writing Code on Pi to work with the Sensors                             |       Basic function to read sensor data and store it in a dictionary completed.       |     80 min     |         Nov 28         |    B, C   |
|    7    |                    Add Code on Pi to interact with the server, receive, send, save data                   |     Server-side functions for sensor data handling and user management implemented.    |     210 min    |         Nov 29         |     C     |
|    8    |                            Establish Data Collection and File Saving using CSV                            |                 Integrated CSV file storage for sensor data collection.                |     30 min     |         Nov 30         |     B     |
|    9    |       Work on the code on Raspberry Pi, remove all glitches and the bugs with further optimization        |                            Debugged and optimized main code.                           |     40 min     |          Dec 1         |     C     |
|    10   | Code Comparative Analysis Graphs of Temperature, Humidity, and Pressure for data gathered during 48 hours |  Added functionality to generate comparative graphs for the sensor data over 48 hours. |     40 min     |          Dec 2         |     C     |
|    11   |                 Coded a function for precise Graph Smoothing that will work with any graph                |           Refined sensor data visualization by applying smoothing techniques.          |     20 min     |          Dec 2         |     C     |
|    12   |                Developed a 12-Hour Prediction Graph for Temperature, Humidity, and Pressure               |     Developed predictive graph based on polynomial functions and past 48-hour data.    |     55 min     |          Dec 4         |     C     |
|    13   |                        Developed a Model Showing Ideal Growth Conditions for Basil                        |   Added code and pie charts to analyze ideal temperature conditions for basil growth.  |     30 min     |          Dec 4         |     C     |
|    14   |      Explained tools used and recording setup   |        Explained tools and setup for both the poster and GitHub documentation       |     70 min     |          Dec 5         |  A, B, C  |
|    15   |                                            Work on Criterion C                                            |              Detailed tools used and added citations for research sources.             |     40 min     |          Dec 6         |     C     |
|    16   |                          Export CSV File from the Raspberry Pi and Finalize Data                          |                     Exported CSV data and organized final results.                     |     20 min     |          Dec 6         |     C     |
|    17   |             Continue Working on Criterion B and C, finish test plan and project limitations               |    Completed the test plan, noted project limitations, and finalized documentation.    |     50 min     |          Dec 6         |    B, C   |
|    18   |                       Create 3 Flow Diagrams for the easier understanding client                          | Included the graphical representation of a program developed for the proposed solution |     45 min     |          Dec 7         |     B     |
|    19   |                                       Create scientific poster                                               |   Developed a science poster covering introduction, methods, results, and conclusion.  |     115 min    |          Dec 7         |     D     |
|    20   |                 Format the poster properly using LaTeX                                                    |                The poster is clear and finished                                        |     25 min     |          Dec 8         |     D     |
|    21   |                                        Film the Demonstration Video                                       |        Created a 6-7 minute video demonstrating product functionality and how we have fulfilled the success criteria        |     45 min     |          Dec 8         |     D     |
|    22   |                          Upload the poster and video onto GitHub                       |       Added a link to the Science Poster      |     25 min     |          Dec 8         |     D     |
## Test Plan
<img width="1338" alt="image" src="https://github.com/user-attachments/assets/49f252c4-23fa-4d98-8690-06239364a358">

# Criteria C: Development

## List of techniques used
1. Object-Oriented Programming (OOP) (OOP allows for the creation of classes and instances, making it easier to manage API requests for both new and existing users by encapsulating related data and behaviors)
2. Functions (Functions allow higher code-readability and allows for the reuse of code)
3. Moving Average (To smooth the data and provides a more dataset more reflective of the environment)
4. Polynomial Fit (To provide deeper understand of the data and allows for prediction based on the sensors' data)
5. Writing Files Using Python (To keep track of the sensor's data and add redundancy to ensure the swiftness of the data-recording process)
6. HTTP Requests (To keep track of the sensor's data and add redundancy to ensure the swiftness of the data-recording process)
   
# Development
## Using a Class to Upload Data to Server (Success Criteria 5)
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

    # create an instance of an object that we created that can send requests to the Weather API
    server = http(server_ip = '192.168.4.137', username = input("What is the username you want to choose?"), password = input("What is the password that you want to use?"), sensor_location = input("Where are the censors located at?"), i = j)
    server.register() # this method registers the user

    server.get_token() # this method retrieves an authorization token from the API server
    print(server.create_new_sensor_all_type()) # create new sensors using the username provided and token generated
else:
    # create an instance of an object that we created that can send requests to the Weather API using the existing user's credential
    server = http(server_ip = '192.168.4.137', username = input("What is your username?"), password = input("What is your password?"), i = input('What is your CSV file number?'))

while True:
    # in an infinite loop
    server.get_token() # this method retrieves an authorization token from the API server
    print(server.update_all_censor()) # this method sends a post request to the server to update the sensor's data both on the server and CSV backup

    time.sleep(60) # stop the program for 60 seconds
```
The code above was used to fulfill criterion 5, saving the data recorded in a CSV and uploading it to a remote server using an API. The class `http` was used because it allowed for more readable code and code that is easier to debug. To upload the data, we needed to make multiple types of API calls to the server, and these API calls share information with each other, such as the username and password to the API, but some also retrieve information that will be used for other API calls, such as the API call that generates an authorization token which is then used by the API call that uploads the data to the server. Encapsulating these API calls into a class allowed for a way to share a set of data across these API call functions in a predictable manner, unlike using global variables, or sometimes function inputs. 

Moreover, as our code has different API calls for new user and old users, such as the new user needing to create a new sensor on the server using the `create_new_sensor_all_type()` method but also API calls that are shared between the two types of users, such as getting the token from the server. Therefore, using a unified `http` class that allows for different instance variables allows us to maximize the usability of code while allowing the implementation to be as easy as possible, meaning that we do not have to write these API calls as independent functions and correctly modify function inputs every time that we need to modify the code.

In essence, this technique, object oriented programming, allowed us to minimize the time that we take to program and record data, as the code has predictable behaviour and is clearer to debug, as we only have to worry about the process within the API calls functions themselves, rather than the variables inputted into these calls.

    
## Polynomial Prediction Generator (Success Criterion 3 & 6)
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


## The Comparative analysis for all sensors (Success Criteria 4)
We included several graphs so our client could analyze and implement the data more easily. They are: 
* A standard graph
* Combined graph which shows the mean of the sensors
* The graph with the deviation
All of these graphs will have the maximum, and minimum points and show the median.

In order not to confuse the client, a set of standard colors was used throughout the project. BME sensor has an `#E35205`<sub>orange </sub> and DHT sensor being `#005C97`<sub>blue </sub>, but for the pressure values the color `#7a479b`<sub>purple</sub>

### For the Standard Graph

The process begins by initializing the `subplot()` function, which allows multiple plots to be drawn within a single figure. In this case, the figure is configured with **3 rows** and **1 column**. The `sharex=True` argument ensures that the x-axis properties are shared across all subplots. When subplots share the x-axis within a column, only the bottom subplot displays the x-tick labels. This approach helps conserve space and improves the readability of the graphs. The variable `axs` represents an array of Axes objects, facilitating easy access to individual subplots [^8].

```.py
fig, axs = plt.subplots(3, 1, figsize=(10, 9), sharex=True)

axs[0].plot(timestamps[:len(temp_values_dht)], temp_values_dht, marker="x", linestyle="-", color="b",
            linewidth=0.8, markersize=4, label="DHT Temp")
axs[0].plot(timestamps, temp_values_bme, marker="o", linestyle="-", color="orange",
            linewidth=0.8, markersize=4, label="BME Temp")

axs[0].set_title("Temperature Readings")
axs[0].set_ylabel("Temperature (°C)")
axs[0].legend()
```

The `axs[0]` object accesses the first row of the subplot. First, the temperature values from the DHT sensor are plotted. The `timestamps` list serves as the x-axis data. The slicing operation `timestamps[:len(temp_values_dht)]` ensures that the `timestamps` list and `temp_values_dht` list are of the same length, as the DHT sensor occasionally returns `None` values. The slicing notation `:` indicates "from the start of the list up to, but not including, the specified index."
Next, the temperature values from the BME sensor are plotted. Unlike the DHT sensor, the BME sensor reliably records data, so the entire `timestamps` list is used without slicing.
The plot is customized with a title, a y-axis label, and a legend for clarity.
The same approach is used for plotting humidity and pressure sensor data.

![main_graph](https://github.com/user-attachments/assets/64f90b4c-6409-4517-8bff-595c8d643ea2)
**Fig.5** Fig. 5 This graph shows the temperature, humidity, and pressure for the data gathered in 48-hours. It includes max, min, median, model values 

### For the mean graph

The code for generating a combined graph of both sensors is similar to the previous example, with only a few differences. Specifically, the key difference lies in the calculation of the average values.
The `average_temp` and `average_hum` variables store the averaged temperature and humidity values, respectively. These variables are lists where each element represents the mean of corresponding measurements from the BME and DHT sensors. The averages are computed by summing the values from both sensors at each index and dividing by two:
```.py
average_temp = [(temp_values_bme[i] + temp_values_dht[i]) / 2.0 for i in range(len(temp_values_bme))]
average_hum = [(hum_values_bme[i] + hum_values_dht[i]) / 2.0 for i in range(len(hum_values_bme))]
```
Once the averages are calculated, the data can be plotted using the `timestamps` list for the x-axis and `average_temp` for the y-axis.

![mean_max_min_med](https://github.com/user-attachments/assets/dee084eb-9e7d-4c55-926c-9b77d7c8afb1)
**Fig.6** Fig. 6 This graph shows the temperature, and humidity for the data gathered in 48 hours. It includes max, min, median values

#### For the graph with the deviation

The code for generating a graph that includes deviations for both sensors is similar to the previous example, with a few key differences. To calculate the standard deviation, the `numpy` module is utilized. The `.std()` function returns a measure of the spread of the data distribution.

```.py
temp_dev_bme = np.std(temp_values_bme)
temp_dev_dht = np.std(temp_values_dht)
hum_dev_bme = np.std(hum_values_bme)
hum_dev_dht = np.std(hum_values_dht)
pres_dev = np.std(pres_values)
```

To visualize the deviations, we modify the plot by adding shaded regions to represent the range of deviation. This is achieved using the `fill_between` function, which creates a band around each sensor's data by subtracting and adding the standard deviation to each value. The `alpha` parameter controls the opacity of the shading.

```.py
axs[0].fill_between(
    timestamps, # X-axis values: list of timestamps for each temperature reading

    # Lower boundary: subtract the deviation from each temperature value
    [val - temp_dev_dht for val in temp_values_dht], # Creates a list of (temperature - deviation) values

    # Upper boundary: add the deviation to each temperature value
    [val + temp_dev_dht for val in temp_values_dht], # Creates a list of (temperature + deviation) values
    color="b", alpha=0.3, label="DHT Deviation" # Transparency level of the fill (30% opacity), color blue
)
axs[0].fill_between(
    timestamps,
    [val - temp_dev_bme for val in temp_values_bme],
    [val + temp_dev_bme for val in temp_values_bme],
    color="orange", alpha=0.3, label="BME Deviation"
)
```

This approach calculates lower and upper bounds for each sensor's measurements by subtracting or adding the standard deviation to each value in the `temp_values_dht` and `temp_values_bme` lists. The same technique can be applied to visualize deviations for humidity and pressure data.

![deviation graph](https://github.com/user-attachments/assets/4fb7906b-10fd-4ce6-9b13-7878fd4962a8)
**Fig.7** Fig. 7 This graph shows the temperature, humidity, and pressure deviation for the data gathered in 48 hours 

![close_up_deviation](https://github.com/user-attachments/assets/e831e4e1-a8a9-4873-a633-78e0d2360557)
**Fig.8** Fig. 8 This graph shows the temperature, humidity, and pressure deviation for the data gathered in 16 hours 


# Criteria D: Functionality

## Poster
![image](https://github.com/user-attachments/assets/d77c629a-8b87-43f2-9fb6-c0a505614956)
**Fig. 9** Fig. 9, Science Poster
[Please Click Here for the PDF](https://github.com/user-attachments/files/18052862/rfghjiko.1.pdf)


A 7 min video demonstrating the proposed solution with narration
[Google Drive](https://drive.google.com/drive/folders/15jsoM78kbg8LWp9bR0qrfyJYnjGiTti5?usp=sharing)

# Appendix A: Evidence of Client Consultation

<img width="926" alt="image" src="https://github.com/user-attachments/assets/63cac082-3b9a-47bb-ace1-2b7bcc65e624">
- The Client's Initial Problem Definition


![image](https://github.com/user-attachments/assets/e09f04a7-a953-4a95-b3ee-070892b6f03b)
- Us sending the success criteria to the client
  
<img width="887" alt="image" src="https://github.com/user-attachments/assets/3ab5c827-efc9-4892-87a4-9f4ff4ba304b">
- The Client's Accepting the Solution and Success Criteria


