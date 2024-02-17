import time
import websocket
import json
import random
import datetime

# Initialize WebSocket connection to frontend Dash app
ws = websocket.WebSocket()
ws.connect("ws://localhost:8050/ws")  # Replace with your frontend Dash app WebSocket URL

def generate_random_telemetry_data():
    while True:
        timestamp = datetime.datetime.now()
        speed = random.randint(60, 120)
        rpm = random.randint(2000, 6000)
        temperature = random.uniform(70, 100)
        yield timestamp, speed, rpm, temperature

if __name__ == "__main__":
    for timestamp, speed, rpm, temperature in generate_random_telemetry_data():
        data = {"data": [timestamp, speed, rpm, temperature]}
        ws.send(json.dumps(data))
        time.sleep(1)  # Adjust the sleep time as needed to control data generation rate
