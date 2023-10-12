from LastFM import LastFM
from OpenWeather import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI

def test_api(message:str, apikey:str, webapi:WebAPI):
  webapi.set_apikey(apikey)
  webapi.load_data()
  result = webapi.transclude(message)
  print(result)


open_weather = OpenWeather() #notice there are no params here...HINT: be sure to use parameter defaults!!!
lastfm = LastFM()

test_api("Testing the weather: @weather", '3e6e18ffbc23e0c8919d6484aafc5da8', open_weather)
# expected output should include the original message transcluded with the default weather value for the @weather keyword.

test_api("Testing lastFM: @lastfm", "07808c7623679f2fce1fbbb12aab3cbb", lastfm)
# expected output include the original message transcluded with the default music data assigned to the @lastfm keyword