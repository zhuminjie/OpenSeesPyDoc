.. include:: sub.txt

=========================
 plot_modeshape command
=========================

.. function:: postprocessing.Get_Rendering.plot_modeshape(mode_number, scale_factor)

   Any modeshape can be visualized using this command. There is no need to perform an eigen analysis exclusively since the command runs
   an eigen analysis internally. Matplotlib and Numpy are required.
   
   Example: ``plot_modeshape(3, 300)``

   ==============================   ====================================================================
   ``mode_number`` |int|            mode number to visualize (Integer). For example: plot_modeshape(3).
   ``scale_factor`` |int|           scale factor (Integer) for to display mode shape. Default is 200. 
   ==============================   ====================================================================
