# This is a simplified example. You will need to refer to the RF24 library documentation for exact usage.

from RF24 import RF24, RF24_PA_LOW
import requests

radio = RF24(22, 0)  # GPIO 22 for CE, CE0 for CSN
pipes = [0xF0F0F0F0E1, 0xF0F0F0F0D2]
radio.begin()
radio.setPALevel(RF24_PA_LOW)
radio.openReadingPipe(1, pipes[0])
radio.startListening()

def read_from_nrf24():
    while not radio.available(0):
        time.sleep(1/100)
    received_payload = []
    radio.read(received_payload, radio.getDynamicPayloadSize())
    print("Received payload: {}".format(received_payload))
    return received_payload

def send_to_server(data):
    # Replace with your server's URL and endpoint
    response = requests.post('http://yourserver.com/receive-data', json={'data': data})
    print(response.text)

while True:
    data = read_from_nrf24()
    if data:
        send_to_server(data)
