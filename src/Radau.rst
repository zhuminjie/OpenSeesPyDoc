.. include:: sub.txt

=======
 Radau
=======

.. function:: beamIntegration('Radau', tag, secTag, N)
              beamIntegration('Radau', tag, N, *secTags)
   :noindex:

   Gauss–Radau integration: uncommon in force-based elements because only **one** end holds an integration point; useful as building block for plastic-hinge schemes. Places ``N`` Gauss–Radau points with a point at node **I**. Order of accuracy: :math:`2N-2`.

   **Prismatic / non-prismatic:** same pattern as :ref:`Lobatto-BeamIntegration`.

.. admonition:: Example

   .. code-block:: python

      import openseespy.opensees as ops

      ops.beamIntegration('Radau', 2, 1, 6)
      ops.beamIntegration('Radau', 3, 4, 1, 2, 2, 1)
