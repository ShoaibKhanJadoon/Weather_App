import requests

city = input("write your city name?: ")

# Fetch the  data
response = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}"
)

# Parse the JSON response
data = response.json()
print(f"""
Weather: {data['weather'][0]['description']}
Temperature: {data['main']['temp']}
Feels like: {data['main']['feels_like']}
Humidity: {data['main']['humidity']}
pressure: {data[ 'main']['pressure']}
""")
