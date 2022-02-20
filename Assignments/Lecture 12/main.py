import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Question 1 #
from Tools.scripts.dutree import display

df = pd.read_csv('bikes.csv')


def calculate_profit(x):
    casual_customers = x['Casual']
    registered_customers = x['Registered']
    casual_price_per_hour = 20
    taxes = 0.14
    maintenance_per_year = 1500 / (12 * 30 * 24)
    profit = taxes * (casual_customers * (casual_price_per_hour + maintenance_per_year) + registered_customers *
                      (casual_price_per_hour + maintenance_per_year))
    return profit


df['Profit/hour'] = df[['Casual', 'Registered']].apply(calculate_profit, axis=1)

# Question 2 #

rented_bikes_array = np.array(df['rented_bikes_count'])

rented_bikes_count_norm = np.random.normal(rented_bikes_array.mean(), rented_bikes_array.std(), rented_bikes_array.size)
plt.hist(rented_bikes_count_norm)

# Question 2 part 2 #
profit_per_hour_array = np.array(df['Profit/hour'])

profit_per_hour__norm = np.random.normal(profit_per_hour_array.mean(), profit_per_hour_array.std(),
                                         profit_per_hour_array.size)
plt.hist(profit_per_hour__norm)

# Question 3 #
profit_per_hour_array = np.array(df['Profit/hour'])
N = 24

rest = profit_per_hour_array.shape[0] % N
a = profit_per_hour_array[:-rest]

assert a.shape[0] % N == 0

# do the reshape
a_RS = a.reshape(-1, N)

profit_per_day_array = np.sum(a_RS, axis=1)

pd.DataFrame({'Profit/day': profit_per_day_array})

# Question 4 #
Season_max = df['season'][(df['registered'] == max(df['registered'])) & (df['Profit/hour'] == max(df['Profit/hour']))]
print('The season that has more registration & profit is: ', np.array(Season_max)[0])

# Question 5 #
Weather_max = df['weather'][(df['registered'] == max(df['registered'])) & (df['Profit/hour'] == max(df['Profit/hour']))]
print('The Weather that has more registration & profit is: ', np.array(Weather_max)[0])

# Question 6 #
df[['Profit/hour', 'rented_bikes_count']].corr()

# Question 7 #
rented_bikes_count_array = np.array(df['rented_bikes_count'])
rush_hour_bikes_lists = []
rush_hour_bikes = []
rush_hour_bikes_total = []
for n in range(int(len(rented_bikes_count_array) / 24) + (
        len(rented_bikes_count_array) - (24 * int(len(rented_bikes_count_array) / 24)))):
    rush_hour_bikes_lists.append(rented_bikes_count_array[n + 7:n + 10])
    rush_hour_bikes_lists.append(rented_bikes_count_array[n + 15:n + 18])

for n in range(len(rush_hour_bikes_lists)):
    rush_hour_bikes.append(rush_hour_bikes_lists[n])

for n in range(0, int(len(rush_hour_bikes) / 2) + (len(rush_hour_bikes) - (2 * int(len(rush_hour_bikes) / 2))), 2):
    rush_hour_bikes_total.append(sum(rush_hour_bikes[n]) + sum(rush_hour_bikes[n + 1]))

pd.DataFrame({'rented_bikes_rush_hour': rush_hour_bikes_total})

# Question 8 #
Rentals_work_holiday = df['rented_bikes_count'][(df['working_day'] == 1) | (df['holiday'] == 1)]

pd.DataFrame({'Rentals_workday_or_holiday': Rentals_work_holiday})

# Question 9 #
if sum(df['registered']) > sum(df['casual']):
    print('registered is more')
else:
    print('casual is more')

# Question 10 #
registered_array = np.array(df['registered'])

n = 24 * 7
registered_weekly = []
for i in range(0, len(registered_array), n):
    registered_weekly.append(np.mean(registered_array[i:i + n]))

pd.DataFrame({'Average of who registered weekly': registered_weekly})

# Question 11 #
rented_bikes_count_array = np.array(df['rented_bikes_count'])
bikes_school_lists = []
school_bikes = []
bikes_school_total = []

for n in range(int(len(rented_bikes_count_array) / 24) + (
        len(rented_bikes_count_array) - (24 * int(len(rented_bikes_count_array) / 24)))):
    bikes_school_lists.append(rented_bikes_count_array[n + 9:n + 13])
    bikes_school_lists.append(rented_bikes_count_array[n + 14:n + 19])

for n in range(len(bikes_school_lists)):
    school_bikes.append(bikes_school_lists[n])

for n in range(0, int(len(school_bikes) / 2) + (len(school_bikes) - (2 * int(len(school_bikes) / 2))), 2):
    bikes_school_total.append(sum(school_bikes[n]) + sum(school_bikes[n + 1]))

display(pd.DataFrame({'rented_bikes_school_times/day': bikes_school_total}))
print('total rented bikes at school times is :', np.sum(bikes_school_total))

# Question 11 #
profit2011_sat_fall = np.sum(df['Profit/hour'].loc[0:24 * 356]) + np.sum(
    df['Profit/hour'][df['season'] == 'Fall']) + np.sum(df['Profit/hour'].loc[24 * 356::24 * 7])

print('Profit in 2011 & saturdays & season fall is: ', profit2011_sat_fall)

# TASK 2 #

df2 = pd.read_csv('loan_data.csv')

df2.info()
df2.describe()
