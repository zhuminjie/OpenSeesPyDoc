.. include:: sub.txt

=====================
 integrator commands
=====================

.. function:: integrator(intType, *intArgs)
   :noindex:

   This command is used to construct the Integrator object. The Integrator object determines the meaning of the terms in the system of equation object Ax=B.

   The Integrator object is used for the following:

   * determine the predictive step for time t+dt
   * specify the tangent matrix and residual vector at any iteration
   * determine the corrective step based on the displacement increment dU

   ================================   ===========================================================================
   ``intType`` |str|                  integrator type
   ``intArgs`` |list|                 a list of integrator arguments
   ================================   ===========================================================================

The following contain information about available ``intType``:



.. toctree::
   :maxdepth: 2
   :caption: Static integrator objects

   loadControl
   displacementControl
   minUnbalDispNorm
   arcLength


.. toctree::
   :maxdepth: 2
   :caption: Transient integrator objects

   centralDifference
   newmark
   hht
   generalizedAlpha
   trbdf2
   explicitDifference

* :ref:`PFEM-Integrator`
