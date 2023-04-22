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

startflag=0

while True:  
   act_dist = int(grovepi.ultrasonicRead(ultrasonic_ranger))
   
   while value_to_remove in dist_list:
      index = dist_list.index(value_to_remove) #get next 
      time_list.pop(index)
      dist_list.remove(value_to_remove)
   
   if ((grovepi.digitalRead(button)) and (startflag==0)): # Button is pressed, hasn't started
       # get the current time and add it to the list
      print("Button pressed, recording data...")
      start_time=time.time()
      startflag=1
         
   elif ((grovepi.digitalRead(button)) and (startflag==1)):
      if ((act_dist > lower_thresh) and (act_dist < upper_thresh) and (startflag==1)):  #within threshold
         # Read distance value from Ultrasonic
         dist_list.append(int(grovepi.ultrasonicRead(ultrasonic_ranger)))
         # get the current time and add it to the list
         time_list.append(time.time()-start_time)
         
      elif ((act_dist < lower_thresh) or (act_dist < upper_thresh)):
             print("Stay in Range")
            
   elif ((grovepi.digitalRead(button)==0) and (startflag==1)):   
      # calculate the velocity and acceleration data
      vel_list = [(dist_list[i+1] - dist_list[i]) / (time_list[i+1] - time_list[i]) for i in range(len(time_list)-1)]
      acc_list = [(vel_list[i+1] - vel_list[i]) / (time_list[i+1] - time_list[i]) for i in range(len(time_list)-2)]
      
      # Create a grid of subplots
      fig, axs = plt.subplots(3, 1, figsize=(6, 8))

      # Plot the distance vs. time data
      axs[0].plot(time_list, dist_list, 'b-')
      axs[0].set_xlabel('Time (s)')
      axs[0].set_ylabel('Distance (m)')
      axs[0].set_title('Distance vs. Time')

      # Plot the velocity vs. time data
      axs[1].plot(time_list[:-1], vel_list, 'g-')
      axs[1].set_xlabel('Time (s)')
      axs[1].set_ylabel('Velocity (m/s)')
      axs[1].set_title('Velocity vs. Time')

            # Plot the acceleration vs. time data
      axs[2].plot(time_list[:-2], acc_list, 'r-')
      axs[2].set_xlabel('Time (s)')
      axs[2].set_ylabel('Acceleration (m/s^2)')
      axs[2].set_title('Acceleration vs. Time')

      # Adjust the spacing between subplots
      plot.subplots_adjust(hspace=0.5)

      # Save the plot to a file
      plot.savefig('plots.png')
      print(dist_list) 
      print(time_list)
      print("Size of the distance list:", len(dist_list))
      print("Size of the time list:", len(time_list))
      


        
