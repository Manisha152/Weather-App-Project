
import requests
api_key = 'cf6c5a505492d70cf208eead5779a4c9'


city = input('Enter city name: ')

url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
   # print(data)
    
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    sunrise=data['sys']['sunrise']
    sunset=data['sys']['sunset']
    visibility=data['visibility']
    humidity=data['main']['humidity']
    country=data['sys']['country']

    print(f'Temperature: {int(temp-273.15)} C')
    print(f'Description: {desc}')
    print(f'Sunrise: {sunrise}')
    print(f'Sunset:{sunset}')
    print(f'Visibility:{visibility}')
    print(f'Humidity:{humidity}')
    print(f'Country:{country}')

else:
    print('Error fetching weather data')