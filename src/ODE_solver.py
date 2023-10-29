
import matplotlib.pyplot as plt
import numpy as np
import scipy.integrate as spi
import math
from params1 import *

#variable index dict
variable_dict = {
    "Xs": 0,
    "Ys": 1,
    "Xh": 2,
    "Yh": 3,
    "Xp": 4,
    "Yp": 5,
    "dXs": 6,
    "dYs": 7,
    "dXh": 8,
    "dYh": 8,
    "dXp": 10,
    "dYp": 11,
}

def calculate_phi_i(i, t, omega, Nb):
    phi_i = (omega*t + 2*(math.pi)*(i-1)/Nb)
    phi_i_deg = (phi_i*(360/(2*math.pi))) % 360
    return phi_i


def calculate_delta_i(Xs, Ys, Xh, Yh, phi_i, c=0):
    delta_i = (Xs - Xh)*np.cos(phi_i) + (Ys - Yh) * \
        np.sin(phi_i) - (c/2)*(1-np.cos(phi_i))

    if delta_i < 0:
        delta_i = 0

    return delta_i


def calculate_v_i(dXs, dYs, dXh, dYh, phi_i):
    v_i = (dXs - dXh)*np.cos(phi_i) + (dYs - dYh)*np.sin(phi_i)

    if v_i < 0:
        v_i = 0

    return v_i


def calculate_sum_term(Xs, Ys, Xh, Yh, dXs, dYs, dXh, dYh, t, eqn, Nb, K, C, mu):
    sum_term = 0
    for i in range(1, Nb+1):
        phi_i = calculate_phi_i(i, t, omega, Nb)
        delta_i = calculate_delta_i(Xs, Ys, Xh, Yh, phi_i)
        v_i = calculate_v_i(dXs, dYs, dXh, dYh, phi_i)

        c_phi = np.cos(phi_i)
        s_phi = np.sin(phi_i)

        if eqn == 1:
            term1 = c_phi + mu*s_phi
            term2 = c_phi
        elif eqn == 2:
            term1 = s_phi - mu*c_phi
            term2 = s_phi
        elif eqn == 3:
            term1 = -(c_phi + mu*s_phi)
            term2 = -c_phi
        elif eqn == 4:
            term1 = -(s_phi + mu*c_phi)
            term2 = -s_phi

        sum_term += K*(delta_i**1.5)*term1 + C*v_i*term2

    return sum_term


def model(v, t, params):

    # state-variable -> u = [Xs, Ys, Xh, Yh, Xp, Yp]
    # v has 12 components: v=[u, u'].

    u, udot = v[:6], v[6:]
    # We compute the second derivative u'' of u.
    Xs, Ys, Xh, Yh, Xp, Yp = u
    dXs, dYs, dXh, dYh, dXp, dYp = udot

    ddXs = (1/Ms)*(Fm*np.cos(alpha)/2 - Cs*(dXp-dXs) - Ks*(Xp-Xs) -
                    calculate_sum_term(Xs, Ys, Xh, Yh, dXs, dYs, dXh, dYh, t, 1, Nb, Ksb, Csb, mu_sb))

    ddYs = (1/Ms)*(-Fm*np.sin(alpha)/2 - Cs*(dYp-dYs) - Ks*(Yp-dYs) -
                    calculate_sum_term(Xs, Ys, Xh, Yh, dXs, dYs, dXh, dYh, t, 2, Nb, Ksb, Csb, mu_sb))

    ddXh = (1/Mh)*(- Ch*dXh - Kh*Xh - 
                    calculate_sum_term(Xs, Ys, Xh, Yh, dXs, dYs, dXh, dYh, t, 3, Nb, Khb, Chb, mu_hb))

    ddYh = (1/Mh)*(- Ch*dYh - Kh*Yh - 
                    calculate_sum_term(Xs, Ys, Xh, Yh, dXs, dYs, dXh, dYh, t, 4, Nb, Khb, Chb, mu_hb))

    ddXp = (1/Mp)*(Fm*np.cos(alpha) - Cs*(dXp-dXs) - Ks*(Xp-Xs))

    ddYp = (1/Mp)*(-Fm*np.sin(alpha) - Cs*(dYp-dYs) - Ks*(Yp-Ys))



    udotdot = [ddXs, ddYs, ddXh, ddYh, ddXp, ddYp]

    # We return v'=[u', u''].
    return np.r_[udot, udotdot]



## Start solving differential equations for above equations

# initial values for v
v0 = np.zeros(12)

# intial velocities dXs, dYs, dXh, dYh, dXp, dYp | we assumed initial state is rest condition velocities = 0
v0[6:] += 0.000
total_sample = int(sample_per_second*total_time)
print("Time for prediction:", total_time)

# time stapms for which prediction to be done
t = np.linspace(0., total_time, total_sample)

# variable which is to be plotted 
plot_var = "Xs"  # chose from     Xs, Ys, Xh, Yh, Xp, Yp, dXs, dYs, dXh, dYh, dXp, dYp
var_index = variable_dict[plot_var]


t_max = max(t)
v = spi.odeint(model, v0, t, args=(Ks,))
plt.figure(figsize=(16, 8))
plt.plot(t[0:], v[0:2000, var_index], 'blue', linewidth=0.2)
plt.ylabel('Amplitude')
plt.xlabel('Time in sec')
plt.tight_layout()
plt.xlim([0.005, t_max])
# displaying the title
plt.title(f"plot of { plot_var }  ")
plt.show()
