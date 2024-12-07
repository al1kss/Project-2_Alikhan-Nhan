def gen_polynomial_graph(x: list, y: list, deg: int, data_smoothness: int) -> tuple:
    y_smoothed = []
    for i in range(0, len(y) - data_smoothness):
        y_section = y[i:i + data_smoothness]
        y_section_average = sum(y_section) / data_smoothness
        y_smoothed.append(y_section_average)

    end_section_start = len(y) - data_smoothness - 1 if data_smoothness % 2 != 0 else len(y) - data_smoothness
    for i in range(end_section_start, len(y)):
        y_section = y[i:]
        y_section_average = sum(y_section) / len(y_section)
        y_smoothed.append(y_section_average)

    coefficients = np.polyfit(x, y_smoothed, deg) #generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients)

    x_graph = np.linspace(min(x), max(x))
    y_graph = polynomial(x_graph)

    return x_graph, y_graph
