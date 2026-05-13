import numpy as np
import matplotlib.pyplot as plt

x=np.array([1.0,2.0,3.0,3.0,1.0])
y=np.array([1.0,2.0,2.0,1.0,1.0])

plt.plot(x,y,color='blue',linewidth=2,marker='.', markersize=5)
plt.title('zadatak 1')
plt.xlabel('x os')
plt.ylabel('y os')
plt.grid(True)
plt.show()
