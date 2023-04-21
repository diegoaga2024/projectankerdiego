import grovepi
import time
import matplotlib.pyplot as plot

# set I2C to use the hardware bus
grovepi.set_bus("RPI_1")

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4

# Connect the Grove Button to digital port D3
# SIG,NC,VCC,GND
button = 3

grovepi.pinMode(button,"INPUT")

lower_thresh=5

upper_thresh=30

# Create empty list
dist_list= []

while True:  
   act_dist = int(grovepi.ultrasonicRead(ultrasonic_ranger))
   
   if ((grovepi.digitalRead(button)) and (act_dist > lower_thresh) and (act_dist < upper_thresh)):  # Button is pressed
    print("Button pressed, recording data...")
    # Read distance value from Ultrasonic
    act_dist = int(grovepi.ultrasonicRead(ultrasonic_ranger))
    dist_list.append(act_dist)
    time.sleep(0.1) # don't overload the i2c bus

   else:
      print(dist_list)
           

        
        
