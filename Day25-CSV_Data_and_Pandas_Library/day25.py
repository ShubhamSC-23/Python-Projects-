import pandas

data = pandas.read_csv("/Users/moniqueschukking/PycharmProjects/day-25/weather.csv")
print(data["temp"])

data_dict = data.to_dict()  
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)
print(len(temp_list))


average_temp = sum(temp_list) / len(temp_list)
print(average_temp)
avg_series_data = data["temp"].mean()
print(avg_series_data)


print(data["temp"].max())


print(data.temp)
print(data["temp"])


print(data[data.day == "Monday"])


print(data[data.temp == data.temp.max()])


def c_to_f(temp_c):
    temp_f = temp_c * (9/5) + 32
    return temp_f

monday = data[data.day == "Monday"]
print(monday.temp)
monday_temp_f = c_to_f(temp_c = monday.temp)
print(monday_temp_f)

data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}
data = pandas.DataFrame(data_dict)

data.to_csv("new_data.csv")




import pandas

data = pandas.read_csv("/Users/moniqueschukking/PycharmProjects/day-25/2018_Central_Park_Squirrel_Census_-_"
                       "Squirrel_Data.csv")
print(data["Primary Fur Color"].value_counts())  

sum_gray = sum(data["Primary Fur Color"] == "Gray")  
sum_cinnamon = sum(data["Primary Fur Color"] == "Cinnamon")
sum_black = sum(data["Primary Fur Color"] == "Black")

color_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Squirrel Count": [sum_gray, sum_cinnamon, sum_black],
}
print(color_dict)

color_df = pandas.DataFrame(color_dict)
print(color_df)

color_df.to_csv("squirrel_count.csv")
