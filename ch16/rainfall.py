import csv
from matplotlib import pyplot as plt
from datetime import datetime

# Get dates and rainfall from file.
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    dates = []
    rainfall = []
    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            rain = float(row[19])
        except ValueError:
            print(current_date, 'missing_data')
        else:
            dates.append(current_date)
            rainfall.append(rain)

# Plot data.
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, rainfall, c='blue', alpha=0.5)

# Format plot.
title = "Daily rainfall - 2014\nSitka"
plt.title(title, fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Rain (in)", fontsize=16)
plt.ylim((0,5))
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()