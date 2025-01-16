from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import requests
from .models import Cityes


appid = "2dc73daf624a5ff019e1d242171d53bf"



def cityInfo(City):
    error = {"cod":"404","message":"city not found"}
    city_data = []


    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&lang=ru&units=metric&appid={appid}")
    data = response.json()
    print(response)
    if data == error:
        print('error')
        pass 
    else:
                    
        Jcity = data['name']
        Jtemp = int(data['main']['temp'])
        Jfeels_like = int(data['main']['feels_like'])
        Jwind_speed = int(data['wind']['speed'])
                    
        Cdata = {
            "Jcity": Jcity,
            "Jtemp": Jtemp,
            "Jfeels_like": Jfeels_like,
            "Jwind_speed": Jwind_speed

        }

        print("Город: ",Jcity)
        print("Темпиратура: ",Jtemp)
        print("Ощущается как :",Jfeels_like)
        print("скорость :",Jwind_speed)

        print(Cdata)
        city_data.append(Cdata)
        return Cdata
    print(city_data) 

def oneCity(request):
    City = request.POST.get("findcity")
    try:
        data = Cityes.objects.get(city=City)

        _City = cityInfo(data)
        return render(request, 'main/page.html', {'data': _City})
        #return HttpResponse(f"<h2>{_City}</h2>") 
    except Cityes.DoesNotExist:
        return render(request, 'main/page.html')
# Create your views here.
def mainPage(request):
    try:    
            error = {"cod":"404","message":"city not found"}
            namesC = Cityes.objects.all()
            print(namesC)
            city_data = []
            for city in namesC:
                print(city.city)

                response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&lang=ru&units=metric&appid={appid}")
                data = response.json()
                print(response)
                if data == error:
                    print('error')
                    pass 
                else:
                    
                    Jcity = data['name']
                    Jtemp = int(data['main']['temp'])
                    Jfeels_like = int(data['main']['feels_like'])
                    Jwind_speed = int(data['wind']['speed'])
                    
                    Cdata = {
                        "Jcity": Jcity,
                        "Jtemp": Jtemp,
                        "Jfeels_like": Jfeels_like,
                        "Jwind_speed": Jwind_speed,
                    }

                    print("Город: ",Jcity)
                    print("Темпиратура: ",Jtemp)
                    print("Ощущается как :",Jfeels_like)
                    print("Минимальная темпиратура :",Jwind_speed)

                    print(Cdata)
                    city_data.append(Cdata)
            print(city_data)
            return render(request, 'main/main2.html', {'data': city_data})
            
    except Exception as e:
            print(e)