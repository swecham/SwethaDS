# File: Chamala_week12_Final_Project.py
# Author: Swetha Chamala
# Date: 11/14/19
# Course: DSC510 - Introduction to programming
# Description: Weather program application in Python
import requests


def main():
    while True:
        weather_check = input("Would you like to check current weather? Please enter Y or N\n").lower()
        if weather_check == 'y':
            user_input = input('Select A to input city name or B to input Zip code:\n').lower()
            if user_input == "a":
                data = city()
                parsed = data.json()
                try:
                    data.raise_for_status()
                    print("Connection established")
                    parse_weather(parsed)
                except requests.exceptions.HTTPError:
                    print("Error: input not valid")  # check for connection errors
                    print("Please enter a valid input")
            elif user_input == 'b':
                data = zip_code()
                parsed = data.json()
                try:
                    data.raise_for_status()
                    print("Connection established")
                    parse_weather(parsed)
                except requests.exceptions.HTTPError:
                    print("Error: input not valid")
                    print("Please enter a valid zip")
            else:
                print("Wrong entry. Please enter a valid input")
        elif weather_check == 'n':
            print("Thank you for using Open Weather Map")
            break
        else:
            print("Enter valid response")


def city():
    while True:
        city_name = input("Enter name of city:\n").lower()
        if all(x.isalpha() or x.isspace() for x in city_name):
            base_url = 'http://api.openweathermap.org/data/2.5/weather?q='  # can also use single line url with api key included in it using {}format to insert city name.
            api_key = ",us&appid=eab064a7469dae20e3026d4e7dae1a54"  # included ",us" to only limit the search to cities in US
            units = '&units=imperial'  # to convert temperature to Fahrenheit
            final_url = base_url + city_name + api_key + units
            response_r = requests.get(final_url)
            return response_r
        else:
            print("enter only alphabets")


def zip_code():
    while True:
        postal_code = input("Enter Zip Code:\n")
        if postal_code.isdigit():
            api_key = ",us&appid=eab064a7469dae20e3026d4e7dae1a54"
            units = '&units=imperial'
            base_url = 'https://api.openweathermap.org/data/2.5/weather?zip='
            final_url = base_url + str(postal_code) + api_key + units
            response_r = requests.get(final_url)
            return response_r
        else:
            print("enter only numbers")


def parse_weather(parsed):
    print('---------------------------------------')
    print('Requested location: {}'.format(parsed['name']))
    print('Current temperature: {} F '.format(parsed['main']['temp']))
    print('Max temperature: {} F, Min temperature: {} F'.format(parsed['main']['temp_max'], parsed['main']['temp_min']))
    print('Wind Speed: {}miles/hr, Degree: {}'.format(parsed['wind']['speed'], parsed['wind']['deg']))
    print('Humidity: {}%'.format(parsed['main']['humidity']))
    print('Pressure: {} hpa'.format(parsed['main']['pressure']))
    print('Longitude = {}'.format(parsed['coord']['lon']))
    print('Latitude = {}'.format(parsed['coord']['lat']))
    print('---------------------------------------')


if __name__ == '__main__':
    main()
