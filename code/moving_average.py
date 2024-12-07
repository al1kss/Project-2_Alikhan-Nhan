def moving_average(data_smoothness):
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
