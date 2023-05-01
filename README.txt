Diego Garcia and Ankur Mathur

Instructions on how to compile/execute a program:

Setup:
Run the server.py file on a local computer.
SSH into the Rpi, which has a GrovePi attached with a ultrasonic sensor at port D3 and a button at D4.
Run ultra.py on the Rpi.

Data Collection:
Push the GrovePi button.
Use a flat, solid object to collect data anywhere with 30 cm and 5 cm of the ultrasonic sensor, varying speed and distance.
Let go of the button whenever you are finished collecting data.

Results:
Watch the ultra file publish the distance, velocity, and accerlation data to the public MQTT server.
Go the the local computer and watch the confirmation that the data was received.
Open the plots.jpeg file containing three subplots of the data.

List of any external libraries that were used(2 days):

grovepi
time
paho.mqtt.client as mqtt
socket
json
matplotlib.pyplot as plot

Link to demo video:
https://drive.google.com/file/d/1KEOgxJlhO2ZWd9jl8E_uOceJuC63LE7h/view?usp=share_link

