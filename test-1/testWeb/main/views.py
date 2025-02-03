from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import json
import requests
from .models import Cityes
import datetime
from django.views.decorators.csrf import csrf_protect

appid = "2dc73daf624a5ff019e1d242171d53bf"

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def cityInfo(City):
    
    city_data = []

    weather_conditions = {
            800: "Ясное небо",
            801: "Небольшая облачность",
            802: "Переменная облачность",
            803: "Облачно с прояснениями",
            804: "Сплошная облачность",
            
            500: "Небольшой дождь",
            501: "Умеренный дождь",
            502: "Сильный дождь",
            503: "Очень сильный дождь",
            504: "Чрезвычайно сильный дождь",
            511: "Ледяной дождь",
            520: "Слабый ливень",
            521: "Ливень",
            522: "Сильный ливень",
            
            300: "Небольшая морось",
            301: "Морось",
            302: "Сильная морось",
            310: "Небольшая морось с дождём",
            311: "Морось с дождём",
            312: "Сильная морось с дождём",
            
            200: "Гроза с небольшим дождём",
            201: "Гроза с дождём",
            202: "Гроза с сильным дождём",
            210: "Слабая гроза",
            211: "Гроза",
            212: "Сильная гроза",
            221: "Рваная гроза",
            230: "Гроза с небольшой моросью",
            231: "Гроза с моросью",
            232: "Гроза с сильной моросью",
            
            600: "Небольшой снег",
            601: "Снег",
            602: "Сильный снег",
            611: "Дождь со снегом (мокрый снег)",
            612: "Небольшой мокрый снег",
            613: "Ливень с мокрым снегом",
            615: "Небольшой дождь со снегом",
            616: "Дождь со снегом",
            620: "Слабый снегопад",
            621: "Снегопад",
            622: "Сильный снегопад",
            
            701: "Лёгкий туман",
            711: "Дымка",
            721: "Мгла",
            731: "Пыльный ветер или песчаная буря",
            741: "Туман",
            751: "Песчаная буря",
            761: "Пыль",
            762: "Вулканический пепел",
            
            771: "Шквалистый ветер",
            781: "Торнадо"
        }
    
    weather_icons = {
            800: "bi-sun",  # Ясное небо
            801: "bi-cloud-sun",  # Небольшая облачность
            802: "bi-cloud",  # Переменная облачность
            803: "bi-cloudy",  # Облачно с прояснениями
            804: "bi-clouds",  # Сплошная облачность

            500: "bi-cloud-drizzle",  # Небольшой дождь
            501: "bi-cloud-rain",  # Умеренный дождь
            502: "bi-cloud-heavy-rain",  # Сильный дождь
            503: "bi-cloud-heavy-rain",  # Очень сильный дождь
            504: "bi-cloud-heavy-rain",  # Чрезвычайно сильный дождь
            511: "bi-cloud-sleet",  # Ледяной дождь
            520: "bi-cloud-drizzle",  # Слабый ливень
            521: "bi-cloud-rain",  # Ливень
            522: "bi-cloud-heavy-rain",  # Сильный ливень

            300: "bi-cloud-drizzle",  # Небольшая морось
            301: "bi-cloud-drizzle",  # Морось
            302: "bi-cloud-drizzle",  # Сильная морось
            310: "bi-cloud-drizzle",  # Небольшая морось с дождём
            311: "bi-cloud-rain",  # Морось с дождём
            312: "bi-cloud-heavy-rain",  # Сильная морось с дождём

            200: "bi-cloud-lightning-rain",  # Гроза с небольшим дождём
            201: "bi-cloud-lightning-rain",  # Гроза с дождём
            202: "bi-cloud-lightning-rain",  # Гроза с сильным дождём
            210: "bi-cloud-lightning",  # Слабая гроза
            211: "bi-cloud-lightning",  # Гроза
            212: "bi-cloud-lightning",  # Сильная гроза
            221: "bi-cloud-lightning",  # Рваная гроза
            230: "bi-cloud-lightning-rain",  # Гроза с небольшой моросью
            231: "bi-cloud-lightning-rain",  # Гроза с моросью
            232: "bi-cloud-lightning-rain",  # Гроза с сильной моросью

            600: "bi-cloud-snow",  # Небольшой снег
            601: "bi-cloud-snow",  # Снег
            602: "bi-cloud-snow-heavy",  # Сильный снег
            611: "bi-cloud-sleet",  # Дождь со снегом
            612: "bi-cloud-snow",  # Небольшой мокрый снег
            613: "bi-cloud-snow-heavy",  # Ливень с мокрым снегом
            615: "bi-cloud-sleet",  # Небольшой дождь со снегом
            616: "bi-cloud-sleet",  # Дождь со снегом
            620: "bi-cloud-snow",  # Слабый снегопад
            621: "bi-cloud-snow",  # Снегопад
            622: "bi-cloud-snow-heavy",  # Сильный снегопад

            701: "bi-cloud-fog",  # Лёгкий туман
            711: "bi-cloud-haze",  # Дымка
            721: "bi-cloud-haze",  # Мгла
            731: "bi-wind",  # Пыльный ветер или песчаная буря
            741: "bi-cloud-fog",  # Туман
            751: "bi-wind",  # Песчаная буря
            761: "bi-wind",  # Пыль
            762: "bi-cloud-drizzle",  # Вулканический пепел

            771: "bi-wind",  # Шквалистый ветер
            781: "bi-tornado",  # Торнадо
        }
    weather_icons_night = {
        800: "bi-moon",
        801: "bi-cloud-moon",
    }

    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={City}&lang=ru&units=metric&appid={appid}")
    data = response.json()
    print(response)
    error = int(data['cod'])
    if 404 == error:
        print('error')
        return error
    else:
                    
        Jcity = data['name']
        Jtemp = int(data['main']['temp'])
        Jfeels_like = int(data['main']['feels_like'])
        Jwind_speed = float(data['wind']['speed'])
        Jvisibility = int(data['visibility'])
        Jkm = Jvisibility // 1000

        Jsunrise = int(data['sys']['sunrise'])
        JsunriseNormal = datetime.datetime.fromtimestamp(int(Jsunrise)).strftime('%H:%M')

        Jsunset = int(data['sys']['sunset'])
        JsunsetNormal = datetime.datetime.fromtimestamp(int(Jsunset)).strftime('%H:%M')
        
        JweatherN = int(data['weather'][0]['id'])
        Jweather = weather_conditions.get(JweatherN)

        Jweather_icon = weather_icons.get(JweatherN)

        lon = float(data['coord']['lon'])
        lat = float(data['coord']['lat'])

        Jdt = int(data['dt'])
        dt = datetime.datetime.fromtimestamp(int(Jdt)).strftime('%H:%M')
        if dt >= "20:00" or dt <= "06:00":
            if JweatherN == 800 or JweatherN == 801:
                Jweather_icon = weather_icons_night.get(JweatherN)

        
        Cdata = {
            "Jcity": Jcity,
            "Jtemp": Jtemp,
            "Jfeels_like": Jfeels_like,
            "Jwind_speed": Jwind_speed,
            "Jvisibility": Jvisibility,
            "Jkm": Jkm,
            "Jsunrise": JsunriseNormal,
            "Jsunset": JsunsetNormal,
            "Jweather": Jweather,
            "Jweather_icon": Jweather_icon,
            "lon": lon,
            "lat": lat

        }
        print("lon: ",lon)
        print("lat: ",lat)
        print(JweatherN)
        print(Jweather)
        print(Jweather_icon)
        print("Город: ",Jcity)
        print("Темпиратура: ",Jtemp)
        print("Ощущается как :",Jfeels_like)
        print("скорость :",Jwind_speed)
        print("видимость :",Jvisibility," m\n",Jkm,"km")
        print("расвет :", JsunriseNormal)
        print("закат :", JsunsetNormal)

        print(Cdata)
        city_data.append(Cdata)
        return Cdata
    
@csrf_protect
def oneCity(request):
    ip = get_client_ip(request)
    res = requests.get(f"http://ipwho.is/{ip}")
    METAdata = res.json()
    METAcity = METAdata['city']
    if request.POST:
        City = request.POST.get("findcity")
        status = cityInfo(City)
        if status == 404:
            return render(request, 'main/page.html')
        else:
            try:
                return render(request, 'main/page.html', {'data': status})
                #return HttpResponse(f"<h2>{_City}</h2>") 
            except Cityes.DoesNotExist:
                return render(request, 'main/page.html')
    else:
        status = cityInfo(METAcity)
        if status == 404:
            return render(request, 'main/page.html')
        else:
            try:
                return render(request, 'main/page.html', {'data': status})
                #return HttpResponse(f"<h2>{_City}</h2>") 
            except Cityes.DoesNotExist:
                return render(request, 'main/page.html')
        
