def moving_average(data_smoothness):
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
