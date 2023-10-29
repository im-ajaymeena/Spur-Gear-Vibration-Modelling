import math
#shaft parameters
fac = 10e1  # multiplication factor for deformation constants
Ks = 3*fac  # deformation constant for the shaft
Cs = 3949.6  # viscosity constant for the shaft
Ms = 1.3  # Mass of the shaft
Ksb = 1*fac  # deformatoion constant for shaft-ball interaction
Csb = 3.6  # viscosity constant for shaft-ball interaction

#housing parameters
Kh = 3*fac  # Spring constant for the shaft
Ch = 3000.6  # viscosity constant for the shaft
Mh = 0.5  # Mass of the shaft
Khb = 1*fac  # deformatoion constant for shaft-ball interaction
Chb = 3.6  # Viscocity constant for shaft-ball interaction

#bearing-ball parameters
Nb = 9  # Number of balls
Mb = 0.0021  # Mass of each ball
mu_sb = 0.1  # Friction coefficient between each ball and the cage
mu_hb = 0.1  # Friction coefficient between each ball and the housing

# other parameters
Fm = 1 # Meshing contact force (for simplicity taken to be constant)
alpha = 10*math.pi/180  # contact angle for meshing force /line of action
omega = 600*0.1047198 # rad/s


g = 9.81  # Acceleration due to gravity
Mp=1.2

sample_per_second=2000 #should not be modified sampling rate
# total_time=0.1 #time duration for which the model has to be estimated
total_time=1 #time duration for which the model has to be estimated