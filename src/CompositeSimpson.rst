.. include:: sub.txt

==================
 CompositeSimpson
==================

.. function:: beamIntegration('CompositeSimpson', tag, secTag, N)
              beamIntegration('CompositeSimpson', tag, N, *secTags)
   :noindex:

   Composite Simpson ``beamIntegration``. Two forms as in :ref:`Lobatto-BeamIntegration`.

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.beamIntegration('CompositeSimpson', 2, 1, 6)
      ops.beamIntegration('CompositeSimpson', 3, 4, 1, 2, 2, 1)
