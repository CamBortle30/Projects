import requests # this library will help you make your requests
import json # this library will help parse api data in json format 

# below we will define components of the URL to simplify the request 
city = input("Enter a City: ")
#lat = input("Enter Latitude: ")
#long = input("Enter Longitude: ")
apiKey = "a32cec8ffdec3eff19c8e73e43c7e026"

#completeRequest = "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+long+"&appid="+apiKey
completeRequest = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid="+apiKey+"&units=imperial"

# when making an API call, we can add parameters to the endpoint. An endpoint is just the exact data we are requesting from the server, and the more parameters, the more specific the data that is returned will be
# for example, the api we're using to make this request, we can filter for 'mode' - which is the data structure returned (json is default), and even 'units' - such as metric vs imperial

# below we will strucuture the requests
weatherEndpoint = requests.get(completeRequest)
if weatherEndpoint.status_code != 200:
    print("Error Occured.")
else:
    weatherEndpointData = weatherEndpoint.json()
    #parseEndpoint = json.loads(weatherEndpointData)
    #print(parseEndpoint) hopefully, this will print some data about the location we inserted for latitude and longitudeb
    weather = weatherEndpointData['weather'][0]['description']
    temp = weatherEndpointData['main']['temp']
    feelsLike = weatherEndpointData['main']['feels_like']
    humidity = weatherEndpointData['main']['humidity']
    windSpeed = weatherEndpointData['wind']['speed']
    print("Weather:", weather)
    print("Temperature:", temp, "degrees farenheit")
    print("Feels Like:", feelsLike, "degrees farenheit")
    print("Humidity:", humidity)
    print("Wind Speed:", windSpeed, "MPH")