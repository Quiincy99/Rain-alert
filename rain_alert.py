from email import message
from http import client
from urllib import response
import requests
from twilio.rest import Client


LAT = 29.716620
LNG = -107.808810

OWM_API_KEY = "950844bf0c2ae88923aafee8f0d54e43"
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = "AC1b41dd98623c79e0a2c1784ead1c8d4c"
auth_token = "3d3bfdc86746817ac864cb496473cbad"

weather_params = {
    "lat": LAT,
    "lon": LNG,
    "appid": OWM_API_KEY,
    "exclude": "current, minutely, daily"
}

response  = requests.get(OWM_URL, params= weather_params)

weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain",
            from_= "+16205778341",
            to= "+87379925451"
        )
