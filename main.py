account_sid = 'ACd1c87dcc5cb23d898de5061f5f04f1b9'
auth_token = '90a8ca0903f02c0fd9130e32408eafa5'


api_key = os.environ.get("OWM_API_KEY")
auth_token = os.environ.get("AUTH_TOKEN")
telefone = os.environ.get("Telefone")


import os
import requests
from twilio.rest import Client
client = Client(account_sid, auth_token)
print(api_key)
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
weather_params = {
    "lat": -22.908333,
    "lon": -43.196388,
    "appid":api_key,
    "exclude":"",
}

response = requests.get(api_key, params = weather_params)

print(response.status_code)
weather_data = response.json()["weather"]
print(weather_data)

for el in weather_data:
    if el["id"] < 700:
        message = client.messages.create(
          from_='whatsapp:+14155238886',
          body='Leve um guarda chuva!',
          to=telefone
        )

        print(message.sid)

    else:
        message = client.messages.create(
            from_='whatsapp:+14155238886',
            body='Não precisa levar um guarda chuva!',
            to=telefone
        )
        print(message.sid)
