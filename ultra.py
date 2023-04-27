import grovepi
import time
import paho.mqtt.client as mqtt
import socket
import json

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
vel_list = []
acc_list = []

#Garbage Value
value_to_remove = 65535
garbage_indices = []

startflag=0
sentflag=0

def on_connect(client,userdata, flags, rc):
   print("Connected to server with result code" + str(rc))
   
client = mqtt.Client() #create a client object
client.on_connect = on_connect #attach the on_connect() callback function defined above to the mqtt client
client.connect("mqtt.eclipseprojects.io",1883, 60) #Connect using the following hostname, port, and keepalive interval 
client.loop_start() #ask paho-mqtt to spawn a separate thread to handle incoming and outgoing mqtt messages.
time.sleep(1) #causes program to pause for 1 second to complete connection process

while True:  
   act_dist = int(grovepi.ultrasonicRead(ultrasonic_ranger))
   
   while value_to_remove in dist_list:
      index = dist_list.index(value_to_remove) #get next 
      time_list.pop(index)
      dist_list.remove(value_to_remove)
   
   if ((grovepi.digitalRead(button)) and (startflag==0)): # Button is pressed, hasn't started
       # get the current time and add it to the list
      print("Button pressed, recording data...")
      start_time = time.time()
      startflag=1
      time.sleep(2)
         
   elif ((grovepi.digitalRead(button)) and (startflag==1)): # Button is pressed, and inital start time with recorded
      if ((act_dist > lower_thresh) and (act_dist < upper_thresh) and (startflag==1)):  #If within threshold
         # Add distance value from Ultrasonic
         dist_list.append(act_dist)
         # Get the current time and add it to the list
         time_list.append(time.time()-start_time)
         
      elif ((act_dist < lower_thresh) or (act_dist < upper_thresh)):
             print("Stay in Range") #Data outside of range not added to threshold
            
   elif ((grovepi.digitalRead(button)==0) and (startflag==1) and (sentflag==0)): # Button not being pressed, and data was already taken 
      # calculate the velocity and acceleration data
      vel_list = [(dist_list[i+1] - dist_list[i]) / (time_list[i+1] - time_list[i]) for i in range(len(time_list)-1)]
      acc_list = [(vel_list[i+1] - vel_list[i]) / (time_list[i+1] - time_list[i]) for i in range(len(time_list)-2)]
      
      time_list = [int(x) for x in time_list]
      dist_list = [int(x) for x in dist_list]
      vel_list = [int(x) for x in vel_list]
      acc_list = [int(x) for x in acc_list]
      
      print(time_list)
      print(dist_list)
      print(vel_list)
      
      json_time_list = json.dumps(time_list)
      json_dist_list = json.dumps(dist_list)
      json_vel_list = json.dumps(vel_list)
      json_acc_list = json.dumps(acc_list)
      
      client.publish("diegoankur/time",json_time_list)
      print ("Publishing time")
      time.sleep(1)
      client.publish("diegoankur/dist",json_dist_list)
      print ("Publishing distance")
      time.sleep(1)
      client.publish("diegoankur/vel", json_vel_list)
      print("Publishing velocity")
      time.sleep(1)
      client.publish("diegoankur/acc", json_acc_list)
      print("Publishing acceleration")
      sentflag=1
      time.sleep(4)

