import requests
import os
from dotenv import load_dotenv

load_dotenv()

#env variable
telegram_bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")
owm_api_key = os.environ.get("OWM_API_KEY")
my_lat = os.environ.get("CITY_LATITUDE")
my_lon = os.environ.get("CITY_LONGITUDE")

def telegram_bot_sendtext(bot_message):
    bot_token = str(telegram_bot_token)
    bot_chatID = str(telegram_chat_id)
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

# https://openweathermap.org/forecast5
# https://api.openweathermap.org/data/2.5/weather?q=Taipei,TW&appid=5f3b656cf385bbce00b465d340a4ca26
# api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API key}

OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
weather_params = {
    "lat": my_lat,
    "lon": my_lon,
    "cnt": 4,
    "appid": owm_api_key,
}

# weather_data = {'cod': '200', 'message': 0, 'cnt': 4, 'list': [{'dt': 1712113200, 'main': {'temp': 284.18, 'feels_like': 282.23, 'temp_min': 284.18, 'temp_max': 284.18, 'pressure': 1020, 'sea_level': 1020, 'grnd_level': 965, 'humidity': 34, 'temp_kf': 0}, 'weather': [{'id': 602, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 33}, 'wind': {'speed': 3.13, 'deg': 103, 'gust': 2.95}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-04-03 03:00:00'}, {'dt': 1712124000, 'main': {'temp': 285.23, 'feels_like': 283.28, 'temp_min': 285.23, 'temp_max': 287.33, 'pressure': 1019, 'sea_level': 1019, 'grnd_level': 964, 'humidity': 30, 'temp_kf': -2.1}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 39}, 'wind': {'speed': 1.54, 'deg': 49, 'gust': 1.29}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-04-03 06:00:00'}, {'dt': 1712134800, 'main': {'temp': 287.67, 'feels_like': 285.78, 'temp_min': 287.67, 'temp_max': 289.41, 'pressure': 1018, 'sea_level': 1018, 'grnd_level': 963, 'humidity': 23, 'temp_kf': -1.74}, 'weather': [{'id': 802, 'main': 'Clouds', 'description': 'scattered clouds', 'icon': '03d'}], 'clouds': {'all': 26}, 'wind': {'speed': 1.68, 'deg': 4, 'gust': 1.69}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-04-03 09:00:00'}, {'dt': 1712145600, 'main': {'temp': 289.23, 'feels_like': 287.42, 'temp_min': 289.23, 'temp_max': 289.23, 'pressure': 1017, 'sea_level': 1017, 'grnd_level': 963, 'humidity': 20, 'temp_kf': 0}, 'weather': [{'id': 803, 'main': 'Clouds', 'description': 'broken clouds', 'icon': '04d'}], 'clouds': {'all': 61}, 'wind': {'speed': 2.46, 'deg': 346, 'gust': 2.56}, 'visibility': 10000, 'pop': 0, 'sys': {'pod': 'd'}, 'dt_txt': '2024-04-03 12:00:00'}], 'city': {'id': 1529085, 'name': 'Wujiaqu', 'coord': {'lat': 44.51, 'lon': 88.01}, 'country': 'CN', 'population': 1000, 'timezone': 28800, 'sunrise': 1712101504, 'sunset': 1712147820}}
response = requests.get(OWM_endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(response.status_code)

# online json viewer: https://jsonviewer.stack.hu/#google_vignette
# weather condition code https://openweathermap.org/forecast5#list
expect_to_rain = False

for hour_data in weather_data["list"]:
    weather_condition_code = hour_data["weather"][0]["id"]
    # if any time point weather condition code is less than 700, then print bring an umbrella
    # print(weather_condition_code)
    if weather_condition_code < 700:
        expect_to_rain = True

if expect_to_rain:
    telegram_bot_sendtext("It's going to rain today. Remember to bring an ☔️")
else:
    telegram_bot_sendtext("It wont rain tomorrow️")

