.. include:: sub.txt

======================
 system commands
======================

.. function:: system(systemType, *systemArgs)

   This command is used to construct the LinearSOE and LinearSolver objects to store and solve the system of equations in the analysis.

   ================================   ===========================================================================
   ``systemType`` |str|               system type
   ``systemArgs`` |list|              a list of system arguments
   ================================   ===========================================================================


The following contain information about available ``systemType``:

.. toctree::
   :maxdepth: 2

   BandGen
   BandSPD
   ProfileSPD
   SuperLU
   UmfPack
   FullGeneral
   SparseSYM
