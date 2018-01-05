.. include:: sub.txt

analysis -- Perform Finite-Element Analysis
=============================================

.. class:: analysis()

   
   A subclass of :class:`tagged` and
   a base class for OpenSees analysis.

   * attributes

     #. :attr:`tagged.tag`

   * methods

     #. :meth:`tagged.__str__`
     #. :meth:`tagged.remove`
     #. :meth:`analysis.eigen`
     #. :meth:`analysis.wipe`


Following are analysis subclasses available in the OpenSees:

.. toctree::
   :maxdepth: 2

   staticAnalysis
   transientAnalysis
   variableTransientAnalysis
   PFEMAnalysis


.. method:: analysis.wipe()

   Wipe all analysis objects. 


.. method:: analysis.eigen(numEigen,genBandArpack=True,symmBandLapack=False,fullGenLapack=False,frequency=True,findLargest=False)

   Perform the eigen value analysis. Return eigen values |listf|.

   ===============================   ======================================================================================
   ``numEigen`` |int|                Number of eigenvalues required.
   ``genBandArpack`` |bool|          Use genBandArpack eigen solver. (optional)
   ``symmBandLapack`` |bool|         Use symmBandLapack eigen solver. (optional)
   ``fullGenLapack`` |bool|          Use fullGenLapack eigen solver. (optional)
   ``frequency`` |bool|              Use generalized algorithm. (optional)
   ``findLargest`` |bool|            Find the largest. (optional)
   ===============================   ======================================================================================


   #. The eigenvectors are stored at the nodes.
   #. The default eigensolver is able to solve only for N-1 eigenvalues, where N is the number of inertial DOFs. When running into this limitation the -fullGenLapack solver can be used instead of the default Arpack solver.
