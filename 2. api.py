import requests
import datetime

url = "https://community-open-weather-map.p.rapidapi.com/weather"
city = input("Give a city name: ")

querystring = {"q": city, "units": "\"metric\""}

headers = {
    #todo change rapidapi-key to here_goes_your_apikey
    'x-rapidapi-key': "42f351c64dmsh7d8251944f56389p12143ajsn6d62d296eba7",
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

if response.status_code == 200:
    response_json = response.json()

    #now = datetime.datetime.now()
    # current_time = now.strftime("%H:%M:%S")
    # print(current_time)


    # print("FULL RESPONSE: ")
    # print(response_json)
    # print("-----------")
    weather_data = response_json["weather"]
    print("weather: " + weather_data[0]['description'])
    temp = response_json["main"]
    print("temperature: " + str(temp['temp']))
    print("feels like: " + str(temp['feels_like']))
    print("pressure: " + str(temp['pressure']))
    clouds = response_json["clouds"]
    print("% clouds: " + str(clouds['all']))
    sys = response_json["sys"]
    print("sunset at: " + str(sys['sunset']))
    
    UTC_now = datetime.datetime.utcnow()
    shift_in_s_from_UTC = response_json['timezone']
    print(UTC_now + datetime.timedelta(0, shift_in_s_from_UTC))





elif response.status_code == 404:
    print("Check the spelling of city name")
elif response.status_code == 500:
    print("Sorry, it's our fault. Come back later.")