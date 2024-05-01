# Ricardo Tosha - Vaso


## Raspberry Configuration

Components:
 - Raspberry Pi 4B
 - Raspberry Pi OS Bullseye 32bit
 - Distance Sensor VL53LXX
 - ADC module ADS1115 / ADS1015
 - LDR module MH sensor series

Install python with venv, and Blinka (CircuitPython for Linux)
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install build-essential python-dev
sudo apt-get install --upgrade python3-setuptools
sudo apt-get install python3-pip
sudo apt-get install python3-venv
source env/bin/activate
```

create python virtual environment
`python3 -m venv sensores`


https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/python-circuitpython
https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython