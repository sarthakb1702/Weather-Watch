from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '1aa4d667d7d7b325eb31d0a006621d98'  # Replace with your actual key

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city'].strip()
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'description': data['weather'][0]['description'].title()
            }
        else:
            try:
                data = response.json()
                error_message = data.get('message', 'Error fetching weather')
            except Exception:
                error_message = 'Error fetching weather'
            weather = {'error': error_message}

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)

