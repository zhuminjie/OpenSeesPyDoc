.. include:: sub.txt

.. _NewtonCotes-BeamIntegration:

==============
 NewtonCotes
==============

.. function:: beamIntegration('NewtonCotes', tag, secTag, N)
              beamIntegration('NewtonCotes', tag, N, *secTags)
   :noindex:

   Newton–Cotes integration: points uniformly spaced along the element, **including** both ends. Order of accuracy: :math:`N-1`.

   **Prismatic:** ``('NewtonCotes', tag, secTag, N)``.

   **Non-prismatic:** ``('NewtonCotes', tag, N, *secTags)``.

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.beamIntegration('NewtonCotes', 2, 1, 6)
      ops.beamIntegration('NewtonCotes', 3, 4, 1, 2, 2, 1)
