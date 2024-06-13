# Build the PLL model



import numpy as np
import control as ctrl
import scipy
import matplotlib.pyplot as plt

#Parameters
Icp = 100e-6 # charge pump current 100uA
Kcp = Icp / 2 / np.pi # Charge pump gain
Kvdd = 20e9 * 2 * np.pi # ring sensitivity to the supply
Kvco = 3e9 * 2 * np.pi # ring sensitivity to the ctrl ( varactor or v2i)
A = 100 # error amplifier gain
wp = 10e3 * 2 * np.pi # error amplifier first pole
Cp = 65e-12 # loop filter cap
Cff = 150e-15 # feedforward cap
R = 20e3 # loop filter resistor
FB = 1 # feedback div

#forward Path1
P1_num = [Kvco * Kcp * R * Cp, Kvco * Kcp]
P1_den = [Cp, 0, 0]
P1_tf = ctrl.TransferFunction(P1_num, P1_den)

print(P1_tf)
#foward Path2_1
P21_num = [A * wp]
P21_den = [Cp, Cp * wp, 0]
P21_tf = ctrl.TransferFunction(P21_num, P21_den)
print(P21_tf)
#forward Path2_2
P22_num = [1]
P22_den = [Cff, 0]
P22_tf = ctrl.TransferFunction(P22_num, P22_den)

print(P22_tf)
# forward path2 seg1
P2seg1_tf = Kcp * (P21_tf + P22_tf)
# forward path2 seg2
P2seg2_num = [Kvdd]
P2seg2_den = [1, 0]
P2seg2_tf = ctrl.TransferFunction(P2seg2_num, P2seg2_den)

P2total_tf = P2seg1_tf * P2seg2_tf


# Sum of the path
Psum = P1_tf + P2total_tf
RL = ctrl.root_locus_plot(Psum,np.arange(0.1,10,0.1))

# close loop

CL = ctrl.feedback(Psum, FB)
print(CL)

t, y = ctrl.step_response(CL)

plt.figure()
plt.plot(t, y)
plt.show()