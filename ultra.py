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

threshold=15;


while True:
   try: 
        if ((grovepi.digitalRead(button) and (grovepi.ultrasonicRead(ultrasonic_ranger)) < threshold) ):  # Button is pressed
            print("Button pressed, recording data...")
            # Read distance value from Ultrasonic
            print(grovepi.ultrasonicRead(ultrasonic_ranger))
            time.sleep(0.1) # don't overload the i2c bus
        
   except Exception as e:
        print ("Error:{}".format(e))
            
        #start_time = time.time()  # Record start time
       
    #if (grovepi.ultrasonicRead(ultrasonic_ranger) > threshold):
        #print(" Far enough")
        #print(grovepi.digitalRead(button))
        #time.sleep(.5)
        
    #else:
        #print("Back off")

        
        
