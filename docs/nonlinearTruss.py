# Nonlinear Truss Example

print("==========================")
import sys
sys.path.append('/path/to/OpenSeesPy')
from OpenSees import *
import numpy as np
import matplotlib.pyplot as plt

# ------------------------------
# Start of model generation
# -----------------------------

print("Starting Nonlinear Truss example")

# set modelbuilder
m = model(ndm = 2, ndf = 2)

# variables
A = 4.0
E = 29000.0
alpha = 0.05
sY = 36.0
udisp = 2.5
Nsteps = 1000
Px = 160.0
Py = 0.0

# create nodes
crds = [[0.0, 0.0], [72.0, 0.0], [168.0, 0.0], [48.0, 144.0]]
nds = [node(crd) for crd in crds]

# set boundary condition
for nd in nds[:-1]:
    nd.fix([1,1])

# define materials
mat = hardening(E=E, sigmaY=sY, Hiso=0.0, Hkin=alpha/(1-alpha)*E)

# define elements
eles = [truss(nds=[nds[0],nds[3]], A=A, mat=mat),
        truss(nds=[nds[1],nds[3]], A=A, mat=mat),
        truss(nds=[nds[2],nds[3]], A=A, mat=mat)]
                        
# create TimeSeries
ts = linearSeries()

# create a plain load pattern
ptn = pattern(ts=ts)

# Create the nodal load
ptn.load(nds[3], load=[Px, Py])

# ------------------------------
# Start of analysis generation
# ------------------------------

# create SOE
profileSPD()

# create DOF number
plainNumberer()

# create constraint handler
plainHandler()

# create integrator
loadControl(incr=1.0/Nsteps)

# create algorithm
newton()

# create test
normUnbalance(tol=1e-8, iter=10)

# create analysis object
analy = staticAnalysis()

# ------------------------------
# Finally perform the analysis
# ------------------------------

# perform the analysis
data = np.zeros((Nsteps+1,2))
for j in range(Nsteps):
    analy.analyze(1)
    data[j+1,0] = nds[3].disp[0]
    data[j+1,1] = ptn.loadFactor*Px

plt.plot(data[:,0], data[:,1])
plt.xlabel('Horizontal Displacement')
plt.ylabel('Horizontal Load')
plt.show()

print("==========================")
