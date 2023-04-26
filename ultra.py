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

#Garbage Value
value_to_remove = 65535
garbage_indices = []

startflag=0

def on_connect(client,userdata, flags, rc):
   print("Connected to server with result code" + str(rc))


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

      json_dist_list = json.dumps(dist_list)
      json_vel_list = json.dumps(vel_list)
      json_acc_list = json.dumps(acc_list)

      client = mqtt.Client()
      client.on_connect = on_connect
      client.connect("mqtt.eclipseprojects.io",1883, 60)
      client.loop_start()
      print(dist_list)
      print(time_list)

      client.publish("diegoankur/dist",json_dist_list)
      print ("Publishing distance"+ json_dist_list)
      time.sleep(4)
      client.publish("diegoankur/vel", json_vel_list)
      print("Publishing velocity")
      time.sleep(4)
      client.publish("diegoankur/acc", json_acc_list)
      print("Publishing acceleration")
      time.sleep(4)

