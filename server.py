import paho.mqtt.subscribe as subscribe
dist_list = subscribe.simple('distance', hostname="eclipse.usc.edu", port=11000)
vel_list = subscribe.simple('velocity', hostname="eclipse.usc.edu", port=11001)
acc_list = subscribe.simple('acceleration', hostname="eclipse.usc.edu", port=11002)

print((dist_list.topic, dist_list.payload))
print((vel_list.topic, vel_list.payload))
print((acc_list.topic, acc_list.payload))