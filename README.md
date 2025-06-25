# Weather Dashboard 🌤

A simple Flask-based web app that lets users check the current weather of any city using the **WeatherAPI.com** service.

## Features
✅ Users can enter a city name (e.g. `London`, `New York`, `Paris,FR`)  
✅ Displays:
- City name
- Temperature (°C)
- Humidity (%)
- Weather condition (e.g. Partly cloudy)

## Technologies Used
- Python 3
- Flask
- WeatherAPI.com (for real-time weather data)

## Setup Instructions

1️⃣ Clone this repo or copy the files to your local machine.  

2️⃣ Install dependencies:
```bash
pip install flask requests
```
3️⃣ Get your free API key from https://www.weatherapi.com/.

4️⃣ Update your API_KEY in the Python file:
```python
API_KEY = 'YOUR_WEATHERAPI_KEY'
```
5️⃣ Run the app:
```bash
python app.py
```
6️⃣ Open your browser and visit:
```
http://127.0.0.1:5000/
```
