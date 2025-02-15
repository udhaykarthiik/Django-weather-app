import requests
from django.shortcuts import render

def get_weather(request):
    weather_data = None
    error = None 

    api_key = '82802833e828ccce828682058b2722a4'  # Replace with your actual API key

    if request.method == "POST":
        city = request.POST.get("city")  # Use .get() to avoid errors if no input is given
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)  # Fixed this line!

        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found!"

    return render(request, "index.html", {"weather": weather_data, "error": error})
