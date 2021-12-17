from django.shortcuts import render

# Create your views here.
import json
import urllib

import main

def index(request):
    if request.method == 'Post':
        city = request.POST['city']

        #taking json data from api
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q = ' + city + '&appid = API_KEY ').read()
        
        #Json --> dictionary
        list_of_data = json.loads(source)

        #data for variable list_of_data
        data = {
            "country_code" : str(list_of_data['sys']['country']),
            'coordinate'   : str(list_of_data['coord']['lon']) + ' ' + str(['coord']['lat']),
            'temp'         : str(list_of_data['main']['temp']) + 'K',
            'pressure'     : str(list_of_data['main']['pressure']),
            'humidity'     : str(list_of_data['main']['humidity']),
        }
        print(data)
    else:
        data = {}
    return render(request , 'index.html' , data )


