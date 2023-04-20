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

# Set up variables for plotting
max_distance = 5  # Max distance to plot (in inches)
max_time = 5  # Max time to plot (in seconds)
num_data_points = 100  # Number of data points to plot
time_array = np.linspace(0, max_time, num_data_points)
distance_array = np.zeros(num_data_points)

# Main program loop
while True:
    if GPIO.input(11):  # Button is pressed
        print("Button pressed, recording data...")
        start_time = time.time()  # Record start time

        # Collect data for 5 seconds
        for i in range(num_data_points):
            # Read distance from ultrasonic sensor
            GPIO.setup(13, GPIO.OUT)
            GPIO.output(13, True)
            time.sleep(0.00001)
            GPIO.output(13, False)
            start_pulse = time.time()
            stop_pulse = time.time()
            while GPIO.input(13) == 0:
                start_pulse = time.time()
            while GPIO.input(13) == 1:
                stop_pulse = time.time()
            pulse_duration = stop_pulse - start_pulse
            distance = pulse_duration * 17150
            distance = round(distance, 2)
            if distance > max_distance:
                distance = max_distance
            distance_array[i] = distance

            # Wait for 0.05 seconds before reading again
            time.sleep(0.05)

        # Plot distance vs time
        if time.time() - start_time < max_time:
            print("Data not valid yet")
        else:
            fig, ax = plt.subplots()
            ax.plot(time_array, distance_array)
            ax.set_xlim([0, max_time])
            ax.set_ylim([0, max_distance])
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Distance (in)')
            ax.set_title('Ultrasonic Distance vs Time')
            plt.show()
