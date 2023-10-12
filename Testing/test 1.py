from OpenWeather import OpenWeather
import datetime

zipcode = "92697"
ccode = "US"
apikey = "3e6e18ffbc23e0c8919d6484aafc5da8"

open_weather = OpenWeather(zipcode, ccode)
open_weather.set_apikey(apikey)
open_weather.load_data()

print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
print(f"The current weather for {zipcode} is {open_weather.description}")
print(f"The current humidity for {zipcode} is {open_weather.humidity}%")
print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")