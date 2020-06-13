
.. include:: src/sub.txt

===============================
Visualization Development Guide
===============================

You are welcome to contribute to the plotting/post-processing commands. This documentation is to explain what is going on inside 
the plotting library "Get+Rendering" and how you can enhance the functons. As of now, Get_Rendering has functions
to plot a structure, mode shapes and shape of a displaced structure and works for 2D (beam-column elements, 
tri, and quad) and 3D (beam-column, tri, 4-node shell, and 8-node brick) elements. 

As of now, all plotting functions should use Matplotlib only and should be able to produce interactive plots. Developers should test 
the new functions extensively , including on Jupyter Notebook, before submitting a pull request. 

**Note:** A list of test examples will be available soon. 

The source code of all the plotting functions is located in `OpenSeesPy <https://github.com/zhuminjie/OpenSeesPy/tree/master/openseespy-pip/openseespy/postprocessing>`_ repository.

As an object oriented approach and to reduce the code repetition, Get_Rendering uses two types of functions. 

==========================
1. Internal functions
==========================

These functions are helper functions that are called by the user functions once the updated
node coordinates are calculated. 

``_plotBeam3D()`` : A procedure to plot a 3D beam-column (or any element with 2 nodes) using iNode, jNode and some internal variables as input.
					
``_plotTri2D()`` :  A procedure to render a 2D, three node shell (Tri) element using iNode, jNode, kNode in counter-clockwise order and some internal variables as input.
					
``_plotTri3D()`` :  NEEDS to be added.

``_plotQuad2D()`` : A procedure to render a 2D, four node shell (Quad, ShellDKGQ etc.) element using iNode, jNode, kNode, lNode in counter-clockwise and some internal variables as input.

``_plotQuad3D()`` : A procedure to render a 3D, four node shell (Quad, ShellDKGQ etc.) element using iNode, jNode, kNode, lNode in counter-clockwise and some internal variables as input.

``_plotCubeSurf()`` : This procedure is called by the ``plotCubeVol()` command to render each surface in a cube using four corner nodes. 

``_plotCubeVol()`` : A procedure to render a 8-node brick element using a list of eight element nodes in bottom and top faces and in counter-clockwise order, and internal variables as input.

 
==========================
2. User functions
==========================

These are the functions available to users to call through OpenSeesPy script. The following table describes what they are and how they work.

    
    ========================  ==========================================================================================================
    ``plot_model()``          Gets the number of nodes and elements in lists by calling ``getNodeTags()`` and ``getEleTags()``. 
                              Then plots the elements in a loop by checking if the model is 2D or 3D, and calling the ``nodecoord()`` 
                              command for each node to get its original coordinates and internal function ``_plotBeam3D``. 
                              
    ``plot_modeshapes()``     Gets the number of nodes and elements in lists by calling ``getNodeTags()`` and ``getEleTags()``. In a 
                              loop, calls ``nodecoord()`` and ``nodeEigenvector()`` for each node to get original and eigen coordinates 
                              respectively. Then plots the mode shape by calling the internal functions.
                              
    ``recordNodeDisp()``      Redords the displaced node-coordinates in a file to use it later in ``plot_deformedshape()`` function.
    
    ``plot_deformedshape()``  Reads the displacement data from the output of ``recordNodeDisp()`` function and original coordinates 
                              using ``nodecoord()`` function. Then plots the displaced shape of the structure using the internal 
                              functions in a manner similar to ``plot_modeshapes()``.
    ========================  ==========================================================================================================	   
 
=======================================
3. Example of an internal function
=======================================

Here is an example of ``_plotQuad3D()`` internal function:

::

   _plotQuad3D(iNode, jNode, kNode, lNode, ax, show_element_tags, element, eleStyle, fillSurface)

This function uses the following inputs:

    ====================  =============================================================================================================
    *Nodes                iNode, jNode, kNode, lNode : A list of four nodes in counter-clockwise order.
    ax                    Reference to the Matplotlib fixure axes space. This should not be changed. 
    show_element_tags     The default is set to "yes" for plotting the model with ``plot_model()`` and "no" while plotting mode shapes 
                          or deformed shapes. This should not be changed. 
    element               This is the tag of that particular element as a string which is displayed when show_element_tags="yes".
    eleStyle              Use eleStyle = "wire" for a wire frame, and "solid" for solid element lines. Wire frame is used when 
                          overlapping the original shape of the structure with the mode shape or displaced shape.
    fillSurface           Use fillSurface = "yes" for color fill in the elements. fillSurface="no" for wireframe.
    ====================  =============================================================================================================

========================
4. Naming conventions
======================== 

The names of classes, variables, and functions should be self-explanatory. Look for names that give useful information about the meaning of the variable or function.
All the internal functions should start with "``_``" and be in camelCase (for example ``_plotCubeSurf``) to distinguish them from the user functions. There are two type of 
user functions, 1) recorder functions and 2) plot functions. All the "recorder" functions should start with "record" and use camelCase (example: ``recordNodeDisp``) and
the plotting functions should start with "``plot_``" use snake_case (example: ``plot_deformedshape``). Try to keep the internal variables (see 3. Example) consistant. New internal variable should be 
defined only if necessary. 


=============
5. Wish List
=============

Some functions helpful to users might include, but not limited to,

* plot_stress() : Record stress in all the elements of a function and plot. This will be useful in visualization of shear walls, fluid-structure interaction and soil modeled as brick elements.

* plot_strain() : Similar functionality as above.

* plot_sectionfiber() : Visualize stress-strain distribution accross a fiber section in a non-linear beam-column element.

* plot_elementforces() : Element forces such as moment, shear, axial force.

* animate_deformedshape() : Animation of the deformed structure for pushover, cyclic and dynamic analysis.

* animate_elementstress() : Animation of the stress or strain in a structure. 

Feel free to comment and discuss how to streamline your plotting code with the existing ``Get_Rendering`` library. Or contact me 
`Anurag Upadhyay <https://github.com/u-anurag>`_.
