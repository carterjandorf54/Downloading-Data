from pathlib import Path
import csv
from datetime import datetime

import matplotlib.pyplot as plt

# Create absolute path to the CSV file, preface the path with r so no encoding issue with \U
absolute_path = r"C:\Users\carte\OneDrive\Desktop\Python\Downloading Data\weather_data\sitka_weather_07-2021_simple.csv"
longer_time_period = r"C:\Users\carte\OneDrive\Desktop\Python\Downloading Data\weather_data\sitka_weather_2021_simple.csv"
los_angeles = r"C:\Users\carte\OneDrive\Desktop\Python\Downloading Data\weather_data\3348168.csv"
path = Path(los_angeles)
lines = path.read_text().splitlines()

# next() call returns the next line of a file (Only call this once to get the header row)
# reader object to parse each line in the file / Stores each comma separated value in a list
reader = csv.reader(lines)
header_row = next(reader)

# Enumerate function returns both the index of each item and the value of each item as you loop through a list
for index, column_header in enumerate(header_row):
    print(index, column_header)

# Extract High Temperatures
dates, highs, lows = [], [], []
for row in reader:
    # High Temp is stored in index 4 / Low Temp is stored in index 5 / Date is stored in index 2
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[6])
        low = int(row[7])
    except ValueError:
        print(f"Missing data for {current_date}")
    else:
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# Plot the high temperatures.
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.1)

# Format plot
ax.set_title(f"Daily High & Low Temps 2021", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(labelsize=16)

plt.show()