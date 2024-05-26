import requests
from django.shortcuts import render

def get_weather(request):
    if request.method == 'POST':
        city = request.POST['city']
        api_key = '6c86f3c8241660a41ad79d2900626b9e'  # Replace with your OpenWeatherMap API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={'6c86f3c8241660a41ad79d2900626b9e'}'
        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
            context = {
                'city': city,
                'temperature': weather_data['main']['temp'],
                'description': weather_data['weather'][0]['description'],
                'icon': weather_data['weather'][0]['icon'],
            }
        else:
            context = {'error': 'City not found'}
        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
