##################################################################
## 3D frame example to show how to render opensees model and 
## plot mode shapes
##
## By - Anurag Upadhyay, PhD Candidate, University of Utah.
## Updated - 09/10/2020
##
## REWRITTEN for opsvis (replaces deprecated Get_Rendering)
##################################################################

import openseespy.opensees as ops
import opsvis as opsv
import matplotlib.pyplot as plt
import numpy as np
from math import asin, sqrt

# set some properties
ops.wipe()
ops.model('Basic', '-ndm', 3, '-ndf', 6)

# properties
# units kip, ft
numBayX = 2
numBayY = 2
numFloor = 7

bayWidthX = 120.0
bayWidthY = 120.0
storyHeights = [162.0, 162.0, 156.0, 156.0, 156.0,
                156.0, 156.0, 156.0, 156.0, 156.0, 156.0]

E = 29500.0
massX = 0.49
M = 0.
coordTransf = "Linear"  # Linear, PDelta, Corotational
massType = "-lMass"     # -lMass, -cMass

nodeTag = 1

# --- Add nodes (floor by floor) ---
zLoc = 0.
for k in range(0, numFloor + 1):
    xLoc = 0.
    for i in range(0, numBayX + 1):
        yLoc = 0.
        for j in range(0, numBayY + 1):
            ops.node(nodeTag, xLoc, yLoc, zLoc)
            ops.mass(nodeTag, massX, massX, 0.01,
                     1.0e-10, 1.0e-10, 1.0e-10)
            if k == 0:
                ops.fix(nodeTag, 1, 1, 1, 1, 1, 1)
            yLoc += bayWidthY
            nodeTag += 1
        xLoc += bayWidthX
    if k < numFloor:
        storyHeight = storyHeights[k]
    zLoc += storyHeight

# --- Add column elements ---
ops.geomTransf(coordTransf, 1, 1, 0, 0)
ops.geomTransf(coordTransf, 2, 0, 0, 1)

eleTag = 1
nodeTag1 = 1
for k in range(0, numFloor):
    for i in range(0, numBayX + 1):
        for j in range(0, numBayY + 1):
            nodeTag2 = nodeTag1 + (numBayX + 1) * (numBayY + 1)
            ops.element('elasticBeamColumn', eleTag,
                        nodeTag1, nodeTag2,
                        50., E, 1000., 1000., 2150., 2150.,
                        1, '-mass', M, massType)
            eleTag += 1
            nodeTag1 += 1

# --- Add beam elements (X-direction) ---
nodeTag1 = 1 + (numBayX + 1) * (numBayY + 1)
for j in range(1, numFloor + 1):
    for i in range(0, numBayX):
        for k in range(0, numBayY + 1):
            nodeTag2 = nodeTag1 + (numBayY + 1)
            ops.element('elasticBeamColumn', eleTag,
                        nodeTag1, nodeTag2,
                        50., E, 1000., 1000., 2150., 2150.,
                        2, '-mass', M, massType)
            eleTag += 1
            nodeTag1 += 1
    nodeTag1 += (numBayY + 1)

# --- Add beam elements (Y-direction) ---
nodeTag1 = 1 + (numBayX + 1) * (numBayY + 1)
for j in range(1, numFloor + 1):
    for i in range(0, numBayY + 1):
        for k in range(0, numBayX):
            nodeTag2 = nodeTag1 + 1
            ops.element('elasticBeamColumn', eleTag,
                        nodeTag1, nodeTag2,
                        50., E, 1000., 1000., 2150., 2150.,
                        2, '-mass', M, massType)
            eleTag += 1
            nodeTag1 += 1
        nodeTag1 += 1

# ================================================================
# VISUALIZATION
# ================================================================

# 1. Plot the model (reads directly from the OpenSees domain)
opsv.plot_model()
plt.title('3D Frame Model')
plt.show()

# 2. Eigen analysis
numEigen = 7
eigenValues = ops.eigen(numEigen)
PI = 2 * asin(1.0)

# Print natural periods
for i in range(numEigen):
    T = PI * 2.0 / np.sqrt(eigenValues[i])
    print(f"Mode {i+1}: T = {T:.4f} s")

# 3. Plot mode shape 5 (auto-scaled)
opsv.plot_mode_shape(5)
plt.title('Mode 5')
plt.show()

# 4. Static gravity analysis
ops.timeSeries('Linear', 1)
ops.pattern('Plain', 1, 1)
ops.load(72, 1, 0, 0, 0, 0, 0)
ops.integrator('LoadControl',10)
ops.analysis('Static')
ops.analyze(10)

# 5. Plot deformed shape (reads current displacements from domain)
opsv.plot_defo()
plt.title('Gravity Deformed Shape')
plt.show()

# 6. Plot mode shape 2 with a fixed scale factor
opsv.plot_mode_shape(2, sfac=300)
plt.title('Mode 2 (sfac=300)')
plt.show()   
