import math
#shaft parameters
fac = 10e2
Ks = 3*fac  # Spring constant for the shaft
Cs = 3949.6  # Damping constant for the shaft
Ms = 1.3  # Mass of the shaft
Ksb = 1*fac  # deformatoion constant for shaft-ball interaction

Mb = 0.0021  # Mass of each ball
K = 7*10e4
c = 0.8
Csb = Chb = 2*c*math.sqrt(Mb*K)
# Csb = Chb = 3.6

#housing parameters
Kh = 3*fac  # Spring constant for the shaft
Ch = 3000.6  # Damping constant for the shaft
Mh = 0.5  # Mass of the shaft
Khb = 1*fac  # deformatoion constant for shaft-ball interaction

#bearing-ball parameters
Nb = 9  # Number of balls

Fm = 100 #contact force 
omega = 600*0.1047198 # rad/s
alpha = 5*math.pi/180  # contact angle for meshing force /line of action

g = 9.81  # Acceleration due to gravity
mu_sb = 0.1  # Friction coefficient between each ball and the cage
mu_hb = 0.1  # Friction coefficient between each ball and the housing

Mp=1.2

sample_per_second=2000
total_time=0.5