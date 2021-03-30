import json
import math
import urllib.request
from django import forms
from crispy_forms.helper import FormHelper

#Class to process the coordinates of the user
class BicingForm(forms.Form):
    
    #User location form
    lat = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'readonly'}), required = False)
    long = forms.FloatField(widget=forms.TextInput(attrs={'readonly':'readonly'}), required = False)

    #Measures the distance between the user and the stations around
    def distance(self, latUser, longUser, latStation, longStation):
       # Constants
        # Grados a Radianes
        degtorad = 0.01745329
        # Radianes a Grados
        radtodeg = 57.29577951
        dlong = (longUser - longStation)
        dvalue = (math.sin(latUser * degtorad) * math.sin(latStation * degtorad)) + (
                math.cos(latUser * degtorad) * math.cos(latStation * degtorad) * math.cos(dlong * degtorad))
        dd = math.acos(dvalue) * radtodeg
        # Grados a millas In case you need the info in Miles
        #miles = round(dd * 69.16)
        # Grados a kilómetros
        kms = round(dd * 111.302, 2)
        return kms
    #Search for the bicycle stations around the user within 450 mts using the Service Api's
    def arrayStations(self, latUser, longUser):
     print(latUser)
     #Api info stations Data
     json_url = urllib.request.urlopen("https://api.bsmsa.eu/ext/api/bsm/gbfs/v2/en/station_information")
     data = json.loads(json_url.read())
     #Data with available bikes and docks in real time
     json_url_status = urllib.request.urlopen("https://api.bsmsa.eu/ext/api/bsm/gbfs/v2/en/station_status")
     data_status= json.loads(json_url_status.read())
     stationsinfo=[]
     stationsinfo.append({"latUser": latUser, "longUser": longUser})
     for x in data['data']['stations']:
            for y in data_status['data']['stations']:
             if y['station_id'] == x['station_id']:
              if self.distance(latUser, longUser, x['lat'], x['lon']) <= 0.45:
                print(x['station_id'])
                info = {
                    "station_id": x['station_id'],
                    "bicycles_available": y['num_bikes_available'],
                    "docks_available": y['num_docks_available'],
                    "latitude":  x['lat'],
                    "longitude": x['lon']
                }
                stationsinfo.append(info)
     return stationsinfo
    