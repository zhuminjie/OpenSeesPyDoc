.. include:: sub.txt

=======================
 Plotting Commands
=======================

The source code is developed by `Anurag Upadhyay <https://github.com/u-anurag>`_ from University of Utah.

Model visualization is an ongoing development to make OpenSeesPy more user friendly.
It utilizes `Matplotlib 3.0 <https://matplotlib.org>`_ library to plot interactive 2D and 3D models.
See the example :doc:`ModelRendering` for a sample script.

Following elements are supported:

    * 2D and 3D Beam-Column Elements
    * 2D and 3D Quad Elements
    * 2D and 3D Tri Elements
    * 8 Node Brick Elements
    * Tetrahedron Elements (to be added)

The following two commands are needed to visualize the model, as shown below:

::

   # import OpenSeesPy rendering module
   from openseespy.postprocessing.Get_Rendering import *
   
   # render the model after defining all the nodes and elements
   plot_model()
   

.. image:: /_static/ModelVisualization_Intro.png

Following are commands related to model visualization:

#. :doc:`plot_model`
#. :doc:`plot_modeshape`

.. toctree::
   :maxdepth: 1
   :hidden:

   plot_model
   plot_modeshape




