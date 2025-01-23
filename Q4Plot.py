from Q4Func import *
import matplotlib.pyplot as plt
import numpy as np


#######   V(s)    ##############
Vx = np.linspace(-250,250,5000)
Vy = []
index = 0
for count in Vx:
    Vy.append(V(Vx[index]))
    index = index + 1

plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")

plt.plot(Vx,Vy,'g')

plt.xlabel("s")
plt.ylabel("V(s)")
plt.title("Plot of V(s)")
plt.savefig("./V(s).png")
plt.clf()

################################

#######   F(s)    #############
Fx = np.linspace(-250,250,5000)
Fy = []
index = 0
for count in Fx:
    Fy.append(F(Fx[index]))
    index = index + 1


plt.axhline(0,0,1,color="grey")
plt.axvline(0,0,1,color="grey")

plt.plot(Fx,Fy,'r')

plt.xlabel("s")
plt.ylabel("F(s)")
plt.title("Plot of F(s)")
plt.savefig("./F(s).png")
plt.clf()

###############################