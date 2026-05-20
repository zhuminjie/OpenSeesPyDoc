.. include:: sub.txt

==========
 Legendre
==========

.. function:: beamIntegration('Legendre', tag, secTag, N)
              beamIntegration('Legendre', tag, N, *secTags)
   :noindex:

   Gauss–Legendre integration: more accurate than Lobatto but **no** points at the element ends by default, so less common in force-based elements. Order of accuracy: :math:`2N-1`.

   **Prismatic:** ``beamIntegration('Legendre', tag, secTag, N)``.

   **Non-prismatic:** ``beamIntegration('Legendre', tag, N, secTag1, …, secTagN)``.

   Arguments: see :ref:`Lobatto-BeamIntegration`.

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.beamIntegration('Legendre', 2, 1, 6)
      ops.beamIntegration('Legendre', 3, 4, 1, 2, 2, 1)
