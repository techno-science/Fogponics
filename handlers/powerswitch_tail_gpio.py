"""
Description

    Turn the PowerSwith Tail II on and off and communicate it's status over
    the websocet connection

"""

import time
import threading
import websocket
import RPi.GPIO as GPIO
try:
    import simplejson as json
except ImportError:
    import json

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

OUTPUT_DICT = {18: False}
GPIO_PIN, _ = OUTPUT_DICT.items()

for key, value in OUTPUT_DICT.items():
    GPIO.setup(key, GPIO.OUT)


def on_message(wsocket, message):
    """Handles any incoming message """
    pass
#     print(message)


def on_close(wsocket):
    """Perfrom an action when the websocket closes   """
    pass
#     print("### closed ###")


def main():
    """ Main function """

    # Connect to the websocket
    wsocket = websocket.WebSocketApp('ws://127.0.0.1:9998',
                                    on_message=on_message,
                                    on_close=on_close)
    wsocket_t = threading.Thread(target=wsocket.run_forever)
    wsocket_t.daemon = True
    wsocket_t.start()

    # Wait for websocket to connect
    time.sleep(5)

    '''Create the message to send over the websocket connection. Can be any
    format, in this case a JSON string. See the corresponding receive code in
    main.js in server/static/js
    '''
    message_on = json.dumps([{'to': 'mister'}, 'On'])
    message_off = json.dumps([{'to': 'mister'}, 'Off'])

    while True:

        try:
            GPIO.output(GPIO_PIN, True)
            # Send a message over the websocket
            wsocket.send(message_on)
            time.sleep(300)
            wsocket.send(message_off)
            GPIO.output(GPIO_PIN, False)
            time.sleep(600)
        except Exception as error:
            raise


if __name__ == '__main__':

    main()
