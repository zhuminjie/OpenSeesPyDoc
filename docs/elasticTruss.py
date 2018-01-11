# Basic Truss Example

print("==========================")
import sys
sys.path.append('/path/to/OpenSeesPy')
from OpenSees import *

# ------------------------------
# Start of model generation
# -----------------------------

print("Starting Elastic Truss example")

# set modelbuilder
m = model(ndm = 2, ndf = 2)

# create nodes
crds = [[0.0, 0.0], [144.0, 0.0], [168.0, 0.0], [72.0, 96.0]]
nds = [node(crd) for crd in crds]

# set boundary condition
for nd in nds[:-1]:
    nd.fix([1,1])

# define materials
mat = elasticMaterial(E=3000.0)

# define elements
eles = [truss(nds=[nds[0],nds[3]], A=10.0, mat=mat),
        truss(nds=[nds[1],nds[3]], A=5.0, mat=mat),
        truss(nds=[nds[2],nds[3]], A=5.0, mat=mat)]
                        
# create TimeSeries
ts = linearSeries()

# create a plain load pattern
ptn = pattern(ts=ts)

# Create the nodal load
ptn.load(nds[3], load=[100.0, -50.0])

# ------------------------------
# Start of analysis generation
# ------------------------------

# create SOE
bandSPD()

# create DOF number
rcm()

# create constraint handler
plainHandler()

# create integrator
loadControl(incr=1.0)

# create algorithm
linearAlgo()

# create analysis object
analy = staticAnalysis()

# ------------------------------
# Finally perform the analysis
# ------------------------------

# perform the analysis
analy.analyze(1)

ux = nds[3].disp[0]
uy = nds[3].disp[1]
if abs(ux-0.53009277713228375450)<1e-12 and abs(uy+0.17789363846931768864)<1e-12:
    print("Passed!")
else:
    print("Failed!")


print("==========================")
