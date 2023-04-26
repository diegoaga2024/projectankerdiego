import paho.mqtt.client as mqtt
import json

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

def on_message_from_vel(client, userdata, message):
    print("Will graph velocity - Received dist list: " + message.payload.decode())

def on_message_from_acc(client, userdata, message):
    print("Will graph acceleration - Received dist list: "+ message.payload.decode())


while True:
        client= mqtt.Client()
        client.on_connect = on_connect
        client.connect("mqtt.eclipseprojects.io", 1883, 60)
        client.loop_forever()





'''
fig, axs = plot.subplots(3, 1, figsize=(6, 8))

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
      plot.savefig('plots.jpg')
      print(dist_list)
      print(time_list)
      print("Size of the distance list:", len(dist_list))
      print("Size of the time list:", len(time_list))
       '''