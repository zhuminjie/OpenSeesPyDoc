from opensees import *
from math import sqrt

wipe()

# define a 3D model
model("basic","-ndm",3,"-ndf",6)

# the response spectrum function
Tn = [0.0, 0.06, 0.1, 0.12, 0.18, 0.24, 0.3, 0.36, 0.4, 0.42, 
	0.48, 0.54, 0.6, 0.66, 0.72, 0.78, 0.84, 0.9, 0.96, 1.02, 
	1.08, 1.14, 1.2, 1.26, 1.32, 1.38, 1.44, 1.5, 1.56, 1.62, 
	1.68, 1.74, 1.8, 1.86, 1.92, 1.98, 2.04, 2.1, 2.16, 2.22, 
	2.28, 2.34, 2.4, 2.46, 2.52, 2.58, 2.64, 2.7, 2.76, 2.82, 
	2.88, 2.94, 3.0, 3.06, 3.12, 3.18, 3.24, 3.3, 3.36, 3.42, 
	3.48, 3.54, 3.6, 3.66, 3.72, 3.78, 3.84, 3.9, 3.96, 4.02, 
	4.08, 4.14, 4.2, 4.26, 4.32, 4.38, 4.44, 4.5, 4.56, 4.62, 
	4.68, 4.74, 4.8, 4.86, 4.92, 4.98, 5.04, 5.1, 5.16, 5.22, 
	5.28, 5.34, 5.4, 5.46, 5.52, 5.58, 5.64, 5.7, 5.76, 5.82, 
	5.88, 5.94, 6.0]
Sa = [1.9612, 3.72628, 4.903, 4.903, 4.903, 4.903, 4.903, 4.903, 4.903, 4.6696172, 
	4.0861602, 3.6321424, 3.2683398, 2.971218, 2.7241068, 2.5142584, 2.3348086, 2.1788932, 2.0425898, 1.9229566, 
	1.8160712, 1.7199724, 1.6346602, 1.5562122, 1.485609, 1.4208894, 1.3620534, 1.3071398, 1.2571292, 1.211041, 
	1.166914, 1.1267094, 1.0894466, 1.054145, 1.0217852, 0.990406, 0.960988, 0.9335312, 0.9080356, 0.8835206, 
	0.8599862, 0.838413, 0.8168398, 0.7972278, 0.7785964, 0.759965, 0.7432948, 0.7266246, 0.710935, 0.6952454, 
	0.6805364, 0.666808, 0.6540602, 0.6285646, 0.6040496, 0.5814958, 0.5609032, 0.5403106, 0.5206986, 0.5030478, 
	0.485397, 0.4697074, 0.4540178, 0.4393088, 0.4255804, 0.411852, 0.3991042, 0.3863564, 0.3755698, 0.3638026, 
	0.353016, 0.34321, 0.333404, 0.3245786, 0.3157532, 0.3069278, 0.2981024, 0.2902576, 0.2833934, 0.2755486, 
	0.2686844, 0.2618202, 0.254956, 0.2490724, 0.2431888, 0.2373052, 0.2314216, 0.2265186, 0.220635, 0.215732, 
	0.210829, 0.205926, 0.2020036, 0.1971006, 0.1931782, 0.1892558, 0.1853334, 0.181411, 0.1774886, 0.1735662, 
	0.1706244, 0.166702, 0.1637602]
timeSeries("Path",1,"-time", *Tn, "-values", *Sa)

# a uniaxial material for transverse shear
uniaxialMaterial("Elastic",2,938000000.0)

# the elastic beam section and aggregator
section("Elastic",1,30000000000.0,0.09,0.0006749999999999999,0.0006749999999999999,12500000000.0,0.0011407499999999994)
section("Aggregator",3,2,"Vy",2,"Vz","-section",1)

# nodes and masses
node(1,0,0,0)
node(2,0,0,3,"-mass",200,200,200,0,0,0)
node(3,4,0,3,"-mass",200,200,200,0,0,0)
node(4,4,0,0)
node(5,0,0,6,"-mass",200,200,200,0,0,0)
node(6,4,0,6,"-mass",200,200,200,0,0,0)
node(7,4,3,6,"-mass",200,200,200,0,0,0)
node(8,0,3,6,"-mass",200,200,200,0,0,0)
node(9,0,3,3,"-mass",200,200,200,0,0,0)
node(10,0,3,0)
node(11,4,3,3,"-mass",200,200,200,0,0,0)
node(12,4,3,0)
node(13,2,1.5,6)
node(14,2,1.5,3)

