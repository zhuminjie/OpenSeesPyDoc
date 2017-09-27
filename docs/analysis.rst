analysis
========

.. py:function:: analysis(type[, dtmax, dtmin, gravity[,ratio]])

   create an analysis

   :param string type: analysis type, see beow
   :param float dtmax: maximum time step (only for ``'PFEM'`` analysis)
   :param float dtmin: minimum time step (only for ``'PFEM'`` analysis)
   :param float gravity: the gravity acceleration for fly-out nodes, up is positive.  (only for ``'PFEM'`` analysis)
   :param float ratio: the ratio for automatic reducing time step size (only for ``'PFEM'`` analysis);

   Available analysis types:

   * ``'Static'`` -- static analysis
   * ``'Transient'`` -- dynamic analysis with constant time step
   * ``'VariableTransient'`` -- dynamic analysis with variable time step
   * ``'PFEM'`` -- dynamic FSI analysis using Particle Finite Element Method.

