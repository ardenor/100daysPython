import pandas
# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)






# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list) / len(temp_list)
# print(f"average: ",average)
#
# print(data["temp"].mean())
# print(data["temp"].max())






#get data in columns
# print(data["condition"])
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# mon_temp = monday.temp[0]
# mon_temp_f = mon_temp * 9/5 + 32
# print(f"{mon_temp_f} Fahrenheit")

#create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Colin"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# # print(data)
# data.to_csv("new_data.csv")





#squirrels
# data = pandas.read_csv("squirrels.csv")
# gray_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
# red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
# black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
# print(gray_squirrels_count)
# print(red_squirrels_count)
# print(black_squirrels_count)
#
# data_dict = {
#     "Fur Color": ["Gray", "Cinnamon", "Black"],
#     "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
# }
#
# df = pandas.DataFrame(data_dict)
# df.to_csv("squirrel_count.csv")






