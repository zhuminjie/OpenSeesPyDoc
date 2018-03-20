.. include:: sub.txt

======================
 test commands
======================

.. function:: test(testType, *testArgs)

   This command is used to construct the LinearSOE and LinearSolver objects to store and solve the test of equations in the analysis.

   ================================   ===========================================================================
   ``testType`` |str|                 test type
   ``testArgs`` |list|                a list of test arguments
   ================================   ===========================================================================


The following contain information about available ``testType``:

.. toctree::
   :maxdepth: 2

   normUnbalance
   normDispIncr
   energyIncr
   relativeNormUnbalance
   relativeNormDispIncr
   relativeTotalNormDispIncr
   relativeEnergyIncr
   fixedNumIter
   normDispAndUnbalance
   normDispOrUnbalance


* :ref:`PFEM-Test`
