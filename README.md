# Weather API

A simple weather API built with Django and Django Rest Framework (DRF) that fetches weather data from OpenWeatherMap based on the city name provided by the user.

## Features
- Fetch weather data for a city
- Default city is "London" if no city is provided
- Returns current weather, temperature, humidity, and other relevant details

## Requirements

- Python 3.x
- Django 5.x
- Django Rest Framework (DRF)
- `requests` library for making API calls to OpenWeatherMap
- OpenWeatherMap API key (sign up at [OpenWeatherMap](https://openweathermap.org/) to get your free API key)

## Installation

### 1. Clone the repository


git clone <repository-url>
cd <repository-directory>
Set up a virtual environment
python -m venv venv
source venv/bin/activate  # For MacOS/Linux
venv\Scripts\activate  # For Windows
3. Install the dependencies
bash
Copy code
pip install -r requirements.txt
4. Set your OpenWeatherMap API key
In services.py, replace the placeholder your_actual_api_key_here with your actual OpenWeatherMap API key:

python
Copy code
api_key = "your_actual_api_key_here"
5. Run database migrations
bash
Copy code
python manage.py migrate
6. Start the Django development server
bash
Copy code
python manage.py runserver
Usage
Once the server is running, you can test the weather API by sending a GET request to:

ruby
Copy code
http://127.0.0.1:8000/api/weather/?city=New York
If you don’t provide a city, it defaults to "London":

ruby
Copy code
http://127.0.0.1:8000/api/weather/
Response
The API will return a JSON response with the weather data, including:

temperature (in Celsius)
humidity
weather description
wind speed
and other details
Example Response:
json
Copy code
{
    "main": {
        "temp": 16.25,
        "humidity": 78
    },
    "weather": [
        {
            "description": "light rain"
        }
    ],
    "wind": {
        "speed": 3.6
    },
    "name": "New York"
}
Troubleshooting
If you encounter issues like "404 Not Found," ensure:

Your server is running (python manage.py runserver).
You have configured the URL path correctly in urls.py.
Your API key is correctly placed in services.py.
License
This project is licensed under the MIT License - see the LICENSE file for details.

Enjoy using the Weather API! 🌤️

sql
Copy code

You can now copy and paste this whole block directly into your `README.md` file! Let me know if you need any further adjustments.
