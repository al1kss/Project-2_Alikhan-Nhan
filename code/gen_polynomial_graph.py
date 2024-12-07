def gen_polynomial_graph(x: list, y: list, deg: int, data_smoothness: int) -> tuple:
    y_smoothed = []
    for i in range(data_smoothness // 2):
        y_section = y[:i + 1]
        y_section_average = sum(y_section) / len(y_section)
        y_smoothed.append(y_section_average)

    for i in range(data_smoothness // 2, len(y) - data_smoothness//2):
        y_section = y[i:i + data_smoothness]
        y_section_average = sum(y_section) / data_smoothness
        y_smoothed.append(y_section_average)

    end_section_start = len(y) - data_smoothness // 2 - 1 if data_smoothness % 2 != 0 else len(y) - data_smoothness // 2
    for i in range(end_section_start, len(y)):
        y_section = y[i:]
        y_section_average = sum(y_section) / len(y_section)
        y_smoothed.append(y_section_average)

    coefficients = np.polyfit(x, y_smoothed, deg) #generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients)

    x_graph = np.linspace(min(x), max(x))
    y_graph = polynomial(x_graph)

    return x_graph, y_graph
