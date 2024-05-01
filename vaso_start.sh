#!/bin/bash
/home/pi/vaso/sensors/bin/python3 /home/pi/vaso/sensors/sensors.py start &
/usr/bin/pd /home/pi/vaso/vaso_0.pd