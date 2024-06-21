import openseespy.opensees as ops

import os.path
import os

# remove existing model
ops.wipe()

# set modelbuilder
ops.model('basic', '-ndm', 3, '-ndf', 3)

# geometric
L = 0.146
H = L*2
h = L/20

numx = 3.0
numy = 3.0
numz = 3.0

# material
rho = 1000.0
mu = 0.0001
b1 = 0.0
b2 = 0.0
b3 = -9.81
kappa = -1.0

# time steps
dtmax = 1e-3
dtmin = 1e-3
totaltime = 1.0

# filename
filename = 'dambreak3D'

# recorder
ops.recorder('BgPVD', filename, 'disp', 'vel', 'pressure','-dT',0.05)
if not os.path.exists(filename):
    os.makedirs(filename)

# fluid particles
nx = round(L/h*numx)
ny = round(L/h*numy)
nz = round(H/h*numz)

eleArgs = ['PFEMElementBubble', rho, mu, b1, b2, b3, kappa]
partArgs = ['cube', 0.0,0.0,0.0,  L,L,H,   nx,ny,nz]
ops.mesh('part',100, *partArgs, *eleArgs)

print('num particles =',nx*ny*nz)

# wall nodes
ndf = 3

ops.node(1, 0.0, 0.0, 0.0)
ops.node(2, 4*L, 0.0, 0.0)
ops.node(3, 4*L, L, 0.0)
ops.node(4, 0.0, L, 0.0)

ops.node(5, 0.0, 0.0, H)
ops.node(6, 4*L, 0.0, H)
ops.node(7, 4*L, L, H)
ops.node(8, 0.0, L, H)

id = 1
ops.mesh('line', 1, 2, 1,2, id, ndf, h)
ops.mesh('line', 2, 2, 2,3, id, ndf, h)
ops.mesh('line', 3, 2, 3,4, id, ndf, h)
ops.mesh('line', 4, 2, 1,4, id, ndf, h)

ops.mesh('line', 5, 2, 5,6, id, ndf, h)
ops.mesh('line', 6, 2, 6,7, id, ndf, h)
ops.mesh('line', 7, 2, 7,8, id, ndf, h)
ops.mesh('line', 8, 2, 5,8, id, ndf, h)

ops.mesh('line', 9, 2, 1,5, id, ndf, h)
ops.mesh('line', 10, 2, 2,6, id, ndf, h)
ops.mesh('line', 11, 2, 3,7, id, ndf, h)
ops.mesh('line', 12, 2, 4,8, id, ndf, h)

ops.mesh('quad', 13, 4, 1,2,3,4, id ,ndf, h)
ops.mesh('quad', 14, 4, 1,10,5,9, id ,ndf, h)
ops.mesh('quad', 15, 4, 2,11,6,10, id ,ndf, h)
ops.mesh('quad', 16, 4, 3,12,7,11, id ,ndf, h)
ops.mesh('quad', 17, 4, 4,9,8,12, id ,ndf, h)

fixedNodes = set()
for mid in [13,14,15,16,17]:
    for nd in ops.getNodeTags('-mesh', mid):
        fixedNodes.add(nd)
for nd in fixedNodes:
    ops.fix(nd, 1,1,1)
fixedNodes = list(fixedNodes)


# background mesh
lower = [-L, -L, -L]
upper = [5*L, 5*L, 3*L]
ops.mesh('bg', h, *lower, *upper, '-structure',1, len(fixedNodes),*fixedNodes)

# create constraint object
ops.constraints('Plain')

# create numberer object
ops.numberer('Plain')

# create convergence test object
ops.test('PFEM', 1e-5, 1e-2, 1e-5, 1e-5, 1e-15, 1e-15, 10,3, 1, 2)

# create algorithm object
ops.algorithm('Newton')

# create integrator object
ops.integrator('PFEM')

# create SOE object
ops.system('PFEM')

# create analysis object
ops.analysis('PFEM', dtmax, dtmin, b3)


# analyze
while ops.getTime() < totaltime:

    if ops.analyze() < 0:
        break

    ops.remesh()



