.. include:: sub.txt

======================
 numberer commands
======================

.. function:: numberer(numbererType, *numbererArgs)

   This command is used to construct the DOF_Numberer object. The DOF_Numberer object determines the mapping between equation numbers and degrees-of-freedom -- how degrees-of-freedom are numbered.

   ================================   ===========================================================================
   ``numbererType`` |str|             numberer type
   ``numbererArgs`` |list|            a list of numberer arguments
   ================================   ===========================================================================


The following contain information about available ``numbererType``:

.. toctree::
   :maxdepth: 2

   PlainNumberer
   RCM
   AMD
