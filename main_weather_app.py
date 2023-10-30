import requests
import tkinter as tk

key = "ad6393dd49254ee9909195433233010"

# current_conditions = requests.get(f"http://api.weatherapi.com/v1/current.json?key=ad6393dd49254ee9909195433233010&q={location}&aqi=no")
# print(type(current_conditions.json()))
# print(current_conditions.json())


def get_current_weather():
    location = location_input_field.get()

    current_conditions = requests.get(
        f"http://api.weatherapi.com/v1/current.json?key={key}&q={location}&aqi=no")

    if current_conditions:
        data = current_conditions.json()
        city = data["location"]["name"]
        region = data["location"]["region"]
        temp_F = data["current"]["temp_f"]

        print(city)
        print(temp_F)

        weather_label.config(text=f"{city}, {region}:  {temp_F}° F")

        return city, temp_F


#############################
#  INTERACTIVE GUI          #
############################

# make the window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x500")



# Input label
location_input_label = tk.Label(root, text="Enter either City, State or Zip Code:")
location_input_label.pack()

# Input field
location_input_field = tk.Entry(root)
location_input_field.pack()

submit_button = tk.Button(root, text="Get Current Weather", command=get_current_weather)
submit_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()



root.mainloop()


# get_current_weather("London")