# beam elements
beamIntegration("Lobatto", 1, 3, 5)
# beam_column_elements forceBeamColumn
# Geometric transformation command
geomTransf("Linear", 1, 1.0, 0.0, -0.0)
element("forceBeamColumn", 1, 1, 2, 1, 1)
# Geometric transformation command
geomTransf("Linear", 2, 0.0, 0.0, 1.0)
element("forceBeamColumn", 2, 2, 3, 2, 1)
# Geometric transformation command
geomTransf("Linear", 3, 1.0, 0.0, -0.0)
element("forceBeamColumn", 3, 4, 3, 3, 1)
# Geometric transformation command
geomTransf("Linear", 4, 1.0, 0.0, -0.0)
element("forceBeamColumn", 4, 2, 5, 4, 1)
# Geometric transformation command
geomTransf("Linear", 5, 0.0, 0.0, 1.0)
element("forceBeamColumn", 5, 5, 6, 5, 1)
# Geometric transformation command
geomTransf("Linear", 6, 0.0, 0.0, 1.0)
element("forceBeamColumn", 6, 7, 6, 6, 1)
# Geometric transformation command
geomTransf("Linear", 7, 0.0, 0.0, 1.0)
element("forceBeamColumn", 7, 8, 7, 7, 1)
# Geometric transformation command
geomTransf("Linear", 8, 0.0, 0.0, 1.0)
element("forceBeamColumn", 8, 9, 2, 8, 1)
# Geometric transformation command
geomTransf("Linear", 9, 0.0, 0.0, 1.0)
element("forceBeamColumn", 9, 8, 5, 9, 1)
# Geometric transformation command
geomTransf("Linear", 10, 1.0, 0.0, -0.0)
element("forceBeamColumn", 10, 10, 9, 10, 1)
# Geometric transformation command
geomTransf("Linear", 11, 1.0, 0.0, -0.0)
element("forceBeamColumn", 11, 3, 6, 11, 1)
# Geometric transformation command
geomTransf("Linear", 12, 1.0, 0.0, -0.0)
element("forceBeamColumn", 12, 11, 7, 12, 1)
# Geometric transformation command
geomTransf("Linear", 13, 0.0, 0.0, 1.0)
element("forceBeamColumn", 13, 11, 3, 13, 1)
# Geometric transformation command
geomTransf("Linear", 14, 0.0, 0.0, 1.0)
element("forceBeamColumn", 14, 9, 11, 14, 1)
# Geometric transformation command
geomTransf("Linear", 15, 1.0, 0.0, -0.0)
element("forceBeamColumn", 15, 12, 11, 15, 1)
# Geometric transformation command
geomTransf("Linear", 16, 1.0, 0.0, -0.0)
element("forceBeamColumn", 16, 9, 8, 16, 1)

# Constraints.sp fix
fix(1, 1, 1, 1, 1, 1, 1)
fix(10, 1, 1, 1, 1, 1, 1)
fix(4, 1, 1, 1, 1, 1, 1)
fix(12, 1, 1, 1, 1, 1, 1)
fix(13, 0, 0, 1, 1, 1, 0)
fix(14, 0, 0, 1, 1, 1, 0)

# Constraints.mp rigidDiaphragm
rigidDiaphragm(3, 14, 2, 3, 9, 11)
rigidDiaphragm(3, 13, 5, 6, 7, 8)

# define some analysis settings
constraints("Transformation")
numberer("RCM")
system("UmfPack")
test("NormUnbalance", 0.0001, 10)
algorithm("Linear")
integrator("LoadControl", 0.0)
analysis("Static")

# run the eigenvalue analysis with 7 modes
# and obtain the eigenvalues
eigs = eigen("-genBandArpack", 7)

# compute the modal properties
modalProperties("-print", "-file", "ModalReport.txt", "-unorm")

# define a recorder for the (use a higher precision otherwise the results
# won't match with those obtained from eleResponse)
filename = 'ele_1_sec_1.txt'
recorder('Element', '-file', filename, '-closeOnWrite', '-precision', 16, '-ele', 1, 'section', '1', 'force')

