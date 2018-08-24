.. include:: sub.txt

======================
zeroLengthContactNTS2D
======================

.. function:: element('zeroLengthContactNTS2D', eleTag,'-sNdNum', sNdNum, '-mNdNum', mNdNum, '-Nodes', *Nodes, Kn, kt, phi)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``sNdNum`` |int|                      Number of Slave Nodes
   ``mNdNum`` |int|                      Number of Master nodes
   ``Nodes`` |listi|                     Slave and master node tags respectively
   ``Kn`` |float|                        Penalty in normal direction
   ``Kt`` |float|                        Penalty in tangential direction
   ``phi`` |float|                       Friction angle in degrees
   ===================================   ===========================================================================


.. note::

   #. The contact element is node-to-segment (NTS) contact. The relation follows Mohr-Coulomb frictional law: :math:`T = N \times \tan(\phi)`, where :math:`T` is the tangential force, :math:`N` is normal force across the interface and :math:`\phi` is friction angle.
   #. For 2D contact, slave nodes and master nodes must be 2 DOF and notice that the slave and master nodes must be entered in counterclockwise order.
   #. The resulting tangent from the contact element is non-symmetric. Switch to the non-symmetric matrix solver if convergence problem is experienced.
   #. As opposed to node-to-node contact, predefined normal vector for node-to-segment (NTS) element is not required because contact normal will be calculated automatically at each step.
   #. contact element is implemented to handle large deformations.

.. seealso::


   `Notes <http://opensees.berkeley.edu/wiki/index.php/ZeroLengthContactNTS2D>`_
