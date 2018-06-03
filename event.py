#!/usr/bin/python

# MIT License
# 
# Copyright (c) 2017 John Bryan Moore
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# This example from John Bryan Moore is modified by Christian Gehringer slightly
# to work with a LED Matrix.. same MIT license apply.
# Uncomment the print commands for debugging or to set the right distances

import time
import VL53L0X
import os
from subprocess import call
from subprocess import Popen

has_run = False
runscript = True

# Create a VL53L0X object
tof = VL53L0X.VL53L0X()
count = 0
count2 = 0

# Start ranging
tof.start_ranging(VL53L0X.VL53L0X_LONG_RANGE_MODE)

timing = tof.get_timing()

while runscript :
    distance = tof.get_distance()
    if (distance > 2500):
        #print ("%d mm, %d cm, %d" % (distance, (distance/10), count))
        count = count + 1
        if (count > 25):
            call('sudo pkill -f demo', shell=True)
            has_run = False
            count = 0
            count2 = 0
    else:
        count2 = count2 + 1
        #print (" %d cm, %d" % ((distance/10), count))
        if count2 > 8:
            if (has_run == False): 
                has_run = True
                print Popen('/home/pi/event.sh')
                count = 0
                #print ("starting demo")
                #print ("%d mm, %d cm, %d" % (distance, (distance/10), count))
                count2 = 0
            else:
                count = 0
                count2 = 0       
                #print ("is running")
    time.sleep(timing/50000.00)

tof.stop_ranging()

if __name__ == "__main__":
    import sys
    fib(int(sys.argv[1]))
