from LastFM import LastFM
import datetime

artist = "keshi"
album = "bandaids"
apikey = "07808c7623679f2fce1fbbb12aab3cbb"

last_fm = LastFM(artist, album)
last_fm.set_apikey(apikey)
one = last_fm.load_data()

'''print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
print(f"The current weather for {zipcode} is {open_weather.description}")
print(f"The current humidity for {zipcode} is {open_weather.humidity}%")
print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")'''
print(f"The album {last_fm.album} by {last_fm.artist} has be listened to by {last_fm.listeners} people and played {last_fm.playcount} times!")
print(f"The album {last_fm.album} by {last_fm.artist} has {last_fm.tracks} songs")
{'album': 
    {'artist': 'keshi', 
    'mbid': '9657d5a0-7fbb-44bb-826c-3840599489ce', 
    'tags': {'tag': 
        [{'url': 'https://www.last.fm/tag/villain+loves+keshi', 'name': 'villain loves keshi'}, 
        {'url': 'https://www.last.fm/tag/lo-fi', 'name': 'lo-fi'}, 
        {'url': 'https://www.last.fm/tag/alternative', 'name': 'alternative'}, 
        {'url': 'https://www.last.fm/tag/alternative+rock', 'name': 'alternative rock'}, 
        {'url': 'https://www.last.fm/tag/rnb', 'name': 'rnb'}]}, 
    'name': 'bandaids', 
    'image': [{'size': 'small', '#text': 'https://lastfm.freetls.fastly.net/i/u/34s/29a0e7984be76ad9bd0b047f7de2242f.jpg'}, 
        {'size': 'medium', '#text': 'https://lastfm.freetls.fastly.net/i/u/64s/29a0e7984be76ad9bd0b047f7de2242f.jpg'}, 
        {'size': 'large', '#text': 'https://lastfm.freetls.fastly.net/i/u/174s/29a0e7984be76ad9bd0b047f7de2242f.jpg'}, 
        {'size': 'extralarge', '#text': 'https://lastfm.freetls.fastly.net/i/u/300x300/29a0e7984be76ad9bd0b047f7de2242f.jpg'}, 
        {'size': 'mega', '#text': 'https://lastfm.freetls.fastly.net/i/u/300x300/29a0e7984be76ad9bd0b047f7de2242f.jpg'}, 
        {'size': '', '#text': 'https://lastfm.freetls.fastly.net/i/u/300x300/29a0e7984be76ad9bd0b047f7de2242f.jpg'}], 
    'tracks': {'track': 
        [{'streamable': {'fulltrack': '0', '#text': '0'}, 'duration': 206, 'url': 'https://www.last.fm/music/keshi/bandaids/less+of+you', 'name': 'less of you', '@attr': {'rank': 1}, 'artist': {'url': 'https://www.last.fm/music/keshi', 'name': 'keshi', 'mbid': 'ee74db56-c264-4c23-9504-29e2d8078f36'}}, 
        {'streamable': {'fulltrack': '0', '#text': '0'}, 'duration': 168, 'url': 'https://www.last.fm/music/keshi/bandaids/alright', 'name': 'alright', '@attr': {'rank': 2}, 'artist': {'url': 'https://www.last.fm/music/keshi', 'name': 'keshi', 'mbid': 'ee74db56-c264-4c23-9504-29e2d8078f36'}}, 
        {'streamable': {'fulltrack': '0', '#text': '0'}, 'duration': 180, 'url': 'https://www.last.fm/music/keshi/bandaids/blue', 'name': 'blue', '@attr': {'rank': 3}, 'artist': {'url': 'https://www.last.fm/music/keshi', 'name': 'keshi', 'mbid': 'ee74db56-c264-4c23-9504-29e2d8078f36'}}, 
        {'streamable': {'fulltrack': '0', '#text': '0'}, 'duration': 195, 'url': 'https://www.last.fm/music/keshi/bandaids/right+here', 'name': 'right here', '@attr': {'rank': 4}, 'artist': {'url': 'https://www.last.fm/music/keshi', 'name': 'keshi', 'mbid': 'ee74db56-c264-4c23-9504-29e2d8078f36'}}, 
        {'streamable': {'fulltrack': '0', '#text': '0'}, 'duration': 215, 'url': 'https://www.last.fm/music/keshi/bandaids/bandaids', 'name': 'bandaids', '@attr': {'rank': 5}, 'artist': {'url': 'https://www.last.fm/music/keshi', 'name': 'keshi', 'mbid': 'ee74db56-c264-4c23-9504-29e2d8078f36'}}]}, 
    'listeners': '110577', 
    'playcount': '2467592', 
    'url': 'https://www.last.fm/music/keshi/bandaids'}}