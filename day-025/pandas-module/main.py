# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
#
# temp_list = data["temp"].to_list()
# print(f"{temp_list=}")
#
# # Calculate the average temperature
# mean_temp = data["temp"].mean()
# print(f"{mean_temp=}")
#
# # Return max value
# max_temp = data["temp"].max()
# print(f"{max_temp=}")
#
# # Get Data in columns
# print(data["condition"])
# print(data.condition)
#
# # Get data in Row
# print(data[data.day == "Monday"])
#
# # Get day when the temperature was the highest
# print(data[data.temp == data.temp.max()].day)
#
# # Convert Monday's temperature to Fahrenheit
# monday = data[data.day == "Monday"]
# monday_temp = monday.temp[0]
# print(monday_temp * 9 / 5 + 32)
#
# # # Create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")


import pandas as pd

data = pd.read_csv(
    "2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20241112.csv")

gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])

count_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
df = pd.DataFrame(count_dict)
df.to_csv("squirrel_count.csv")