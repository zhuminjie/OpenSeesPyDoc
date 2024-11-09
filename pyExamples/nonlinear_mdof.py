'''
=========================================================================================================================
================================================== NonLinear MDOF =======================================================
=========================================================================================================================

By M. Eng. Joseph Jaramillo, National University of Engineering
e-mail: jjaramillod@uni.edu.pe
Date - 22/10/2024

This example models a multi-degree-of-freedom (MDOF) damped system commonly used in earthquake engineering of a three-story 
building. It conducts a nonlinear dynamic (time history)  analysis using the El Centro 1940 earthquake as the input ground
motion.
'''

import openseespy.opensees as ops
import numpy as np
import plot_nonlinear_mdof_graphs
# Base units
m = 1                        # Meters
s = 1                        # Seconds
kN = 1                       # Kilo Newtons

# Derivated units
g = 9.81*m/s**2              # Gravity
cm = 1e-2*m                  # Centimeter
mm = 1e-3*m                  # Milimeter
Ton = kN*s**2/m              # Ton

# Parameters - data
N = 3                        # N° DOF
h = 0.05                     # Damping ratio
dt = 0.02                    # Time step
dt_out = 0.001               # Output time step
tFinal = 35                  # Analysis stop time
m1 = 0.1*Ton                 # Mass / floor 
m2 = 0.1*Ton
m3 = 0.1*Ton 
Py1 = 0.55*kN                 # Yielding strength / floor
Py2 = 0.45*kN                 
Py3 = 0.30*kN                 
K1 = 60*kN/m                 # Stiffness / floor
K2 = 50*kN/m
K3 = 30*kN/m
b = 0.01                     # Strain-hardening ratio

######## Model ###############
ops.wipe()					                     # clear memory of all past model definitions
ops.model('basic', '-ndm', 1, '-ndf', 1) 		 # Define the model builder, ndm=#dimension, ndf=#dofs

# Create nodes
ops.node(0, 0)
ops.node(1, 0, '-mass', m1)
ops.node(2, 0, '-mass', m2)
ops.node(3, 0, '-mass', m3)

# Define boundary condition
ops.fix(0, 1)

# Material definition
ops.uniaxialMaterial('Steel01', 1, Py1, K1, b)
ops.uniaxialMaterial('Steel01', 2, Py2, K2, b)
ops.uniaxialMaterial('Steel01', 3, Py3, K3, b)

# Element definition
ops.element('zeroLength', 1, 0, 1, '-mat',    1   , '-dir', 1, '-doRayleigh', 1)
ops.element('zeroLength', 2, 1, 2, '-mat',    2   , '-dir', 1, '-doRayleigh', 1)
ops.element('zeroLength', 3, 2, 3, '-mat',    3   , '-dir', 1, '-doRayleigh', 1)

# Set Rayleigh damping
w1, w2, w3 = np.array(ops.eigen('-fullGenLapack', 3))**0.5
a0 = 2*h*w1*w2/(w1+w2)
a1 = 2*h/(w1+w2)
ops.rayleigh(a0, .0, .0, a1)                     # RAYLEIGH damping

# Natural periods
print('\nNatural periods:       Natural frequencies:')
print(f'T1 = {2*np.pi/w1:.3f} [s]    |    f1 = {w1/(2*np.pi):.3f} [Hz]')
print(f'T2 = {2*np.pi/w2:.3f} [s]    |    f2 = {w2/(2*np.pi):.3f} [Hz]')
print(f'T3 = {2*np.pi/w3:.3f} [s]    |    f3 = {w3/(2*np.pi):.3f} [Hz]')

# Define the dynamic analysis 
load_tag = 1
patter_tag = 1
direc = 1 
ops.timeSeries('Path', load_tag, '-dt', dt, '-filePath', r'./el_centro.th', '-factor', g)                                           # Reading ground motion
ops.pattern('UniformExcitation', patter_tag, direc, '-accel', load_tag)

# Define output data files
rD_path =  r'./Relative_disp.out'
ops.recorder('Node', '-file', r'./Relative_disp.out', '-time', '-dT', dt_out, '-node', 1, 2, 3, '-dof', 1, 'disp')                  # Relative displacements with respect to the ground

rA_path =  r'./Relative_accel.out'
ops.recorder('Node', '-file', rA_path, '-time', '-dT', dt_out, '-node', 1, 2, 3, '-dof', 1, 'accel')                                # Relative accelerations with respect to the ground

aA_path =  r'./Absolute_accel.out'
ops.recorder('Node', '-file', aA_path, '-timeSeries', load_tag, '-time', '-dT', dt_out, '-node', 0, 1, 2, 3, '-dof', 1, 'accel')    # Absolute accelerations

eF_path =  r'./Element_force.out'
ops.recorder('Element', '-file', eF_path, '-time', '-dT', dt_out, '-ele', 1, 2, 3, 'localForce')                                    # Local spring force

# Run the dynamic analysis
Gamma = 0.5
Beta = 0.25
tol = 1.0e-12
itrs = 100
ops.wipeAnalysis()
ops.algorithm('Newton')
ops.system('BandGen')
ops.numberer('Plain')
ops.constraints('Plain')
ops.integrator('Newmark', Gamma, Beta)
ops.analysis('Transient')
ops.test('NormUnbalance', tol, itrs)
num_steps = int(tFinal/dt_out+1)
ops.analyze(num_steps, dt_out)
ops.wipe()

rD = np.genfromtxt(rD_path, usecols=[1, 2, 3]).T

rA = np.genfromtxt(rA_path, usecols=[1, 2, 3]).T
aA = np.genfromtxt(aA_path, usecols=[1, 2, 3, 4]).T

eF = np.genfromtxt(eF_path, usecols=[1, 2, 3]).T


# Matplotlib plots 
rD /= mm
K = [K1, K2, K3]
Py = [Py1, Py2, Py3]
plot_nonlinear_mdof_graphs.plot(N, rD, rA, aA, eF, dt_out, num_steps, tFinal, K, Py)
