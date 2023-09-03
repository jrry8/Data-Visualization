import csv
from matplotlib import pyplot as plt
from datetime import datetime

while (True):
    print('This dataset contains monthly weather data for SeaTac from 1948 to 2023.')
    year = int(input('Which year would you like to see? '))
    if 1948 <= year <= 2023:
        break
    print('Please input a valid year.')

filename = 'seatac_monthly.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    date_idx = header_row.index('DATE')
    # also consider TMAX and TMIN
    min_temp_idx = header_row.index('EMNT')     # lowest temp per month
    max_temp_idx = header_row.index('EMXT')     # highest temp per month

    highs, lows, dates = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[date_idx], '%Y-%m')
        if current_date.year != year:
            continue
        try:
            cur_high = float(row[max_temp_idx])
            cur_low = float(row[min_temp_idx])
        except ValueError:
            print(current_date, "missing data")
        else:
            highs.append(cur_high)
            lows.append(cur_low)
            dates.append(current_date)

# plot data
fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title('SeaTac Monthly High and Low Temperatures', fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()