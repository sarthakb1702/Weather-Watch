from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '07cdde153adc42f5af6164214252506'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form['city'].strip()
        url = f'http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}'
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            weather = {
                'city': data['location']['name'],
                'temperature': data['current']['temp_c'],
                'humidity': data['current']['humidity'],
                'description': data['current']['condition']['text']
            }
        else:
            try:
                data = response.json()
                error_message = data.get('error', {}).get('message', 'Error fetching weather')
            except Exception:
                error_message = 'Error fetching weather'
            weather = {'error': error_message}

    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
