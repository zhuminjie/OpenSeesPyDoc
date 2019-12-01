.. include:: sub.txt

=============================================================================
 A Procedure to Render 2D or 3D OpenSees Model
=============================================================================

#. The source code is developed by `Anurag Upadhyay <https://github.com/u-anurag>`_ from University of Utah.
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/Get_Rendering.py>`.
#. Import this file in the main OpenSeesPy model file to plot the model in 2D or 3D.
#. The procedure has an option to turn off the diplay of node tags and element tags.

#. Save the file 'Get_Rendering.py' in the same folder as the main model file and import by writing in the model file, "import Get_Rendering".
#. Plot the model by writing "Get_Rendering.model_plotter()" after defining all the nodes and elements.

.. image:: /_static/ModelPlotter.png

.. literalinclude:: /pyExamples/Get_Rendering.py
   :linenos:
