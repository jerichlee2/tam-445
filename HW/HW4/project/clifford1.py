from clifford.g3 import *  # import GA for 3D space
from math import e, pi
a = e1 + 2*e2 + 3*e3 # vector 
R = e**(pi/4*e12)    # rotor 
R*a*~R    # rotate the vector  