# some settings for the response spectrum analysis
tsTag = 1 # use the timeSeries 1 as response spectrum function
direction = 1 # excited DOF = Ux

# currently we use same damping for each mode
dmp = [0.05]*len(eigs)
# we don't want to scale some modes...
scalf = [1.0]*len(eigs)
# CQC function
def CQC(mu, lambdas, dmp, scalf):
	u = 0.0
	ne = len(lambdas)
	for i in range(ne):
		for j in range(ne):
			di = dmp[i]
			dj = dmp[j]
			bij = lambdas[i]/lambdas[j]
			rho = ((8.0*sqrt(di*dj)*(di+bij*dj)*(bij**(3.0/2.0))) /
				((1.0-bij**2.0)**2.0 + 4.0*di*dj*bij*(1.0+bij**2.0) + 
				4.0*(di**2.0 + dj**2.0)*bij**2.0))
			u += scalf[i]*mu[i] * scalf[j]*mu[j] * rho;
	return sqrt(u)

# ========================================================================
# TEST 00
# run a response spectrum analysis for each mode.
# then do modal combination in post-processing.
# Use Tn and Sa lists
# ========================================================================
responseSpectrumAnalysis(direction, '-Tn', *Tn, '-Sa', *Sa)

# read the My values [3rd column] for each step 
# (1 for each mode, they are section forces associated to each modal displacement)
My = []
with open(filename, 'r') as f:
	lines = f.read().split('\n')
	for line in lines:
		if len(line) > 0:
			tokens = line.split(' ')
			My.append(float(tokens[2]))

# post process the results doing the CQC modal combination for the My response (3rd column in section forces)
MyCQC = CQC(My, eigs, dmp, scalf)

print('\n\nTEST 00:\nRun a Response Spectrum Analysis for all modes.')
print('Do CQC combination in post processing.')
print('Use Tn and Sa lists.\n')
print('{0: >10}{1: >15}'.format('Mode', 'My'))
for i in range(len(eigs)):
	print('{0: >10}{1: >15f}'.format(i+1, My[i]))
print('{0: >10}{1: >15f}'.format('CQC', MyCQC))

# ========================================================================
# TEST 01
# run a response spectrum analysis for each mode.
# then do modal combination in post-processing.
# Use a Path timeSeries to store the Tn-Sa pairs
# ========================================================================
responseSpectrumAnalysis(tsTag, direction)

# read the My values [3rd column] for each step 
# (1 for each mode, they are section forces associated to each modal displacement)
My = []
with open(filename, 'r') as f:
	lines = f.read().split('\n')
	for line in lines:
		if len(line) > 0:
			tokens = line.split(' ')
			My.append(float(tokens[2]))

# post process the results doing the CQC modal combination for the My response (3rd column in section forces)
MyCQC = CQC(My, eigs, dmp, scalf)

print('\n\nTEST 01:\nRun a Response Spectrum Analysis for all modes.')
print('Do CQC combination in post processing.')
print('Use a Path timeSeries to store Tn-Sa pairs.\n')
print('{0: >10}{1: >15}'.format('Mode', 'My'))
for i in range(len(eigs)):
	print('{0: >10}{1: >15f}'.format(i+1, My[i]))
print('{0: >10}{1: >15f}'.format('CQC', MyCQC))

# ========================================================================
# TEST 02
# run a response spectrum analysis mode-by-mode.
# grab results during the loop, not using the recorder
# then do modal combination in post-processing.
# ========================================================================
remove('recorder', 0)
My = []
for i in range(len(eigs)):
	responseSpectrumAnalysis(direction, '-Tn', *Tn, '-Sa', *Sa, '-mode', i+1)
	force = eleResponse(1, 'section', '1', 'force')
	My.append(force[2])

# post process the results doing the CQC modal combination for the My response (3rd column in section forces)
MyCQC = CQC(My, eigs, dmp, scalf)

print('\n\nTEST 02:\nRun a Response Spectrum Analysis mode-by-mode.')
print('Grab results during the loop and do CQC combination with them.\n')
print('{0: >10}{1: >15}'.format('Mode', 'My'))
for i in range(len(eigs)):
	print('{0: >10}{1: >15f}'.format(i+1, My[i]))
print('{0: >10}{1: >15f}'.format('CQC', MyCQC))

# done
wipe()
