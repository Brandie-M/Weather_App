import requests, json
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

key = "ad6393dd49254ee9909195433233010"

##################
## Microservice ##
##################

def get_random_trivia():
    response = requests.get("http://localhost:5000/random_trivia")

    if response.status_code == 200:
        print("Requesting Random Trivia")
        trivia_text = response.json().get("trivia")
        trivia.config(text=trivia_text)
        print(trivia_text)
    else:
        print("failed to get trivia")
        trivia.config(text="Sorry, we couldn't get the trivia. Please try again later.")

###############
## Main App ##
##############

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
        temp_C = data["current"]["temp_c"]
        conditions = data["current"]["condition"]["text"]
        conditions_icon_code = data["current"]["condition"]["code"]
        humidity = data["current"]["humidity"]
        feelslike_F = data["current"]["feelslike_f"]
        feelslike_C = data["current"]["feelslike_c"]
        wind_mph = data["current"]["wind_mph"]
        wind_kph = data["current"]["wind_kph"]
        wind_dir = data["current"]["wind_dir"]
        is_day = data["current"]["is_day"]
        uv = data["current"]["uv"]
        precipitation_in = data["current"]["precip_in"]
        precipitation_mm = data["current"]["precip_mm"]


        condition_icon = find_icon(conditions_icon_code)

        temperature.pack()
        more_info.pack()
        current_conditions_status.pack()
        current_conditions_icon.pack()

        if country != "USA" and country != "United States of America":
            weather_location.config(text=f"{city}, {country}")
            temperature.config(text=f"{temp_C}° C")
            more_info.config(
                text=f"Additional Info: \n\n"
                     f"Feels like: {feelslike_C}° C \n"
                     f"Humidity: {humidity}% \n"
                     f"Wind: {wind_kph} kph {wind_dir} \n"
                     f"UV Index: {uv} \n"
                     f"Precipitation: {precipitation_mm} mm"
            )
        else:
            weather_location.config(text=f"{city}, {region}")
            temperature.config(text=f"{temp_F}° F")
            more_info.config(
                text=f"Additional Info: \n\n"
                     f"Feels like: {feelslike_F}° F \n"
                     f"Humidity: {humidity}% \n"
                     f"Wind: {wind_mph} mph {wind_dir} \n"
                     f"UV Index: {uv} \n"
                     f"Precipitation: {precipitation_in} in"
            )
        
        current_conditions_status.config(text=f"{conditions}")

        if is_day == 1:
            image_path = f"day/{condition_icon}.png"
        else:
            image_path = f"night/{condition_icon}.png"

        # Load and display the image
        image = Image.open(image_path)
        photo = ImageTk.PhotoImage(image)
        current_conditions_icon.config(image=photo)
        current_conditions_icon.image = photo

    else:
        weather_location.config(text="Please enter a valid City or Zip Code.")
        temperature.pack_forget()
        more_info.pack_forget()
        current_conditions_status.pack_forget()
        current_conditions_icon.pack_forget()



def find_icon(icon_code):
    with open("weather_conditions.json", "r") as file:
        weather_conditions = json.load(file)
        for condition in weather_conditions:
            if condition["code"] == icon_code:
                print(condition["icon"])
                return condition["icon"]


def display_help(button_text):
    if button_text == "Available Features":
        help_text.config(text="Available Features: "
                            "\n\n    1. Searchable world-wide locations. "
                            "\n    2. Current temperature in Fahrenheit (USA) or Celsius (rest of the world)."
                            "\n    3. Current weather conditions."
                            "\n    4. Current weather conditions icon."
                            "\n    5. Additional weather information (Feels like, Humidity, Wind, UV, Precipitation)."
                            "\n    6. Random weather trivia.")
    elif button_text == "How to use this app":
        help_text.config(text="How to use this app:"
                           "\n\n    1. Type a City and State OR a Zip Code into the blank "
                              "field and click the Get Current Weather button."
                           "\n    2. If you only type a city, the app will pick the "
                              "city/state or city/country combination that is most popular."
                           "\n    3. If you want to check the weather for "
                              "somewhere else, simply type in another location."
                           )
    elif button_text == "Troubleshooting":
        help_text.config(text="Troubleshooting: \nIf you clicked the Get Current Weather button "
                              "and the weather doesn't show make sure: "
                          "\n\n    1. You are connected to the internet."
                          "\n    2. You have entered a valid Zip Code or City name."
                          )


def pass_button_text(button_text):
    display_help(button_text)


#############################
#  INTERACTIVE GUI          #
############################

# make the window
root = tk.Tk()
root.title("Weather App")
root.geometry("700x700")
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


### Weather Display  ###

# Input label
location_input_label = tk.Label(root, text="Enter a City, State, City, Country, or Zip Code:")
location_input_label.pack(padx=3,pady=3)

# Input field
location_input_field = tk.Entry(root, background="LightSteelBlue1")
location_input_field.pack(padx=10, pady=10)

#submit button
submit_button = tk.Button(
    root,
    text="Get Current Weather",
    command=get_current_weather,
    background="SteelBlue1"
)
submit_button.pack()


# Weather Frame
outer_weather_frame = tk.Frame(root, bg="white")
outer_weather_frame.pack(padx=10, pady=10)

inner_weather_frame_left = tk.Frame(outer_weather_frame, bg="white")
inner_weather_frame_left.pack(side=tk.LEFT, padx=20, pady=20)

inner_weather_frame_right = tk.Frame(outer_weather_frame, bg="white")
inner_weather_frame_right.pack(side=tk.RIGHT, padx=20, pady=20)


# Display weather location
weather_location = tk.Label(inner_weather_frame_left, text="", background="white", justify="left")
weather_location.pack()

# Temperature display
temperature = tk.Label(inner_weather_frame_left, text="", font=100, background="white", justify="left")
temperature.pack()

# Current conditions icon
current_conditions_icon = tk.Label(inner_weather_frame_left, image="", background="white", justify="left")   
current_conditions_icon.pack()

# Current conditions display
current_conditions_status = tk.Label(inner_weather_frame_left, text="", background="white", justify="left")
current_conditions_status.pack()

# More info display
more_info = tk.Label(inner_weather_frame_right, text="", background="white", justify="left")
more_info.pack()


#####################
# Trivia Section Display   #
####################

# Trivia Frame
frame1 = tk.Frame(root, bg="white")
frame1.pack(padx=10, pady=10)

# Creating a horizontal separator
separator = ttk.Separator(frame1, orient='horizontal')
separator.pack(fill='x', pady=5)

#Trivia button
submit_button = tk.Button(
    frame1,
    text="Click for Random Weather Trivia (Just for fun!)",
    command=get_random_trivia,
    background="SteelBlue1"
)
submit_button.pack(padx=10, pady=10)

# Shows trivia
trivia = tk.Label(frame1, text="", background="white")
trivia.pack(padx=10, pady=10)

# Creating a horizontal separator
separator = ttk.Separator(frame1, orient='horizontal')
separator.pack(fill='x', pady=5)

# Help section label
help_section_label = tk.Label(root, text="Need help? Click one of the buttons below:", background="white")
help_section_label.pack(padx=3, pady=3)

# Help section frame
frame = tk.Frame(root, bg="white")
frame.pack()

### help section ###

#Available features button
available_features_button = tk.Button(
    frame,
    text="Available Features",
    command=lambda: pass_button_text("Available Features"),
    background="SteelBlue1"
)
available_features_button.pack(padx=10, pady=10, side=tk.LEFT)

#How to use button
how_to_use_button = tk.Button(
    frame,
    text="How to use this app",
    command=lambda: pass_button_text("How to use this app"),
    background="SteelBlue1"
)
how_to_use_button.pack(padx=10, pady=10, side=tk.LEFT)

#Troubleshooting button
troubleshooting_button = tk.Button(
    frame,
    text="Troubleshooting",
    command=lambda: pass_button_text("Troubleshooting"),
    background="SteelBlue1"
)
troubleshooting_button.pack(padx=10, pady=10, side=tk.LEFT)

# Available Features Text
help_text = tk.Label(
    root,
    text="",
    wraplength=600,
    background="white",
    anchor="w",
    justify="left"
)
help_text.pack()


root.mainloop()

