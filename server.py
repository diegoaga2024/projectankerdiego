import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plot
import time

time_samples= []
dist_samples= []
vel_samples= []
acc_samples= []


def get_plot(t, d, v, a):
        fig, axs = plot.subplots(3, 1, figsize=(6, 8))
        # Adjust the spacing between subplots
        plot.subplots_adjust(hspace=0.5)
       # Plot the distance vs. time data
        axs[0].plot(t, d, 'b-')
        axs[0].set_xlabel('Time (s)')
        axs[0].set_ylabel('Distance (m)')
        axs[0].set_title('Distance vs. Time')

        # Plot the velocity vs. time data
        axs[1].plot(t[:-1], v, 'g-')
        axs[1].set_xlabel('Time (s)')
        axs[1].set_ylabel('Velocity (m/s)')
        axs[1].set_title('Velocity vs. Time')

         # Plot the acceleration vs. time data
        axs[2].plot(t[:-2], a, 'r-')
        axs[2].set_xlabel('Time (s)')
        axs[2].set_ylabel('Acceleration (m/s^2)')
        axs[2].set_title('Acceleration vs. Time')

        # Save the plot to a file
        print('saving plot')
        plot.savefig('plots.jpg')

def on_connect(client, userdata, flags, rc):
        print("Connected")
        client.subscribe("diegoankur/time")
        client.subscribe("diegoankur/dist")
        client.subscribe("diegoankur/vel")
        client.subscribe("diegoankur/acc")

        client.message_callback_add("diegoankur/time", on_message_from_time)
        client.message_callback_add("diegoankur/dist", on_message_from_dist)
        client.message_callback_add("diegoankur/vel", on_message_from_vel)
        client.message_callback_add("diegoankur/acc", on_message_from_acc)

def on_message_from_time(client, userdata, message):
    global time_samples
    print("Received time list: ")
    time_samples= [float(x) for x in message.payload.decode()[1:-1].split(", ")]
    print(time_samples)
    if time_samples and dist_samples and vel_samples and acc_samples:
        get_plot(time_samples,dist_samples, vel_samples, acc_samples)
        
def on_message_from_dist(client, userdata, message):
    global dist_samples
    print("Received dist list: ")
    dist_samples= [float(x) for x in message.payload.decode()[1:-1].split(", ")]
    print(dist_samples)
    if time_samples and dist_samples and vel_samples and acc_samples:
        get_plot(time_samples,dist_samples, vel_samples, acc_samples)

def on_message_from_vel(client, userdata, message):
    global vel_samples
    print("Received velocity list: ")
    vel_samples= [float(x) for x in message.payload.decode()[1:-1].split(", ")]
    print(vel_samples)
    if time_samples and dist_samples and vel_samples and acc_samples:
        get_plot(time_samples, dist_samples, vel_samples, acc_samples)

def on_message_from_acc(client, userdata, message):
    global acc_samples
    print("Received acceleration list: ")
    acc_samples= [float(x) for x in message.payload.decode()[1:-1].split(", ")]
    print(acc_samples)
    if time_samples and dist_samples and vel_samples and acc_samples:
        get_plot(time_samples, dist_samples, vel_samples, acc_samples)

while True:
        client= mqtt.Client()    #create a client object
        client.on_connect = on_connect #attach the on_connect() callback function defined above to the mqtt client
        client.connect("mqtt.eclipseprojects.io", 1883, 60) # Connect using the following hostname, port, and keepalive
        time.sleep(1)
        client.loop_start()
        if len(time_samples)>0 and len(dist_samples)>0 and len(vel_samples) >0 and len(acc_samples)>0:
            get_plot(time_samples, dist_samples, vel_samples, acc_samples)
            print(dist_samples)