import time
import matplotlib.pyplot as plt

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN)
GPIO.setup(11, GPIO.IN)

GPIO.setwarnings(False)

#Hardware SPI configuration
SPI_PORT= 0
SPI_DEVICE=0
mcp= Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Create lists to store distance and time data
distances = []
times = []

# Main program loop.
while True:

    # Check if button on pin 11 is pressed
    if GPIO.input(11):
        # Clear lists
        distances = []
        times = []
        start_time = time.time()
        # Wait for 5 seconds to collect data
        while time.time() - start_time < 5:
            # Read distance from ultrasonic sensor
            distance = # Code to read distance from ultrasonic sensor
            # Append distance and time to lists
            distances.append(distance)
            times.append(time.time() - start_time)
            time.sleep(0.1)
        # Plot data if we have valid data
        if distances and times:
            # Filter out distances greater than 5 inches
            distances = [d if d <= 5 else None for d in distances]
            # Filter out times greater than 5 seconds
            times = [t if t <= 5 else None for t in times]
            # Remove None values
            distances = [d for d in distances if d is not None]
            times = [t for t in times if t is not None]
            if distances and times:
                # Plot distance vs time
                plt.plot(times, distances)
                plt.xlabel('Time (s)')
                plt.ylabel('Distance (in)')
                plt.show()
        else:
            print('Data not valid yet')
    else:
        # Code to plot distance, velocity, and acceleration
        # Read distance from ultrasonic sensor
        distance = # Code to read distance from ultrasonic sensor
        # Append distance and time to lists
        distances.append(distance)
        times.append(time.time())
        # Filter out distances greater than 5 inches
        distances = [d if d <= 5 else None for d in distances]
        # Filter out times greater than 5 seconds
        times = [t - times[0] if t - times[0] <= 5 else None for t in times]
        # Remove None values
        distances = [d for d in distances if d is not None]
        times = [t for t in times if t is not None]
        if distances and times:
            # Plot distance vs time
            plt.plot(times, distances)
            plt.xlabel('Time (s)')
            plt.ylabel('Distance (in)')
            plt.show()
