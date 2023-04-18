import requests

url = requests.get("https://api.weatherbit.io/v2.0/current/airquality?lat=35.7721&lon=-78.63861&key=API_KEY").text


print(url)