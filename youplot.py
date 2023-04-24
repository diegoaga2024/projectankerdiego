#code20-2
import numpy as np
import math
import matplotlib.pyplot as plt
ang = np.arange(180)
xo = np.sin(np.radians(ang))
noise = ((np.random.rand(180)*2)-1.0)/100.0
xn = xo+noise
plt.subplot(121)
plt.ylabel('sine')
plt.xlabel('degrees')
plt.plot(xo)
plt.subplot(122)
plt.ylabel('sine')
plt.xlabel('degrees')
plt.plot(xn)
plt.suptitle('code20-2')
plt.show()
