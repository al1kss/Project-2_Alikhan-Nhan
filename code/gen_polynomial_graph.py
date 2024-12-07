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
        # Create a list with value of y at index i up until i + window_size, this list has length of window_size.
        y_section = y[i:i + window_size]
        # Calculate the average value of the elements in the list, the window's average.
        y_section_average = sum(y_section) / window_size
        # Append the calculated average to the smoothen results
        y_smoothed.append(y_section_average)

    # the following loop starts from the index next to the index that the previous ended on until the last value of the list
    for i in range(len(y) - window_size + 1, len(y)):
        # Create a list with value of y at index i up until the last element of y, this is also the biggest window possible for that index
        y_section = y[i:]
        # Calculate the average value of the elements in the list, the window's average.
        y_section_average = sum(y_section) / len(y_section)
        # Append the calculated average to the smoothen results
        y_smoothed.append(y_section_average)

    coefficients = np.polyfit(x, y_smoothed, deg) # Generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients)  # Create an object that acts like a polynomial

    # Generate the x-values of the polynomial graph
    # by creating a list that has len(x) of evenly spaced values between the x-values starting point (lowest value) and the x-value stopping point (highest value)
    x_graph = np.linspace(min(x), max(x), num=len(x))
    
    # Generate the y-values of the polynomial graph
    # by creating a list that has values which are the value of the elements of x_graph inputted into the polynomial
    y_graph = polynomial(x_graph)

    return x_graph, y_graph # Return the x-values and y-values of the polynomial's graph
