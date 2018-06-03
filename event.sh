#!/bin/bash
#sudo pkill -f runtext2.pyw #kills the running python scripts first!
cd /
#old code using the slower python
#cd /home/pi/rpi-rgb-led-matrix/python/samples/ 
#nohup python runtext3.pyw --text "example test"
#sleep 1
cd /home/pi/rpi-rgb-led-matrix/examples-api-use/
nohup ./demo -D 1  runtext.ppm --led-gpio-mapping=adafruit-hat-pwm --led-rows=64 --led-chain=2
