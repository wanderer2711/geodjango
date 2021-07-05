from typing import List

from django.views.generic.base import TemplateView
from .models import Location
import requests
from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
import json
from django.core.serializers import serialize

def index(request):
    l = Location.objects.filter(point__isnull=False)
    for i in l:
        lat = str(i.point.coords[1])
        lon = str(i.point.coords[0])

        model = Location
        api_key = "7aad66ca433ee2d64650f4c17ce798e8"
        url = 'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=7aad66ca433ee2d64650f4c17ce798e8'
        base_url = 'http://api.openweathermap.org/data/2.5/weather?'


        comp_url = base_url +   "lat=" + lat + "&lon=" + lon + "&appid=" + api_key + "units=metric"
        
        q = requests.get(url=comp_url).json()
        print(q)

        city_weather = {
            # 'city': q['main']['name'], 
            'temperature': q['main']['temp'],
            'humidity': q['main']['humidity']
        }

    # city_weather = {

    # }
    # queryset = Location.objects.filter(point__isnull=False)

    data = {'l' : l, 'city_weather': city_weather}

    return render(request, 'weather/weather.html', data)

# class Weather(TemplateView):
#     template_name = "weather/weather.html"


#     def get_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["location"] = json.loads(serialize("geojson", Location.objects.all()))
#         return context
    