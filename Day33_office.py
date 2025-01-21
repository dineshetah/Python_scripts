# import requests


# #https://sunrise-sunset.org/api
# my_lat =28.447720
# my_lon = 77.524570

# # Here create dictionary 
# parameters = {
# "lat" :my_lat, 
# "Ing":my_lon,
# "formatted":0,
# }

# url ="https://api.sunrise-sunset.org/json"
# response = requests.get(url,params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"]
# sunset = data["results"]["sunset"]
# print(sunrise)
# #print(data)


import requests
from datetime import datetime 
import smtplib
import time
my_lat = 28.447720
my_lon = 77.524570
MY_EMAIL = "dinesh.etah457@gmail.com"
MY_PASSWORD = "rsogimolfaikckyb"
parameters = {
    "lat": my_lat,
    "lng": my_lon,
    "formatted": 0,  # this is dict key value added here for formatted purposes 
}
def is_iss_overhead():
    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url, params=parameters)
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
 # Your position is within +5 or -5 degrees of the iss position.
    #if 46 <= iss_latitude<=56
    if my_lat-5<= iss_latitude<= my_lat +5 and my_lon-5<= iss_latitude<= my_lon +5:
        return True
def is_night():
    url = "https://api.sunrise-sunset.org/json"
    response = requests.get(url, params=parameters)
    parameters = {
    "lat": my_lat,
    "lng": my_lon,
    "formatted": 0,  # this is dict key value added here for formatted purposes 
}
    try:
        response.raise_for_status()
        data = response.json()
            # sunrise = data["results"]["sunrise"]
            # sunset = data["results"]["sunset"]
            #time_split = sunrise.split("T")[1]  # here the separted time 

        # iss_latitude = float(data["iss_position"]["latitude"])
        # iss_longitude = float(data["iss_position"]["longitude"])

        sunrise=data["results"]["sunrise"].split("T")[1].split(":")[0]  # here used another split (:) for indexing 
        sunset =data["results"]["sunset"].split("T")[1].split(":")[0]
            #print(time_split)
        print("Sunrise:", sunrise )
        print("Sunset:", sunset)
    except requests.exceptions.HTTPError as err:
         print(err)
    time_now = datetime.now().hour
    if time_now >= sunset or time_now <=sunrise:
         return True
         print(time_now)
while True:
#https://www.w3schools.com/python/ref_string_split.asp
# Send me an email to tell me to look up
    if is_iss_overhead() and is_night:

        connection = smtplib.SMTP("smtp.gmail.com")      # here create a object SMTP class
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()     # TLS stands for  Transport Layer Security 
            connection.login(user=MY_EMAIL, password= MY_PASSWORD)
            connection.sendmail(
                from_addr= MY_EMAIL, 
                to_addrs="sudeepyadav19082019@gmail.com", 
                msg ="Subject:Hello\n\nThis is the body of my email.")