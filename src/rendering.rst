.. include:: sub.txt

=============================================================================
 A Procedure to Render 2D or 3D OpenSees Model
=============================================================================

#. The source code is developed by `Anurag Upadhyay <https://github.com/u-anurag>`_ from University of Utah.
#. The source code can be downloaded :download:`here </pyExamples/Get_Rendering.py>`.
#. Import this file in the main OpenSeesPy model file to plot the model in 2D or 3D.
#. The procedure has an option to turn off the diplay of node tags and element tags.
#. Below is an example showing how to visualize an OpenSeesPy model.
#. Save the file 'Get_Rendering.py' in the same folder as the main model file and import by writing in the model file, "import Get_Rendering". (see line 18 in below example)
#. Plot the model by writing "Get_Rendering.model_plotter()" after defining all the nodes and elements. (see line 129 in below example)

.. image:: /_static/ModelPlotter.png

.. literalinclude:: /pyExamples/RenderingExample.py
   :linenos:
