import sympy as sp
from sympy import *

#símbols utilitzats
phi0 = symbols('Phi0')
pi = symbols('pi')
C_J = symbols('C_J')
C_0 = symbols('C_0')
Cg = symbols('Cg')
pa = symbols('pA')
pb = symbols('pB')
pc = symbols('pC')
Vg = symbols('Vg')

#variables
ma = ((phi0/(2*pi))**2)*(C_J+C_0)
mx = C_J*((phi0/(2*pi))**2)
mb = ((phi0/(2*pi))**2)*(2*C_J+C_0+Cg)
mg = (phi0/(2*pi))*Cg*Vg


#matriu de masses
#M = Matrix([[ma,-2*mx,0],[-2*mx,mb,-2*mx],[0,-2*mx,ma]])
M = Matrix([[ma,-2*mx],[-2*mx,ma]])
M_inverse = M.inv()

#vector p
P = Matrix([pa,pb])

H = 0.5*P.T*M_inverse*P


pprint(simplify(H))




