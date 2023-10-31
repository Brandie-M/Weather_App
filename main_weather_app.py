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
        country = data["location"]["country"]
        temp_F = data["current"]["temp_f"]

        print(city)
        print(temp_F)

        if country != "United States of America":
            weather_location.config(text=f"{city}, {country}")
        else:
            weather_location.config(text=f"{city}, {region}")

        temperature_F.config(text=f"{temp_F}° F")
    else:
        weather_location.config(text="Please enter a valid City or Zip Code.")
        temperature_F.config(text="")

        # return city, temp_F

def show_help():
    help_text.config(text="Available Features: "
                          "\n    1. Searchable world-wide locations. "
                          "\n    2. Current temperature in Fahrenheit ."
                          "\n \n\nHow to use this app:"
                          "\n    1. Type a City and State OR a Zip Code into the blank field \n        and click the Get Current Temperature button."
                           "\n   2. If you only type a city, the app will pick the city/state \n        or city/country combination that is most popular."
                        "\n    3. If you want to check the weather for somewhere else, \n        simply type in another location."
                          "\n\n \nTroubleshooting: \nIf you clicked the Get Current Temperature button and the weather doesn't show make sure: "
                          "\n    1. You are connected to the internet."
                          "\n    2. You have entered a valid Zip Code or City name."
                     )

#############################
#  INTERACTIVE GUI          #
############################

# make the window
root = tk.Tk()
root.title("Weather App")
root.geometry("500x800")
root.configure(background="white")

# page heading
heading_label = tk.Label(
    root,
    text="Welcome to the On-Demand Weather App",
    font=(100),
    background="white"
)
heading_label.pack(
    padx=20,
    pady=20
)

# Input label
location_input_label = tk.Label(root, text="Enter a City, State or Zip Code:")
location_input_label.pack(
    padx=3,
    pady=3
)

# Input field
location_input_field = tk.Entry(
    root,
    background="LightSteelBlue1"
)
location_input_field.pack(
    padx=10,
    pady=10
)

#submit button
submit_button = tk.Button(
    root,
    text="Get Current Temperature",
    command=get_current_weather,
    background="SteelBlue1"
)
submit_button.pack(
    padx=10,
    pady=10
)

# Shows weather location
weather_location = tk.Label(root, text="", background="white")
weather_location.pack(
    padx=10,
    pady=10
)

# Temperature in F
temperature_F = tk.Label(
    root,
    text="",
    font=100,
    background="white"
)
temperature_F.pack(
    padx=0,
    pady=0
)

#help button
help_button = tk.Button(
    root,
    text="I need help!",
    command=show_help,
    background="SteelBlue1"
)
help_button.pack(
    padx=30,
    pady=30
)

help_text = tk.Label(
    root,
    text="",
    background="light cyan",
    wraplength=400,
    anchor="w",
    justify="left",
    pady=20,
    padx=20

)
help_text.pack(
)

root.mainloop()

