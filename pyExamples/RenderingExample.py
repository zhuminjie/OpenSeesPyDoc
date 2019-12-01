
##################################################################
## 2D steel frame example to show model visualization.
##
## By - Anurag Upadhyay, PhD Student, University of Utah.
## Date - 11/25/2019
##################################################################

print("=========================================================")
print("Start 2D Steel Frame Example")

from openseespy.opensees import *

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import os
import Get_Rendering


AnalysisType='Pushover'	;		#  Pushover  Gravity

## ------------------------------
## Start of model generation
## -----------------------------
# remove existing model
wipe()

# set modelbuilder
model('basic', '-ndm', 2, '-ndf', 3)

import math

############################################
### Units and Constants  ###################
############################################

inch = 1;
kip = 1;
sec = 1;

# Dependent units
sq_in = inch*inch;
ksi = kip/sq_in;
ft = 12*inch;

# Constants
g = 386.2*inch/(sec*sec);
pi = math.acos(-1);

#######################################
##### Dimensions 
#######################################

# Dimensions Input
H_story=10.0*ft;
W_bayX=16.0*ft;
W_bayY_ab=5.0*ft+10.0*inch;
W_bayY_bc=8.0*ft+4.0*inch;
W_bayY_cd=5.0*ft+10.0*inch;

# Calculated dimensions
W_structure=W_bayY_ab+W_bayY_bc+W_bayY_cd;

# ###########################
# ##### Nodes
# ###########################

# Create All main nodes
node(1, 0.0, 0.0)
node(2, W_bayX, 0.0)
node(3, 2*W_bayX, 0.0)

node(11, 0.0, H_story)
node(12, W_bayX, H_story)
node(13, 2*W_bayX, H_story)

node(21, 0.0, 2*H_story)
node(22, W_bayX, 2*H_story)
node(23, 2*W_bayX, 2*H_story)

node(31, 0.0, 3*H_story)
node(32, W_bayX, 3*H_story)
node(33, 2*W_bayX, 3*H_story)

# ###############
#  Constraints
# ###############

fix(1, 1, 1, 1)
fix(2, 1, 1, 1)
fix(3, 1, 1, 1)

# #######################
# ### Elements 
# #######################

ColTransfTag=1
BeamTranfTag=2

geomTransf('Linear', ColTransfTag)
geomTransf('Linear', BeamTranfTag)

# Assign Elements  ##############
# ## Add non-linear column elements
element('elasticBeamColumn', 1, 1, 11, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)
element('elasticBeamColumn', 2, 2, 12, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)
element('elasticBeamColumn', 3, 3, 13, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)

element('elasticBeamColumn', 11, 11, 21, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)
element('elasticBeamColumn', 12, 12, 22, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)
element('elasticBeamColumn', 13, 13, 23, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)

element('elasticBeamColumn', 21, 21, 31, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)
element('elasticBeamColumn', 22, 22, 32, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)
element('elasticBeamColumn', 23, 23, 33, 20., 1000., 1000., ColTransfTag, '-mass', 0.0)

#  ### Add linear main beam elements, along x-axis
element('elasticBeamColumn', 101, 11, 12, 20., 1000., 1000., BeamTranfTag, '-mass', 0.0)
element('elasticBeamColumn', 102, 12, 13, 20., 1000., 1000., BeamTranfTag, '-mass', 0.0)

element('elasticBeamColumn', 201, 21, 22, 20., 1000., 1000., BeamTranfTag, '-mass', 0.0)
element('elasticBeamColumn', 202, 22, 23, 20., 1000., 1000., BeamTranfTag, '-mass', 0.0)

element('elasticBeamColumn', 301, 31, 32, 20., 1000., 1000., BeamTranfTag, '-mass', 0.0)
element('elasticBeamColumn', 302, 32, 33, 20., 1000., 1000., BeamTranfTag, '-mass', 0.0)

# Visualize the model
Get_Rendering.model_plotter()

