# LED-TOF
64x64 LED matrix controlled by a raspberry pi zero and a VL53L0X time-of-flight distance sensor.

See [https://gehringer.li/led-matrix](https://gehringer.li/led-matrix) for more detailed description of the project. 

##Summary:
This code is connecting the [rpi-rgb-led-matrix by H. Zeller](https://github.com/hzeller/rpi-rgb-led-matrix) scripts to be controlled by a VL53L0X time-of-flight distance sensor, which is implemented by using the [this repository of John Bryan Moore](https://github.com/johnbryanmoore/VL53L0X_rasp_python).
This project is far from coding elegance and screams of my programming ignorance but at least it works.

## Installation and setup
1) Install the repositories mentioned above and get the respective demos running (for the matrix control I don't care for the python code since on a raspberry zero this performs quite slowly compared to C, check out the examples-api-use folder for ./demo).
2) Put event.py in the python folder of the distance senser, e.g. /home/pi/VL53L0X/python and make it autorun on startup.
3) put the batch file event.sh in /home/pi (or whereever you refer it from the event.py). Thats it.
4) No simply modify the event.sh to do whatever you want - I prefer to display my own .ppm images as a runtext.