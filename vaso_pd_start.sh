#!/bin/bash
cd /home/pi/tocha-vaso
git pull || true
/usr/bin/pd -nogui /home/pi/tocha-vaso/pd/vaso.pd