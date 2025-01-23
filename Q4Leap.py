from Q4Func import *
from Q4Ucrit import *
from Leapfrog_Timestepping_Code import *

c = 1
h = 0.01
stop_t = 20
leapfrog_method(eq1, U_crit - c, h, stop_t)

