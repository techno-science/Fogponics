#!/bin/bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

python3 $DIR/server/server.py &
# ALlow time for the web and websocket servers to launch
sleep 10
python3 $DIR/handlers/temp_humid_i2c.py &
python3 $DIR/handlers/powerswitch_tail_gpio.py &
