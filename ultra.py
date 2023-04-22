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
   
   if ((grovepi.digitalRead(button)):# Button is pressed
       # get the current time and add it to the list
         start_time = time.time()
         time_list.append(start_time)
       if ((act_dist > lower_thresh) and (act_dist < upper_thresh)):  #within threshold
         print("Button pressed, recording data...")
         # Read distance value from Ultrasonic
         act_dist = int(grovepi.ultrasonicRead(ultrasonic_ranger))
         dist_list.append(act_dist)
         time.sleep(0.1) # don't overload the i2c bus
         # get the current time and add it to the list
         current_time = time.time()
         time_list.append(current_time)
         # wait for 1 second
         time.sleep(1)
     

   else:
      while value_to_remove in dist_list:
         index = dist_list.index(value_to_remove)
         time_list.pop(index)
         dist_list.remove(value_to_remove)
      
      # format the time values
      formatted_times = [round(t - start_time, 3) for t in time_list]

      # print the formatted time values
      print(formatted_times)   
      print(dist_list) 
      print(time_list)
      print("Size of the list:", len(dist_list))
           

        
        
