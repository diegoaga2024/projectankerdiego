import paho.mqtt.subscribe as subscribe
dist = subscribe.simple('distance', hostname="eclipse.usc.edu", port=11000)
vel = subscribe.simple('velocity', hostname="eclipse.usc.edu", port=11001)
acc = subscribe.simple('acceleration', hostname="eclipse.usc.edu", port=11002)

print((dist.topic, dist.payload))
print((vel.topic, vel.payload))
print((acc.topic, acc.payload))