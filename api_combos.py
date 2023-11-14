import requests
import json
import pandas as pd
from utils import latitude as l 


# function will return some weather data for a given zip code
def getWeatherOutput (ZipString):
	weatherUrl = "https://us-weather-by-zip-code.p.rapidapi.com/getweatherzipcode"

	querystring = {"zip": ZipString}

	headers = {
		"X-RapidAPI-Key": l.xrakey,
		"X-RapidAPI-Host": "us-weather-by-zip-code.p.rapidapi.com"
	}

	response = requests.get(weatherUrl, headers=headers, params=querystring)

	return response.json()
	

# function will return some housing data for a given zip code
def getHousingOutput(ZipString) : 
	url = "https://api.rentcast.io/v1/markets?"

	headers = {
		"accept": "application/json",
		"X-Api-Key": l.rcakey
	}

	housingParams = {
		"zipCode" : ZipString, 
		"historyRange" : '6'
	}

	response = requests.get(url, headers=headers, params = housingParams)

	return response.json()

# try to implement a slightly better output, perhaps by converting dictionary to tables
def exportPrettyTable(dictionary, zipcodes):
	# df = pd.DataFrame(dictionary, columns = ['City', 'AQI', 'Wind (MPH)', 'averageRent', 'totalListings'], 
				#    index=[zipcodes[0],zipcodes[1], zipcodes[2], zipcodes[3], zipcodes[4]])
	# df = pd.DataFrame.from_dict(dictionary, index= ['City', 'AQI', 'Wind (MPH)', 'averageRent', 'totalListings'])
	
	df = pd.DataFrame.from_dict(dictionary)
	return df

def main(): 
	zip_prompt = input("Please enter a comma seperated list of zip codes you would like some information for: \n")
	zipcodes = zip_prompt.split(',')
	
	resultsDict = {}
	for zip in zipcodes: 
		ZipString = str(zip)
		weatherOutput = getWeatherOutput(ZipString)
		housingOutput = getHousingOutput(ZipString)
		resultsDict[zip] = [
					 weatherOutput['City'], 
					 weatherOutput['AirQualityIndex'], 
					 weatherOutput['WindMPH'], 
					 housingOutput['rentalData']['averageRent'], 
					 housingOutput['rentalData']['totalListings']
		]

	print ("Below is a output of information for the provided zip codes")
	print (exportPrettyTable(resultsDict, zipcodes))

if __name__ == "__main__":
    main()



