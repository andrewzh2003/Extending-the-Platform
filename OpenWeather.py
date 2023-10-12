# openweather.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python
import urllib, json
import datetime
from urllib import request, error
from WebAPI import WebAPI

class OpenWeather(WebAPI):
    '''def __init__(self, zipcode, ccode):
        self.zipcode = zipcode
        self.ccode = ccode'''

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.     
        '''
        zipcode = "92697"
        ccode = "US"
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zipcode},{ccode}&appid={self.apikey}&units=imperial"
        weather_obj = self._download_url(url)
        if weather_obj is not None:
            self.temperature = weather_obj['main']['temp']
            self.high_temperature = weather_obj['main']['temp_max']
            self.low_temperature = weather_obj['main']['temp_min']
            self.longitude = weather_obj['coord']['lon']
            self.latitude = weather_obj['coord']['lat']
            self.description = weather_obj['weather'][0]['description']
            self.humidity = weather_obj['main']['humidity']
            self.sunset = datetime.datetime.fromtimestamp(int(weather_obj['sys']['sunset'])).strftime('%H:%M:%S')
            self.city = weather_obj['name']
            self.pressure = weather_obj['main']['pressure']

    def transclude(self, message:str) -> str: ## weather description
        if '@weather' in message:
            new = message.split("@weather")
            x = self.description
            i = 0
            trascluded_message = ''
            while i < len(new):
                if i < len(new) - 1:
                    trascluded_message += new[i]
                    trascluded_message += x
                    i += 1
                else:
                    trascluded_message += new[i]
                    i += 1
            return trascluded_message
        else:
            return message
    '''
    Replaces keywords in a message with associated API data.
    :param message: The message to transclude
        
    :returns: The transcluded message
    '''
    #TODO: write code necessary to transclude keywords in the message parameter with appropriate data from API
    pass
    #TODO: use the apikey data attribute and the urllib module to request data from the web api. See sample code at the begining of Part 1 for a hint.
    #TODO: assign the necessary response data to the required class data attributes

# NAME
# EMAIL
# STUDENT ID

