# Import required libraries
import time
import matplotlib.pyplot as plt
import numpy as np
import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Set up GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)  # Button
GPIO.setup(13, GPIO.IN)  # Ultrasonic sensor
GPIO.setwarnings(False)

# Set up SPI connection to MCP3008 ADC
SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

threshold=5;

# Main program loop
while True:
    if GPIO.input(11):  # Button is pressed
        print("Button pressed, recording data...")
        start_time = time.time()  # Record start time
    
    print('Reading distance values, press Ctrl-C to quit...')
    for i in range(50):
	if (mcp.read_adc(0)>threshold):
            print('Less than 5inch: ')
            print (mcp.read_adc(0))
        else:
            print('More than 54 inch: ') 
            print (mcp.read_adc(0))
        time.sleep(0.1);
