"""
Description

    Read from the SHT10 Teperature/Humidity Sensor and push the data
    over the websocket connection

"""

import time
import threading
import websocket
import RPi.GPIO as GPIO
from pi_sht1x import SHT1x
try:
    import simplejson as json
except ImportError:
    import json

GPIO.setwarnings(False)

DATA_PIN = 2
SCK_PIN = 3


def on_message(wsocket, message):
    """Handles any incoming message """
    pass
#     print message


def on_close(wsocket):
    """Perfrom an action when the websocket closes   """
    pass
#     print "### closed ###"


def main():
    """ Main function """

    # Connect to the websocket
    wsocket = websocket.WebSocketApp('ws://127.0.0.1:9998',
                                     on_message=on_message,
                                     on_close=on_close)
    wsocket_t = threading.Thread(target=wsocket.run_forever)
    wsocket_t.daemon = True
    wsocket_t.start()

    # Wait for websocket connection.
    time.sleep(5)

    # Read from the sensor and push the data over the websocket connection
    while True:

        try:
            with SHT1x(DATA_PIN,
                       SCK_PIN,
                       vdd='3V',
                       gpio_mode=GPIO.BCM) as sensor:

                temp = sensor.read_temperature()
                humidity = sensor.read_humidity(temp)

            if temp or humidity:
                '''Create the message to send over the websocket connection.
                Can be in any format, in this case a JSON string.
                See the receive code in main.js in server/static/js
                '''
                message = json.dumps([{'to': 'temp_humid'}, temp, humidity])
                # Send a message over the websocket
                wsocket.send(message)
        except IndexError:
            pass
        except TypeError:
            pass

        time.sleep(30)


if __name__ == '__main__':

    main()
