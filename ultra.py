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

# Create empty lists
dist_list= []
time_list = []

#Garbage Value
value_to_remove = 65535
garbage_indices = []

while True:  
   act_dist = int(grovepi.ultrasonicRead(ultrasonic_ranger))
   
   if ((grovepi.digitalRead(button))):# Button is pressed
       # get the current time and add it to the list
         print("Button pressed, recording data...")
         start_time = time.time()
         time_list.append(start_time-start_time)
         if ((act_dist > lower_thresh) and (act_dist < upper_thresh)):  #within threshold
           # Read distance value from Ultrasonic
            dist_list.append(int(grovepi.ultrasonicRead(ultrasonic_ranger)))
            # get the current time and add it to the list
            time_list.append(time.time()-start_time)
   else:
         while value_to_remove in dist_list:
            index = dist_list.index(value_to_remove) #get next 
            time_list.pop(index)
            dist_list.remove(value_to_remove)

         # print the formatted time values  
         print(dist_list) 
         print(time_list)
         print("Size of the list:", len(dist_list))

        
