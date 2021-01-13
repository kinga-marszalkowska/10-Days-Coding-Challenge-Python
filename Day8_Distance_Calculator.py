import requests
import geocoder
from math import sqrt, cos, pi


def get_lat_long(address):
    url = "https://trueway-geocoding.p.rapidapi.com/Geocode"

    querystring = {"address": address, "language": "en"}

    headers = {
        'x-rapidapi-key': "your_apikey_goes_here",
        'x-rapidapi-host': "trueway-geocoding.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    return response.json()["results"][0]["location"]["lat"], response.json()["results"][0]["location"]["lng"]


def calculate_geo_distance(x1, x2, y1, y2):
    return sqrt(pow((x2 - x1), 2) + pow((cos((x1 * pi) / 180) * (y2 - y1)), 2)) * (40075.704/360)


origin = geocoder.ip('me').latlng
destination = get_lat_long("505 Howard St, San Francisco")

print("{0:.2f}".format
      (calculate_geo_distance(origin[0], destination[0], origin[1], destination[1])), "km")



