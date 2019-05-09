# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 15:12:06 2019

@author: pchi893
"""
# Converted to openseespy by: Pavan Chigullapally       
#                         University of Auckland  
#                         Email: pchi893@aucklanduni.ac.nz 
# --------------------------------------------------------------------------------------------------
# Example 1a. cantilever 2D
# EQ ground motion with gravity
# all units are in kip, inch, second
# elasticBeamColumn ELEMENT
#		Silvia Mazzoni & Frank McKenna, 2006
#
#    ^Y
#    |
#    2       __ 
#    |         | 
#    |         | 
#    |         | 
#  (1)      36'
#    |         | 
#    |         | 
#    |         | 
#  =1=    ----  -------->X
#

# SET UP ----------------------------------------------------------------------------

import openseespy.opensees as op
#import the os module
import os
op.wipe()

#########################################################################################################################################################################

#########################################################################################################################################################################
op.model('basic', '-ndm', 2, '-ndf', 3) 

#to create a directory at specified path with name "Data"
os.chdir('C:\\Opensees Python\\OpenseesPy examples')

#this will create the directory with name 'Data' and will update it when we rerun the analysis, otherwise we have to keep deleting the old 'Data' Folder
dir = "C:\\Opensees Python\\OpenseesPy examples\\Data-1a"
if not os.path.exists(dir):
    os.makedirs(dir)

#this will create just 'Data' folder    
#os.mkdir("Data")
    
#detect the current working directory
#path1 = os.getcwd()
#print(path1)

h = 432.0

op.node(1, 0.0, 0.0)
op.node(2, 0.0, h)

op.fix(1, 1, 1, 1)

op.mass(2, 5.18, 1e-9, 0.0)

op.geomTransf('Linear', 1)
A = 3600000000.0
E = 4227.0
Iz = 1080000.0

op.element('elasticBeamColumn', 1, 1, 2, A, E, Iz, 1)

op.recorder('Node', '-file', 'Data-1a/DFree.out','-time', '-node', 2, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-1a/DBase.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Node', '-file', 'Data-1a/RBase.out','-time', '-node', 1, '-dof', 1,2,3, 'reaction')
#op.recorder('Drift', '-file', 'Data-1a/Drift.out','-time', '-node', 1, '-dof', 1,2,3, 'disp')
op.recorder('Element', '-file', 'Data-1a/FCol.out','-time', '-ele', 1, 'globalForce')
op.recorder('Element', '-file', 'Data-1a/DCol.out','-time', '-ele', 1, 'deformations')

#defining gravity loads
op.timeSeries('Linear', 1)
op.pattern('Plain', 1, 1)
op.load(2, 0.0, -2000.0, 0.0)

op.integrator('LoadControl', 0.1)
op.numberer('Plain')
op.system('BandGeneral')
op.constraints('Plain')
op.test('NormDispIncr', 1e-8, 6)
op.algorithm('Newton')
op.analysis('Static')
op.analyze(10)

op.loadConst('-time', 0.0)

#applying Dynamic Ground motion analysis
#G= 386.0
#op.timeSeries('Path', 2, '-dt', 0.005, '-filePath', 'A10000.dat', '-factor', G)
op.timeSeries('Path', 2, '-dt', 0.01, '-filePath', 'BM68elc.acc', '-factor', 1.0)
op.pattern('UniformExcitation', 2, 1, '-accel', 2) #how to give accelseriesTag?

eigen = op. eigen('-fullGenLapack', 1)
import math
power = math.pow(eigen, 0.5)
betaKcomm = 2 * (0.02/power)

op.rayleigh(0.0, 0.0, 0.0, betaKcomm)

op.wipeAnalysis()
op.constraints('Plain')
op.numberer('Plain')
op.system('BandGeneral')
op.test('NormDispIncr', 1e-8, 10)
op.algorithm('Newton')
op.integrator('Newmark', 0.5, 0.25)
op.analysis('Transient')
op.analyze(1000, 0.02)

u2 = op.nodeDisp(2, 1)
print("u2 = ", u2)

op.wipe()