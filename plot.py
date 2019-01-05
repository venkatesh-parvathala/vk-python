import matplotlib.pyplot as plt
import numpy as np
F1=50
F2=100
F3=150
fs=8000
n=np.arange(0,2000,1)
x=np.sin(2* np.pi *F1*n/fs)
plt.subplot(411)
plt.plot(n,x,'b')
y=np.sin(2*np.pi*F2*n/fs+15)
plt.subplot(412)
plt.plot(n,y,'y')
a=np.sin(2*np.pi*F3*n/fs)
plt.subplot(413)
plt.plot(n,a)
z=x+y+a
plt.subplot(414)
plt.plot(n,z)
plt.show()
