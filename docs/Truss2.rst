.. _truss2-example:

Static Elastic Truss Example
===============================

::

   import sys
   sys.path.append('/path/to/OpenSeesPy')

   from OpenSees import *

   m = model(ndm = 2, ndf = 2)

   # create nodes
   nds = {}
   nds[1] = node(1, [0.0, 0.0])
   nds[2] = node(2, [144.0, 0.0])
   nds[3] = node(3, [168.0, 0.0])
   nds[4] = node(4, [72.0, 96.0])

   # set boundary condition
   for i in range(3):
       m.fix(nds[i+1], fix=[1,1])

   # define materials
   mat = uniaxialMaterial.Elastic(1, E=3000.0)

   # define elements
   eles = {}
   eles[1] = element.Truss(1,nds=[nds[1],nds[4]], A=10.0, mat=mat)
   eles[2] = element.Truss(2,nds=[nds[2],nds[4]], A=5.0, mat=mat)
   eles[3] = element.Truss(3,nds=[nds[3],nds[4]], A=5.0, mat=mat)

   # create TimeSeries
   ts = timeSeries.Linear(1)

   # create a plain load pattern
   ptn = pattern.Plain(1, ts=ts)

   # Create the nodal load - command: load nodeID xForce yForce
   l = ptn.load(nds[4], load=[100.0, -50.0])

   # ------------------------------
   # Start of analysis generation
   # ------------------------------

   # create SOE
   system.BandSPD()

   # create DOF number
   numberer.RCM()

   # create constraint handler
   constraints.Plain()

   # create integrator
   integrator.LoadControl(incr = 1.0)

   # create algorithm
   algorithm.Linear()

   # create analysis object
   analy = analysis.Static()

   # ------------------------------
   # Finally perform the analysis
   # ------------------------------

   # perform the analysis
   analy.analyze(1)

   results = open('results.out','a+')
   
   ux = nds[4].disp[0]
   uy = nds[4].disp[1]
   if abs(ux-0.53009277713228375450)<1e-12 and abs(uy+0.17789363846931768864)<1e-12:
   results.write('PASSED : Truss.py\n');
   print("Passed!")
   else:
   results.write('FAILED : Truss.py\n');
   print("Failed!")
   
   results.close()


