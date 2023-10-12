# lastfm.py

# Starter code for assignment 4 in ICS 32 Programming with Software Libraries in Python
import urllib, json
import datetime
from urllib import request, error
from WebAPI import WebAPI

class LastFM(WebAPI):
    '''def __init__(self, artist, album):
        self.artist = artist
        self.album = album'''

    def load_data(self) -> None:
        '''
        Calls the web api using the required values and stores the response in class data attributes.     
        '''
        response = None
        r_obj = None
        artist = "keshi"
        album = "bandaids"      
        url_to_download = f"http://ws.audioscrobbler.com/2.0/?method=album.getinfo&api_key={self.apikey}&artist={artist}&album={album}&format=json"

        try:
            response = urllib.request.urlopen(url_to_download)
            json_results = response.read()
            r_obj = json.loads(json_results)

        except urllib.error.HTTPError as e:
            print('Failed to download contents of URL')
            print('Status code: {}'.format(e.code))
        
        else:
            self.listeners = r_obj['album']['listeners']
            self.playcount = r_obj['album']['playcount']
            self.tracks = len(r_obj['album']['tracks']['track'])

        finally:
            if response != None:
                response.close()
        
        return r_obj
        #TODO: use the apikey data attribute and the urllib module to request data from the web api. See sample code at the begining of Part 1 for a hint.
        #TODO: assign the necessary response data to the required class data attributes
    def transclude(self, message:str) -> str: ## amount of total listeners based on album
        if '@lastfm' in message:
            new = message.split("@lastfm")
            x = self.listeners
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

# NAME Andrew Z. Hos
# EMAIL andrewzh@uci.edu
# STUDENT ID 11211101
