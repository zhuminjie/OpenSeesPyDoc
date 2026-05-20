.. include:: sub.txt

==============
 Trapezoidal
==============

.. function:: beamIntegration('Trapezoidal', tag, secTag, N)
              beamIntegration('Trapezoidal', tag, N, *secTags)
   :noindex:

   Trapezoidal rule ``beamIntegration``. Two forms as in :ref:`Lobatto-BeamIntegration`.

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.beamIntegration('Trapezoidal', 2, 1, 6)
      ops.beamIntegration('Trapezoidal', 3, 4, 1, 2, 2, 1)
