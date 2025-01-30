from Q4Func import *
from Q4Ucrit import *
from Leapfrog_Timestepping_Code import *

c = 0.1
h = 0.0001
stop_t = 50
leapfrog_method(eq1, U_crit - c, h, stop_t, "./Lesser_U.png", "a", "Slightly less than U_crit")
leapfrog_method(eq1, U_crit + c, h, stop_t, "./Greater_U.png", "b", "Slightly more than U_crit")

