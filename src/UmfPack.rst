.. include:: sub.txt

=============
 UmfPack SOE
=============

.. function:: system('UmfPack')
   :noindex:

   This command is used to construct a sparse system of equations which uses the `UmfPack`_ solver.

.. function:: system('UmfPack', '-useLongIndices')
   :noindex:

   Pass ``'-useLongIndices'`` to use 64-bit indices in UMFPACK instead of the default 32-bit indices.

   If symbolic or numeric factorization returns **-1**, try adding this option.
