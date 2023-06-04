#make a weather app that tells you the weather of a city by using api of openweathermap.org use command line for output
import requests
import json
import sys
import os
import time
import datetime
print("\033[1;33mWelocome to the Weather Report App you can check the weather of any city in the world")
print("\033[1;30m-------------------------------------------------")
test=input("Press Enter to continue...")
resp=input("\033[1;34m Do you want to Enter a new API key? (y/n)")
if(resp=='y'):
    import config
else:
    pass
check = os.path.exists("api/api_key.txt")
if check == False:
    print("\033[1;31m API key not found .")
    sys.exit()
else:
    pass
# Take the input of API key
# api_key=input("Enter the API key: ")
#fetch api key from file 
api_key=""
with open("api/api_key.txt", "r") as f:
    api_key=f.read()
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"
resp2=True;
while(resp2):
    
    city_name = input("\033[1;33mEnter city name : ")
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name
    response = requests.get(complete_url)
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        current_temperature = y["temp"]
        current_pressure = y["pressure"]
        current_humidiy = y["humidity"]
        z = x["weather"]
        weather_description = z[0]["description"]
        #make the temperature in celcius
        current_temperature_int=int(current_temperature)
        current_temperature_int = current_temperature_int - 273.15
        #round off temperature to 2 decimal places
        current_temperature_int = round(current_temperature_int,2)
        current_temperature = str(current_temperature_int)
        #make a variable that fetch the current time and date of a place
        current_time = datetime.datetime.now()
        #print the data
        #format the current time in a am / pm notation
        current_time = current_time.strftime("%I:%M %p")
        print("\033[1;30m")
        print("🌍 City = " + city_name + "\n🕒 Date and Time = " + str(current_time))
        
        print("🌡️ Temperature = " +
              str(current_temperature) + " degree Celcius" +
              "\n🌍 Atmospheric pressure = " +
            str(current_pressure) + "hPa"
            "\n💧 Humidity = " +
            str(current_humidiy) + " %"
            "\n❄️  Description = " +
             str(weather_description))
    else:   
        print(" City Not Found ")
    print("\n \033[1;30m-------------------------------------------------")
    resp2=input("\n \033[1;31m Do you want to check the weather of another city? (y/n) : ")
    if(resp2=='y'):
        pass
    else:
        break
print("\033[1;30m")

    

    
    
        