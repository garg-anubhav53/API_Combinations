import requests
import json

WeatherUrl = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"

querystring = {"zip":"94111"}

headers = {
	"X-RapidAPI-Key": "6795ba421bmsh8f363c73274493bp14dbb7jsn03a28699e5d0",
	"X-RapidAPI-Host": "us-weather-by-zip-code.p.rapidapi.com"
}

response = requests.get(WeatherURL, headers=headers, params=querystring)

print(response.json())

# data = json.loads(response.json().toString())

# print(data['city'])

print(response.json()['City'])