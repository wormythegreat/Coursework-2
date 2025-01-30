import numpy as np
import matplotlib.pyplot as plt

#np1 means n+1
#nm1 means n-1


def F(s):
    #function returns the value of F(s)
    #not multiplied by m since it cancels out later
    #so here F(s) is acceleration of cart

    V0 = 193.170645

    a = 100
    b = 100
    c = 55
    d = 100
    #define all the variables used to calculate F(s)
    
    Fs1 =  ( 6*(s**5)*(a**(-2))*(b**(-2))*(c**(-2)) )  -  ( 4*(s**3)*(a**(-2))*(b**(-2)) )  -  ( 4*(s**3)*(a**(-2))*(c**(-2)) )  +  ( 2*s*(a**(-2)) )
    Fs2 =  (   ( (s**6)*(a**(-2))*(b**(-2))*(c**(-2)) )  -  ( (s**4)*(a**(-2))*(b**(-2)) )  -  ( (s**4)*(a**(-2))*(c**(-2)) )  +  ( (s**2)*(a**(-2)) )   )   *   ( 4*s*(d**(-2)) )
    #Calculate 2 smaller parts of F(s) separately
    
    Fs = V0 * (np.exp(2-(2*(s**2)*(d**(-2))))) * (Fs1-Fs2)
    #Combine the 2 parts with the rest of F(s)
    
    return Fs




def forward_euler_timestep(S_n, V_n, h):
    #uses the forward euler method to estimate Sn+1 and Vn+1 from Sn and Vn

    S_np1 = S_n + h*V_n
    V_np1 = V_n + h*F(S_n)

    return S_np1, V_np1



def leapfrog_timestep(S_nm1, S_n, V_nm1, V_n, h):
    #uses the leapfrog method to estimate Sn+1 and Vn+1 from Sn-1, Sn, Vn-1, and Vn

    S_np1 = S_nm1 + 2*h*V_n
    V_np1 = V_nm1 + 2*h*F(S_n)

    return S_np1, V_np1



def leapfrog_method(S_0, V_0, h, stop_time, file_name, colors, title):
    #uses the leapfrog method to compute and plot a numerical solution for s and v

    #function parameters:
    #   S_0 is initial position
    #   V_0 is initial velocity
    #   h is the timestep
    #   stop_time is the time at which the method stops

    t = np.arange(0, stop_time + h, h)
    #create the set of values for time
    S = np.zeros(len(t))
    V = np.zeros(len(t))
    #set up arrays to record postion and velocity

    S[0] = S_0
    V[0] = V_0
    #set initial values of position and velocity

    S[1], V[1] = forward_euler_timestep(S[0], V[0], h)
    #uses forward euler method for first timestep since Sn-1 and Vn-1 aren't known

    for n in range(1, len(t)-1):
        S[n+1], V[n+1] = leapfrog_timestep(S[n-1], S[n], V[n-1], V[n], h)
    #uses leapfrog method for every other timestep until stop_time is reached

    if colors == "b":
        plt.axhline(y=0, color="0.0")
        plt.plot(t, S, label="Position", color="b")
        plt.plot(t, V, label="Velocity", color="r")
        plt.title(title)
        plt.legend(fontsize=9)
        plt.savefig(file_name)
        plt.clf()

    else:
        plt.axhline(y=0, color="0.0")
        plt.plot(t, S, label="Position")
        plt.plot(t, V, label="Velocity")
        plt.title(title)
        plt.legend(fontsize=9)
        plt.savefig(file_name)
        plt.clf()
    #plot both position and velocity against time




