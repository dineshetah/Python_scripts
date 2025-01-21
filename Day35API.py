# API Key, Authentication, Environment variable and Sending SMS 

# API Authentication 
#https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
# https://openweathermap.org
import requests


#using API Keys to Autheniticate and Get the Weather from openWeatherMap

Own_endingpoint = "https://api.openweathermap.org/data/2.5/weather?"

api_key = "6ed7e602abaa96d9ee2dcf38c429c23b"
#api_key= "69f04e46130569b159c2761a9d9e664d2"

weather_params = {
    "lat":44.34 ,
    "long":10.99 ,
    "appid": api_key,
    "cnt": 4, 
}
response = requests.get(Own_endingpoint, params=weather_params)
#print(response.status_code) # here get a code 401
weather_data = response.json()


# Challenge - check if it will rain in the next 12 hours 

print(weather_data["list"][0]["weather"][0]["id"])

# Here defined condition 
will_rain = False

for hour_data in weather_data["list"]:
    print(hour_data["weather "][0]["id"])
    condition_code = hour_data["weather "][0]["id"]
    if int(condition_code) < 700:
        print("Bring an umbrella.")
        will_rain = True
if will_rain:
    print("Bring an umbrella.")

    client = Client(account_sid, auth_token)
    message = client.messages \
            .create(
                body ="Join Earth's mightiest heroes. Like Kevin Bacon.",
                from = "9439970162",
                to = "+8077259313"
            )
    print(message.status)



# Use PythonAnyWhere to Automate the Python Script 




# Get your latitude and longitude from latlog.net 
# Make a request to the forecast API using the requests module 
# Print out the HTTP status code that you get back. 
# Print the response to the console.
# Copy- paste the response to an online JSON viewer (e.g., jsonviewer.stack.hu)
# Locate the weather id and description for each forecast 

# Note : for more viewer json data https://jsonviewer.stack.hu