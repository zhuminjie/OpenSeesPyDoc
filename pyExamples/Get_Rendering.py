
##########################################################################################
## This script records the Nodes and Elements in order to render the OpenSees model.	##
## As of now, this procedure does not work for 2D/3D shell and solid elements.			##
##																						##
## Created By - Anurag Upadhyay															##
##																						##
## You can download more examples from https://github.com/u-anurag						##
##########################################################################################

import sys
#sys.path.append('C:/OpenSeesPy')					# for Windows Computer
sys.path.append('/home/anurag/OpenSeesPy')		# For linux Computer
from opensees import *
import numpy as np

def model_plotter():
	import matplotlib.pyplot as plt
	
	nodeList = getNodeTags()
	eleList = getEleTags()
	show_node_tags = 'yes'		# Check if you want to display the node numbers     :: 'yes'  or   'no'
	show_element_tags = 'yes'	# Check if you want to display the element numbers  :: 'yes'  or   'no'
	offset = 0.05				#offset for text

	ele_style = {'color':'black', 'linewidth':1, 'linestyle':'-'} # elements
	node_style = {'color':'black', 'marker':'.', 'linestyle':''} 

	# Check if the model is 2D or 3D
	if len(nodeCoord(nodeList[0])) == 2:
		print('2D model')
		x = []
		y = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1)
		for element in eleList:
			Nodes = eleNodes(element)
			iNode = nodeCoord(Nodes[0])
			jNode = nodeCoord(Nodes[1])
			
			x.append(iNode[0])  # list of x coordinates to define plot view area
			y.append(iNode[1])	# list of y coordinates to define plot view area

			plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),marker='', **ele_style)

			if show_node_tags == 'yes':
				ax.plot(iNode[0], iNode[1], **node_style)
				ax.text(iNode[0], iNode[1], str(Nodes[0]), fontsize=6, fontweight='bold', color='green') #label nodes
				if element == eleList[-1]:
					ax.plot(jNode[0], jNode[1], **node_style)
					ax.text(jNode[0], jNode[1], str(Nodes[0]), fontsize=6, fontweight='bold', color='green') #label nodes

			if show_element_tags == 'yes':
				ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])/2, str(Nodes[0]), fontsize=6, fontweight='bold', color='darkred') #label elements
			
			nodeMins = np.array([min(x),min(y)])
			nodeMaxs = np.array([max(x),max(y)])
			
			xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
			yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
			view_range = max(max(x)-min(x), max(y)-min(y))
			

	if len(nodeCoord(nodeList[0])) == 3:
		x = []
		y = []
		z = []
		fig = plt.figure()
		ax = fig.add_subplot(1,1,1, projection='3d')
		for element in eleList:
			Nodes = eleNodes(element)
			iNode = nodeCoord(Nodes[0])
			jNode = nodeCoord(Nodes[1])
			
			x.append(iNode[0])  # list of x coordinates to define plot view area
			y.append(iNode[1])	# list of y coordinates to define plot view area
			z.append(iNode[2])	# list of z coordinates to define plot view area
			
			plt.plot((iNode[0], jNode[0]), (iNode[1], jNode[1]),(iNode[2], jNode[2]), marker='', **ele_style)
			
			if show_node_tags == 'yes':
				ax.plot([iNode[0], iNode[1], iNode[2]], **node_style)
				ax.text(iNode[0]*1.05, iNode[1]*1.05, iNode[2]*1.05, str(Nodes[0]), fontsize=6, fontweight='bold', color='green') #label nodes
				if element == eleList[-1]:
					ax.plot([jNode[0], jNode[1], jNode[2]], **node_style)
					ax.text(jNode[0]*1.05, jNode[1]*1.05, jNode[2]*1.05, str(Nodes[0]), fontsize=6, fontweight='bold', color='green') #label nodes
			
			if show_element_tags == 'yes':
				ax.text((iNode[0]+jNode[0])/2, (iNode[1]+jNode[1])*1.02/2, (iNode[2]+jNode[2])*1.02/2, str(Nodes[0]), fontsize=6, fontweight='bold', color='darkred') #label elements
			
			nodeMins = np.array([min(x),min(y),min(z)])
			nodeMaxs = np.array([max(x),max(y),max(z)])
			
			xViewCenter = (nodeMins[0]+nodeMaxs[0])/2
			yViewCenter = (nodeMins[1]+nodeMaxs[1])/2
			zViewCenter = (nodeMins[2]+nodeMaxs[2])/2
			view_range = max(max(x)-min(x), max(y)-min(y), max(z)-min(z))
			ax.set_xlim(xViewCenter-(view_range/4), xViewCenter+(view_range/4))
			ax.set_ylim(yViewCenter-(view_range/4), yViewCenter+(view_range/4))
			ax.set_zlim(zViewCenter-(view_range/4), zViewCenter+(view_range/4))
	
	plt.axis('off')
	plt.show()
