.. include:: sub.txt

==============
Nonlinear MDOF
==============

#. The source code is developed by `Joseph Jaramillo <https://github.com/jjaramillod93>`_ from National University of Engineering.
#. The source code is shown below, which can be downloaded :download:`here </pyExamples/nonlinear_mdof.py>`.
#. The ground motion file :download:`here </pyExamples/el_centro.th>`.
#. And also the python plotting script :download:`here </pyExamples/plot_nonlinear_mdof_graphs.py>`.
#. Make sure the `numpy`_ and `matplotlib`_ packages are installed in your Python distribution.
#. Run the source code in your favorite Python program and should see:

::

   Natural periods:       Natural frequencies:
   T1 = 0.628 [s]    |    f1 = 1.592 [Hz]
   T2 = 0.257 [s]    |    f2 = 3.898 [Hz]
   T3 = 0.162 [s]    |    f3 = 6.164 [Hz]

.. image:: /_static/nonlinear_mdof_abs_accel.jpg

.. image:: /_static/nonlinear_mdof_rel_accel.jpg

.. image:: /_static/nonlinear_mdof_rel_disp.jpg

.. image:: /_static/nonlinear_mdof_hysteresis.jpg

.. literalinclude:: /pyExamples/nonlinear_mdof.py
   :linenos:
   
