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

threshold=10;


while True:
    try:
        # Read distance value from Ultrasonic
        print(grovepi.ultrasonicRead(ultrasonic_ranger))

    except Exception as e:
        print ("Error:{}".format(e))
    
    if (grovepi.ultrasonicRead(ultrasonic_ranger) > threshold):
        print(" Far enough")
        print(grovepi.digitalRead(button))
        time.sleep(.5)
        
        except IOError:
            print ("Error")
        
    time.sleep(0.1) # don't overload the i2c bus
    
    else:
        print("Back off")

        
        
