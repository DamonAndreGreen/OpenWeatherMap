import requests, json 
from bottle import route, run, template
import datetime #Using this import to convert the UNIX timestamp from openweathermap to the regular date and time format

# Apply an account at openweathermap.org.
@route('/')
def index(): # The function
  city = input("Please enter city name : ") 
  apikey = 'b0906263b97835f4e5422443cc5606eb' #My apikey
  url = template('http://api.openweathermap.org/data/2.5/weather?q={{city}}&units=imperial&appid={{apikey}}', #Converting the units from Kelvins to Fahrenheit
       city=city, apikey=apikey)
  response = requests.get(url) 
  dict = response.json() # convert json data to python dictionary
  response = requests.get(url)
  x = response.json()  #This is to extract the temperature and humidity field
  y = x["main"] #Variable set up   
  current_temperature = y["temp"] 
  current_pressure = y["pressure"] 
  current_humidiy = y["humidity"]
  #The three above is apart of the main category. Just plugging them up so later it can display once code runs
  p = x["dt"]
  current_time =  p
  #Time is apart of dt. Here I'm just plugging in time as P to display the time
  
  # o = x["timezone"]
  #current_zone = o
  # I originally was including timezone but I didn't like how the convert look and made the results more confusing
  # store the value of "weather" 
  # key in variable z 
  d = x["weather"] 
  weather_description = d[0]["description"] 
  #from Weather I'm getting the description
  
  # print the following  
  print("In " + str(city) +
        "\nThe temperature is " +
                  str(round(current_temperature,1)) + " degrees fahrenheit" +
        "\nThe humidity percentage is " +
                  str(round(current_humidiy,1)) + "%" +
        "\nCurrently the weather is showing " +
                  str(weather_description) +
        "\nThe date and time is "+
                  str(datetime.datetime.fromtimestamp(
        int(current_time)
    ).strftime('%Y-%m-%d %H:%M:%S')))
  
  # return str(dict) The original Json. Disabled as I extracted the data from it and printed the data that needed to be printed.
index()
run(host='localhost', port=80, debug=True, reloader=True)

