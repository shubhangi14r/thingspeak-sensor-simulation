import requests
import random
import time


API_KEY = "TENTWQ7N8V5KHQTW"  
THINGSPEAK_URL = "https://api.thingspeak.com/update"  

def send_data():
    while True:
        # Generate random sensor values
        temperature = round(random.uniform(20, 40), 2)  # °C
        humidity = round(random.uniform(30, 90), 2)     # %
        pressure = round(random.uniform(950, 1050), 2)  # hPa
        light_intensity = round(random.uniform(100, 1000), 2)  # Lux

        # Send data to ThingSpeak
        payload = {
            'api_key': API_KEY, 
            'field2': humidity,          # Humidity in %
            'field3': pressure,          # Pressure in hPa
            'field4': light_intensity    # Light intensity in Lux
        }
        response = requests.get(THINGSPEAK_URL, params=payload)
        
        if response.status_code == 200:
            print(f"Data sent: Temperature={temperature}°C, Humidity={humidity}%, Pressure={pressure} hPa, Light={light_intensity} Lux")
        else:
            print("Failed to send data. Status code:", response.status_code)

        time.sleep(15)  # ThingSpeak allows updates every 15 seconds

# Run the simulation
send_data()

