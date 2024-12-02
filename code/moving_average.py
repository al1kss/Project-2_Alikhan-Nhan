def moving_average(windowSize: int, x: list) -> list:
    x_smoothed = []
    for i in range(0, len(x)-1-windowSize):
        x_section = x[i:i+windowSize]
        x_average = sum(x_section) / windowSize
        x_smoothed.append(x_average)
    return x_smoothed
