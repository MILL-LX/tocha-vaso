# Ricardo Tocha - Vaso

## Sensor Connections

components:
 - Raspberry Pi 3B
 - Raspberry Pi OS Bullseye 32bit
 - Distance Sensor VL53LXX
 - ADC module ADS1115 / ADS1015
 - LDR module MH sensor series

![Sensor Connections](sensor_connections.jpg)

## Raspberry Configuration

install python  
```
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get install build-essential python-dev
sudo apt-get install --upgrade python3-setuptools
sudo apt-get install python3-pip
```

clone repo  
```
git clone https://github.com/MILL-LX/tocha-vaso.git
cd tocha-vaso
```

install blinka (CircuitPython for Linux)  
https://learn.adafruit.com/circuitpython-on-raspberrypi-linux/installing-circuitpython-on-raspberry-pi  
```
sudo pip3 install --upgrade adafruit-python-shell
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo python3 raspi-blinka.py
```
test blinka  
```
python3 sensores/blinkatest.py
```

install adafruit libraries and OSC library  
https://learn.adafruit.com/adafruit-vl53l0x-micro-lidar-distance-sensor-breakout/python-circuitpython  
https://learn.adafruit.com/adafruit-4-channel-adc-breakouts/python-circuitpython  
```
sudo pip3 install adafruit-circuitpython-vl53l0x
sudo pip3 install adafruit-circuitpython-ads1x15
sudo pip3 install python-osc
```

install pure data and extensions for osc comms
```
sudo apt install puredata
sudo apt install pd-mrpeach
sudo apt install pd-mrpeach-net
```

install systemd services  
```
sudo cp vaso-sensores.service /etc/systemd/system/
sudo cp vaso-pd.service /etc/systemd/system/
sudo systemctl enable vaso-sensores.service
sudo systemctl enable vaso-pd.service
```