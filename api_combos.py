import requests
import json

# function will return some weather data for a given zip code
def getWeatherOutput (ZipString):
	weatherUrl = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"

	querystring = {"zip": ZipString}

	headers = {
		"X-RapidAPI-Key": "6795ba421bmsh8f363c73274493bp14dbb7jsn03a28699e5d0",
		"X-RapidAPI-Host": "us-weather-by-zip-code.p.rapidapi.com"
	}

	response = requests.get(weatherUrl, headers=headers, params=querystring)

	print(response.json())

	print(response.json()['City'])
	return response.json()
	

# function will return some housing data for a given zip code
def getHousingOutput(ZipString) : 
	url = "https://api.rentcast.io/v1/markets?"

	headers = {
		"accept": "application/json",
		"X-Api-Key": "7bb22ecba95544d4bab9191475a5bd92"
	}

	housingParams = {
		"zipCode" : ZipString, 
		"historyRange" : '6'
	}

	response = requests.get(url, headers=headers, params = housingParams)

	print (response.json())
	return response.json()


def main(): 
	zipcodes = [94111, 46077, 46113, 52227, 49501]
	resultsDict = []
	for zip in zipcodes: 
		ZipString = str(zip)
		weatherOutput = getWeatherOutput(ZipString)
		housingOutput = getHousingOutput(ZipString)
		resultsDict.append(zip, 
					 weatherOutput['City'], 
					 weatherOutput['AirQualityIndex'], 
					 weatherOutput['WindMPH'], 
					 housingOutput['rentalData']['averageRent'], 
					 housingOutput['rentalData']['totalListings'])
	
	print("This is the result of the full dict: ", resultsDict)

if __name__ == "__main__":
    main()



