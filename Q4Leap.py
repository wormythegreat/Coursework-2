from Q4Func import *
from Q4Ucrit import *
from Leapfrog_Timestepping_Code import *

c = 0.1
h = 0.1
stop_t = 600
leapfrog_method(eq1, U_crit - c, h, stop_t)

