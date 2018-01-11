# needed for all scripts, import OpenSees
import sys
sys.path.append('/scratch/opensees/SRC/interpreter')
from opensees import *

# Optional, import matplotlib
import matplotlib.pyplot as plt
import math

# wipe all previous objects
wipe()

# create a model with fluid
model('basic', '-ndm', 2, '-ndf', 3)

# geometric
L = 0.146
H = L
H2 = 0.3
b = 0.012
h = 0.005
alpha = 1.4
Hb = 20.0*b/3.0
tw =  3*h

# material
rho = 1000.0
mu = 0.0001
b1 = 0.0
b2 = -9.81
thk = 0.012
kappa = -1.0

rhos = 2500.0
A = thk*thk
E = 1e6
Iz = thk*thk*thk*thk/12.0
bmass = A*Hb*rhos

# analysis
dtmax = 1e-3
dtmin = 1e-7
totaltime = 1.0

filename = 'obstacle'

# recorder
recorder('PVD', filename, 'disp', 'vel', 'pressure')

# nodes
node( 1, 0.0, 0.0)
node( 2, L, 0.0)
node( 3, L, H)
node( 4, 0.0, H)
node( 5, 0.0, H2)
node( 6, 4*L, 0.0)
node( 7, 4*L, H2)
node( 8, 2*L, 0.0)
node( 9, 2*L, Hb)
node( 10, -tw, H2)
node( 11, -tw, -tw)
node( 12, 4*L+tw, -tw)
node( 13, 4*L+tw, H2)

fix(3, 0, 0, 1)

# transformation
transfTag = 1
geomTransf('Corotational', transfTag)


# section
secTag = 1
section( 'Elastic', secTag, E, A, Iz)

# beam integration
inteTag = 1
numpts = 2
beamIntegration( 'Legendre', inteTag, secTag, numpts)

# mesh
wall = 1
ndf = 3
mesh('tri',wall,ndf,h,11,5,4,1,2,8,6,7,13,12,11,10,1,1,1,1,1,1,1,1,1,1,1)

fluid = 2
ndf = 2
mesh('tri', fluid,ndf,h,4,1,2,3,4,0,1,1,0)

beam = 3
ndf = 3
mesh('line', beam,ndf,h,2,8,9,0,1,'dispBeamColumn',transfTag,inteTag)

#mass
bmass = bmass / len(region(beam,'getNodeTags'))
for nd in region(beam,'getNodeTags'):
    mass(int(nd), bmass, bmass, 0.0)

# fix
for nd in region(wall,'getNodeTags'):
    fix(int(nd), 1,1,1)


# remesh
remesh('tri',alpha,1,fluid,2,wall,beam,'PFEMElement2DBubble',rho,mu,b1,b2,thk,-1.0)

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
system('PFEM', '-umfpack')

# create analysis object
analysis('PFEM', dtmax, dtmin, b2)

# analysis
while getTime() < totaltime:

    # analysis
    if analyze() < 0:
        break


    # remesh
    remesh('tri',alpha,1,fluid,2,wall,beam,'PFEMElement2DBubble',rho,mu,b1,b2,thk,-1.0)

