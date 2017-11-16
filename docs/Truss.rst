.. _truss-example:

Static Nonlinear Truss Example
===============================

::

   import sys
   sys.path.append('/path/to/OpenSeesPy')

   from OpenSees import *
   import numpy as np

   # create model
   m = model(ndm = 2, ndf = 2)

   # variables
   A = 4.0
   E = 29000.0
   alpha = 0.05
   sY = 36.0
   udisp = 2.5

   # create nodes
   nds = {}
   nds[1] = node(1, crds=[0.0, 0.0])
   nds[2] = node(2, crds=[72.0, 0.0])
   nds[3] = node(3, crds=[168.0, 0.0])

   for tag, nd in nds.items():
       m.fix(nd, fix=[1,1])

   nds[4] = node(4, crds=[48.0, 144.0])

   # define materials
   mat = uniaxialMaterial.Hardening(1, E=E, sigmaY=sY,
                     Hiso=0.0, Hkin=alpha/(1-alpha)*E)

   # define elements
   eles = {}
   eles[1] = element.Truss(1, nds=[nds[1],nds[4]], A=A, mat=mat)
   eles[2] = element.Truss(2, nds=[nds[2],nds[4]], A=A, mat=mat)
   eles[3] = element.Truss(3, nds=[nds[3],nds[4]], A=A, mat=mat)

   # loads
   Nsteps = 100
   Px = 160.0
   Py = -100.0*0

   # create TimeSeries
   ts = timeSeries.Linear(1)

   # create a plain load pattern
   ptn = pattern.Plain(1, ts)

   # Create the nodal load - command: load nodeID xForce yForce
   l = ptn.load(nds[4], load=[Px,Py])

   # ------------------------------
   # Start of analysis generation
   # ------------------------------

   # create SOE
   system.ProfileSPD()

   # create DOF number
   numberer.Plain()

   # create constraint handler
   constraints.Plain()

   # create integrator
   integrator.LoadControl(incr=1.0/Nsteps)

   # create algorithm
   algorithm.Newton()

   # create test
   test.NormUnbalance(tol=1.0e-8, iter=10, pFlag=0)

   # create analysis object
   analy = analysis.Static()

   # analysis
   data = np.zeros((Nsteps+1,2))
   for j in range(Nsteps):
       analy.analyze(1)
       data[j+1,0] = nds[4].disp[0]
       data[j+1,1] = ptn.loadFactor*Px

   np.savetxt('Truss.disp',data,delimiter=' ')
    
   # print results
   print("Deterministic response =", nds[4].disp)
   print(nds[4])
   for tag,ele in eles.items():
       print(ele)
