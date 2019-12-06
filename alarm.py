#!/usr/bin/env python
# Smart Alarm 

import requests, json

# Weather API 
# Enter your API key here for Weather API
api_key = "d89bcf10c5fa1e1c1288adde83f5ed64"

# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# City name
city_name = "Atlanta"

# Complete url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name

# get method of requests module
# return response object
response = requests.get(complete_url)

# json method of response object
# convert json format data into
# python format data
weather = response.json()

# converting weather into farenheit
min_temp = weather['main']['temp_min']
max_temp = weather['main']['temp_max']

far_min = round((min_temp - 273.15) * 9 / 5 + 32)
far_max = round((max_temp - 273.15) * 9 / 5 + 32)
print(far_min, far_max)

# Checking the weather type
weather_type = weather['weather'][0]['main']

# Checking today's date

from time import sleep
from datetime import datetime, date
import calendar
import os
from subprocess import call


def findDay(date):
	born = date.weekday()
	return (calendar.day_name[born])

alarms = {'Monday':'0700','Tuesday':'0700','Wednesday':'0700','Thursday':'0700','Friday':'0010','Saturday':'0900', 'Sunday':'0900'}

# Quotes
quotes = ['I would rather die of passion than of boredom','A person who never made a mistake never tried anything new',
          'If you fell down yesterday, stand up today','No man has a good enough memory to be a successful liar',
          'Today is the tomorrow you worried about yesterday','Light travels faster than sound. This is why some people appear bright until you hear them speak.']

from random import randint


# Alarm Sound Set Up
import pygame
pygame.mixer.init()
pygame.mixer.music.load("alarm_sound.mp3")

# Setting up audio output
import pyttsx3
engine = pyttsx3.init()

# Alarm Function 
while True:
	date = date.today()
	today_date = findDay(date)
	today_alarm_hour = alarms[today_date][0:2]
	today_alarm_min = alarms[today_date][2:]
	now = datetime.now()
	hournow = now.hour
	minnow = now.minute

        morning_statement = "Today is" + today_date
        min_temp = "The minimum temperature is" + str(far_min) + " fahrenheit."
        max_temp = "The maximum temperature is " + str(far_max) + "fahrenheit."

        weather_statement = "The weather today is" + weather_type

        
	if int(hournow) == int(today_alarm_hour) and int(minnow) == int(today_alarm_min):
            pygame.mixer.music.play()

            sleep(14)
            engine.setProperty('rate',200)
            engine.say(morning_statement)
            engine.runAndWait()
            engine.say(min_temp)
            engine.runAndWait()
            engine.say(max_temp)
            engine.runAndWait()
            engine.say(weather_statement)
            engine.runAndWait()
            
            if weather_type == 'Rain':
                engine.say("It is raining today. Bring an umbrella")
                engine.runAndWait()

            engine.say("Here is today's motivational quote")
            engine.runAndWait()

            engine.setProperty('rate',175)
            engine.say(quotes[randint(0,5)])
            engine.runAndWait()

            sleep(2)

            engine.say("Have a nice day")
            engine.runAndWait()
            
            break
    

	






