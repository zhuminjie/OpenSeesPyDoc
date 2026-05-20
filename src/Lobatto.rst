.. include:: sub.txt

.. _Lobatto-BeamIntegration:

=========
 Lobatto
=========

.. function:: beamIntegration('Lobatto', tag, secTag, N)
              beamIntegration('Lobatto', tag, N, *secTags)
   :noindex:

   Create a Gauss–Lobatto ``beamIntegration`` object. Gauss–Lobatto is common for :doc:`ForceBeamColumn` (`Neuenhofer and Filippou 1997`_) because it places an integration point at each end of the element, where bending is largest if there are no interior element loads.

   **Prismatic** — one section for all points: ``(tag, secTag, N)``.

   **Non-prismatic** — one section tag per point, in order from node *I* to *J*: ``(tag, N, secTag1, secTag2, …, secTagN)``.

   ================================   ===========================================================================
   ``tag`` |int|                      unique beam integration tag
   ``secTag`` |int|                   (prismatic) one defined section for all points
   ``N`` |int|                        number of integration points
   ``secTags`` |listi|                (non-prismatic) ``N`` section tags
   ================================   ===========================================================================

.. note::

   The non-prismatic form assigns different sections along the length (e.g. tapering reinforcement) without relying on hinge-only schemes. The same two forms exist for :doc:`Legendre`, :doc:`Radau`, :doc:`NewtonCotes`, :doc:`Trapezoidal`, and :doc:`CompositeSimpson`.

.. admonition:: Example

   Prismatic: 6 points, section tag 1. Non-prismatic: 3 sections ``[1, 2, 1]`` at 3 Lobatto points.

   .. code-block:: python

      import openseespy.opensees as ops

      ops.beamIntegration('Lobatto', 2, 1, 6)
      sec_tag_list = [1, 2, 1]
      ops.beamIntegration('Lobatto', 3, len(sec_tag_list), *sec_tag_list)
