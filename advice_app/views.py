from django.shortcuts import render
from pip._vendor import requests

url = "https://api.adviceslip.com/advice"

# Create your views here.
def index(request):
    data = requests.get(url)
    json_data = data.json()
    random_advice = json_data["slip"]

    return render(request, 'index.html', {'random_advice': random_advice})