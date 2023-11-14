import requests
import json

zip = 94111
ZipString = str(zip)


# weatherUrl = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"

# querystring = {"zip": ZipString}

# headers = {
# 	"X-RapidAPI-Key": "6795ba421bmsh8f363c73274493bp14dbb7jsn03a28699e5d0",
# 	"X-RapidAPI-Host": "us-weather-by-zip-code.p.rapidapi.com"
# }

# response = requests.get(weatherUrl, headers=headers, params=querystring)

# print(response.json())

# print(response.json()['City'])

url = "https://api.rentcast.io/v1/markets?"

headers = {
    "accept": "application/json",
    "X-Api-Key": "7bb22ecba95544d4bab9191475a5bd92"
}

housingParams = {
    "zipCode" : zip, 
    "historyRange" : '6'
}

response = requests.get(url, headers=headers, params = housingParams)

print (response.json())