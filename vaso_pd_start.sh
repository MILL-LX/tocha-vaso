#!/bin/bash
cd /home/pi/tocha-vaso
git pull || true
/usr/bin/pd -nogui -audioindev 3 /home/pi/tocha-vaso/pd/vaso.pd