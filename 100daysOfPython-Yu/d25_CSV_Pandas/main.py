# data = []
# with open('./weather_data.csv') as weather_data:
#     data = weather_data.readlines()
#
# print(data)

# import csv
#
# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#
#
# print(temperatures)

import pandas

data = pandas.read_csv('./weather_data.csv')

# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
#
# #print('average Temperature: ' + str(round(sum(temp_list)/len(temp_list),2)) )
#
# average_temp = data['temp'].mean()
#
max_temp = data['temp'].max()
# print(max_temp)

#print(data.condition)
#equal to data['condition']

#get data from data frame rows
#print(data[data.temp == max_temp])

# monday = data[data.day == 'Monday']
#
# print((float(monday.temp[0])) * (9/5) + 32)

