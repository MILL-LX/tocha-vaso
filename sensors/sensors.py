import time
import board
import busio
from pythonosc import udp_client
import adafruit_vl53l0x
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

osc_host = "127.0.0.1"
osc_port = 9000

# Initialize OSC client
client = udp_client.SimpleUDPClient(osc_host, osc_port)

# Create the I2C bus
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize TOF sensor.
vl53 = adafruit_vl53l0x.VL53L0X(i2c)

# Initialize ADC module to measure LDR voltage.
ads = ADS.ADS1015(i2c)
# Create single-ended input on channel 0
chan = AnalogIn(ads, ADS.P0)

print("sending sensor data to", osc_host, ':', osc_port)

while True:
    # print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage),"{0}".format(vl53.range))
    client.send_message("/ldr", chan.value)
    client.send_message("/tof", vl53.range)
    time.sleep(0.1)