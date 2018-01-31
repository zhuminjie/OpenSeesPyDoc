import sys
sys.path.append('/path/to/OpenSeesPy')
from opensees import *

# ------------------------------
# Start of model generation
# -----------------------------

# remove existing model
wipe()

# set modelbuilder
model('basic', '-ndm', 2, '-ndf', 2)

# geometric
L = 0.146
H = L*2
H2 = 0.3
h = 0.005
alpha = 1.2
tw =  3*h

# material
rho = 1000.0
mu = 0.0001
b1 = 0.0
b2 = -9.81
thk = 0.012
kappa = -1.0

# time steps
dtmax = 1e-3
dtmin = 1e-6
totaltime = 1.0

# filename
filename = 'dambreak'

# recorder
recorder('PVD', filename, 'disp', 'vel', 'pressure')

# nodes
node(1, 0.0, 0.0)
node(2, L, 0.0)
node(3, L, H)
node(4, 0.0, H)
node(5, 0.0, H2)
node(6, 4*L, 0.0)
node(7, 4*L, H2)
node(8, -tw, H2)
node(9, -tw, -tw)
node(10, 4*L+tw, -tw)
node(11, 4*L+tw, H2)

# fluid mesh 
fluid = 4
ndf = 2
id = -1
mesh('line', 1, 9, 4,5,8,9,10,11,7,6,2, id, ndf, h)
mesh('line', 2, 3, 2,1,4, id, ndf, h)
mesh('line', 3, 3, 2,3,4, id, ndf, h)

eleArgs = ['PFEMElementBubble',rho,mu,b1,b2,thk,kappa]
mesh('tri', fluid, 2, 2,3, id, ndf, h, *eleArgs)

# wall mesh
wall = 5
id = 1
mesh('tri', wall, 2, 1,2, id, ndf, h)

for nd in getNodeTags('-mesh', wall):
    fix(nd, 1,1)

# save the original modal
record()

# create constraint object
constraints('Plain')

# create numberer object
numberer('Plain')

# create convergence test object
test('PFEM', 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 1e-5, 100, 3, 1, 2)

# create algorithm object
algorithm('Newton')

# create integrator object
integrator('PFEM')

# create SOE object
system('PFEM')

# create analysis object
analysis('PFEM', dtmax, dtmin, b2)

# analysis
while getTime() < totaltime:

    # analysis
    if analyze() < 0:
        break

    remesh(alpha)
    


