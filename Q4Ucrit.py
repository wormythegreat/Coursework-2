from Q4Func import *
from math import sqrt

#Use from part 2
#These are not right
eq1 = -143.47473211748283
eq2 = -79.16886756825691
eq3 = -40
eq4 = 0
eq5 = 40
eq6 = 90
eq7 = 150

#####     E = 1/2mv^2 + V(s)   #####

#At V(eq2), v = 0 so can work out the energy of the system with U = U_crit

E_crit = V(eq2)

#So at eq1 (which is where the roller coaster is launched form) the energy
#equation looks like:

#E_crit = 1/2mU^2 + V(eq1)

#Rearranging for U

U_crit = sqrt((2/m)*(E_crit-V(eq1)))