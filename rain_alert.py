import requests
from twilio.rest import Client
import os


LAT = 10.823099
LNG = 106.629662

OWM_API_KEY = os.environ["API_KEY"]
OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"

account_sid = os.environ["ACCOUNT_SID"]
auth_token = os.environ["AUTH_TOKEN"]

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
            body="It's going to rain today so bring your umbrella",
            from_= "+16205778341",
            to= "+87379925451"
        )

