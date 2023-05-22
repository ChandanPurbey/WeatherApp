from flask import Flask,render_template,request
import requests
import json

app = Flask(__name__)



@app.route('/',methods=['GET','POST'])
def input():
    return render_template('index.html')


@app.route('/output',methods=['GET','POST'])
def output():
    with open('API_key.json') as file:
        credentials = json.load(file)

    api_key = credentials['API_key']
    print(api_key)
    if request.method == 'POST':
        print('coming here')
        city = request.form['city']

        url = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+api_key+"&units=metric" 
        response = requests.get(url)
        try:
            if response.status_code == 200:
                data = response.json()
                print(data)
                weather_data = {
                'cityName': data['name'],
                'temperature': data['main']['temp'],
                'weatherDescription': data['weather'][0]['description']
                }
                print(weather_data)
                return render_template('output.html', weather_data=weather_data)
        except Exception as e:
            return str(e)
    else:
        return 'Invalid request method'
    


if __name__=='__main__':
    app.run(debug=False)