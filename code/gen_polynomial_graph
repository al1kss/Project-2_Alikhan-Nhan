def gen_polynomial_graph(x: list, y: list, deg: int, smoothness: int):
    coefficients = np.polyfit(x, y, deg) #generate polynomial approximation's coefficient
    polynomial = np.poly1d(coefficients) #generate polynomial as an object
    x_graph = np.linspace(min(x), max(x))
    y_graph = polynomial(x_graph)
    return x_graph, y_graph
