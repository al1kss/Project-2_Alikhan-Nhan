def gen_polynomial_graph(x: list, y: list, deg: int, data_smoothness: int) -> tuple:
    y_smoothed = [] #array to store results
    for i in range(0, len(y) - data_smoothness + 1): # repeat until it is not possible to create
        # Create an array with value of y at index i up until i + data_smoothness, this array has length of data_smoothness.
        y_section = y[i:i + data_smoothness]
        # Calculate the average value of the array, the window's average.
        y_section_average = sum(y_section) / data_smoothness
        # Append the calculated average to the smoothen results
        y_smoothed.append(y_section_average)

    for i in range(len(y) - data_smoothness + 1, len(y)):
        y_section = y[i:]
        y_section_average = sum(y_section) / len(y_section)
        y_smoothed.append(y_section_average)

    coefficients = np.polyfit(x, y_smoothed, deg) #generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients)

    x_graph = np.linspace(min(x), max(x))
    y_graph = polynomial(x_graph)

    return x_graph, y_graph
