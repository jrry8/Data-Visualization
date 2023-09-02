import csv
from matplotlib import pyplot as plt
from datetime import datetime

#filename = 'sitka_weather_2014.csv'
filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    highs, lows, dates = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], '%Y-%m-%d')
            cur_high = int(row[1])
            cur_low = int(row[3])
        except ValueError:
            print(current_date, "missing data")
        else:
            highs.append(cur_high)
            lows.append(cur_low)
            dates.append(current_date)
    #print(highs)

# plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title('Daily High and Low Temperatures - 2014', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()