.. include:: sub.txt

System Object
=======================

.. class:: system()

   A python :class:`system` object
   is a wrapper to the OpenSees ``LinearSOE`` and
   ``LinearSOESolver`` objects.

   .. note::
   
      One cannot create an :class:`system` object
      directly, but only through the :ref:`system-class-methods`.

      There is only one global :class:`system` object.
      Creating another :class:`system` object
      will automatically invalid the previous :class:`system` objects.

.. _system-class-methods:

Class methods
--------------

#. :meth:`system.BandGen`
#. :meth:`system.BandSPD`
#. :meth:`system.ProfileSPD`
#. :meth:`system.SuperLU`
#. :meth:`system.UmfPack`
#. :meth:`system.FullGen`
#. :meth:`system.SparseSYM`
#. :meth:`system.Diagonal`
#. :meth:`system.SProfileSPD`
#. :meth:`system.PFEM`
#. :meth:`system.PFEMQuasi`
#. :meth:`system.PFEMDia`
#. :meth:`system.Egen`
	       
.. classmethod:: system.BandGen()

   Create a BandGen :class:`system` for matrix which have a banded profile.
   When a solution is required, the Lapack routines DGBSV and SGBTRS are used.

.. classmethod:: system.BandSPD()

   Create a BandSPD :class:`system` for symmetric positive definite matrix
   which have a banded profile.
   When a solution is required, the Lapack routines DPBSV and DPBTRS are used.

.. classmethod:: system.ProfileSPD()

   Create a ProfileSPD :class:`system` for symmetric positive definite matrix.

.. classmethod:: system.SuperLU(piv=0.0,np=1,npRow=1,npCol=1,symm=False)

   Create a SuperLU :class:`system` for sparse matrix
   using `SuperLU`_. Parameters also refer to `SuperLU`_.

.. classmethod:: system.UmfPack()

   Create a UmfPack :class:`system` for sparse matrix
   using `UmfPack`_.

.. classmethod:: system.FullGen()

   Create a FullGen :class:`system` for full matrix.
   When a solution is required, the Lapack routines DGESV and DGETRS are used.
   This type of system should almost never be used!

.. classmethod:: system.SparseSYM(lSparse=1)

   Create a SparseSYM :class:`system` for sparse symmetric 
   matrix which uses a row-oriented solution method in the solution phase.

   =====================   ======================
   ``lSparse`` |int|       Ordering scheme:

                           #. -- MMD
			   #. -- ND
			   #. -- RCM
   =====================   ======================

.. classmethod:: system.Diagonal()

   Create a Diagonal :class:`system` for diagonal matrix.

.. classmethod:: system.SProfileSPD()

   Create a SProfileSPD :class:`system` for symmetric positive definite matrix.

.. classmethod:: system.PFEM()

   Create a PFEM :class:`system` using Particle Finite Element Method
   for Fluid-Structure Interaction with incompressible fluid.

.. classmethod:: system.PFEMQuasi()

   Create a PFEMQuasi :class:`system` using Particle Finite Element Method
   for Fluid-Structure Interaction with quasi-incompressible fluid.

.. classmethod:: system.PFEMDia()

   Create a PFEMDia :class:`system` using Particle Finite Element Method
   for Fluid-Structure Interaction. Use diagonal system but require **very**
   small time steps.

.. classmethod:: system.Egen(sSolver, pSolver=sSolver)

   Create a Egen :class:`system` for both structural analysis and
   Fluid-Structure Interaction using `Eigen`_.

   =====================   ================================================================
   ``sSolver`` |str|       Structural solver:
		           ``'LLT'``, ``'LDLT'``, ``'LU'``, ``'QR'``, ``'CG'``, ``'PCG'``,
		           ``'LSCG'``, ``'BiCG'``, ``'PBiCG'``
   ``pSolver`` |str|       Pressure solver (optional)
   =====================   ================================================================



   


Examples
----------

::

   system.ProfileSPD()


