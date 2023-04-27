import paho.mqtt.client as mqtt
import json
import matplotlib.pyplot as plot

fig, axs = plot.subplots(3, 1, figsize=(6, 8))
# Adjust the spacing between subplots
plot.subplots_adjust(hspace=0.5)

def on_connect(client, userdata, flags, rc):
        print("Connected")
        client.subscribe("diegoankur/dist")
        client.subscribe("diegoankur/vel")
        client.subscribe("diegoankur/acc")

        client.message_callback_add("diegoankur/dist", on_message_from_dist)
        client.message_callback_add("diegoankur/vel", on_message_from_vel)
        client.message_callback_add("diegoankur/acc", on_message_from_acc)

# Custom message callback that prints the IP address
def on_message_from_dist(client, userdata, message):
    print("Will graph distance - Received dist list: "+ message.payload.decode())
    # Plot the distance vs. time data
    axs[0].plot(time_list, dist_list, 'b-')
    axs[0].set_xlabel('Time (s)')
    axs[0].set_ylabel('Distance (m)')
    axs[0].set_title('Distance vs. Time')

def on_message_from_vel(client, userdata, message):
    print("Will graph velocity - Received dist list: " + message.payload.decode())
    # Plot the velocity vs. time data
    axs[1].plot(time_list[:-1], vel_list, 'g-')
    axs[1].set_xlabel('Time (s)')
    axs[1].set_ylabel('Velocity (m/s)')
    axs[1].set_title('Velocity vs. Time')

def on_message_from_acc(client, userdata, message):
    print("Will graph acceleration - Received dist list: "+ message.payload.decode())
 # Plot the acceleration vs. time data
    axs[2].plot(time_list[:-2], acc_list, 'r-')
    axs[2].set_xlabel('Time (s)')
    axs[2].set_ylabel('Acceleration (m/s^2)')
    axs[2].set_title('Acceleration vs. Time')


client= mqtt.Client()    #create a client object
client.on_connect = on_connect #attach the on_connect() callback function defined above to the mqtt client
client.connect("mqtt.eclipseprojects.io", 1883, 60) # Connect using the following hostname, port, and keepalive
client.loop_forever()

# Save the plot to a file
plot.savefig('plots.jpg')
