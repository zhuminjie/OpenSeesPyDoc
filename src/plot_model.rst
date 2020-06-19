.. include:: sub.txt

=========================
 plot_model command
=========================

.. function:: postprocessing.Get_Rendering.plot_model(<"nodes">, <"elements">)

   Once the model is built, it can be visualized using this command. By default Node and element tags are not displayed.
   Matplotlib and Numpy are required. No analysis is required in order to visualize the model. 
   
   Input arguments to diaplay node and element tags can be used in any combination.
   
   ==================================  ============================================================
   ``plot_model()``                     Displays the model with no node and element tags on it.
   ``plot_model("nodes")``              Displays the model with only node tags on it.
   ``plot_model("elements")``           Displays the model with only element tags on it.
   ``plot_model("nodes","elements")``   Displays the model with both node and element tags on it.
   ==================================  ============================================================



   
