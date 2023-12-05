# Weather_App
Python weather app that uses Tkinkter for the GUI and calls for data from Weather API
# Interactive Weather Application

This repository contains the code for an interactive desktop weather application. Built with Python, this application provides real-time weather information and engages users with random weather trivia. It features a user-friendly graphical user interface (GUI) built with Tkinter and integrates with WeatherAPI for live weather updates.

## Features

- **Real-Time Weather Data**: Fetches and displays current weather conditions based on user-input locations.
- **Weather Trivia**: A Flask microservice that serves random weather-related trivia, enhancing user engagement.
- **Dynamic Icons**: Uses the Python Imaging Library (PIL) to display weather condition-specific icons.
- **Robust Error Handling**: Ensures seamless API interactions and enhances user experience.

## Installation

To run this application, you will need Python installed on your system. Clone the repository and install the required dependencies:

```bash
git clone [https://github.com/yourusername/weather-app.git](https://github.com/Brandie-M/Weather_App)
cd weather-app
pip install -r requirements.txt
```

## Usage

To start the application, run:

```bash
python main.py
```
Enter a city, state, or ZIP code in the input field and click "Get Current Weather" to view the weather data. Click "Get Random Weather Trivia" for interesting trivia.

## License
This project is licensed under the [MIT License](http://opensource.org/licenses/MIT).

## Acknowledgments
  - **Weather data provided by [WeatherAPI](https://www.weatherapi.com/).
  - **Trivia data served by a custom Flask microservice.
