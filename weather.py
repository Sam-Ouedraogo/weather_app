''' Programmer: Samuel W. Ouedraogo
    Last edit: 04/15/2023
'''

import requests
from dotenv import load_dotenv
import os
from pprint import pprint


load_dotenv()

def get_weather():
    print('\n*** City lookup ***\n')

    city = input("Please enter a city name:\t")


    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=imperial'

    # response object is captured in the weather_data variable in JSON format
    weather_data = requests.get(request_url).json()
    
    #pprint(weather_data)
    
    print(f"It is currently {weather_data["main"]["temp"]} in {weather_data["name"]}, but it feels like {weather_data["main"]["feels_like"]}.")
    

if __name__ == "__main__":
        
    get_weather()