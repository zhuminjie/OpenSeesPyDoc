


.. include:: sub.txt

===============================================================
MasonPan12 - 12 node Masonry panel element
===============================================================

| Developed and implemented by: 
| `Gonzalo Torrisi <mailto:gonzalo.torrisi@ingenieria.uncuyo.edu.ar>` (UNCuyo, Mendoza, Arrgentina)


The MasonPan12 command is used to construct a 12 node masonry panel element (Torrisi, 2012), which has 6 struts (3 in each direction) and it is able to capture the non linear behaviour of a masonry panel element diagonally loaded where
the principal crack is diagonal. The six struts allow the element to carry axial forces after the central strut are totally degraded due to cracking. Also, the six struts can interact with the sourronding frame to introduce shear forces and bending moments to the extreme zone of the columns and beams near the joint.


.. function:: element('MasonPan12', eleTag,*eleNodes,  mat_1, mat_2, thick, w_tot, w_1)
   :noindex:

   ===================================   ===========================================================================
   ``eleTag`` |int|                      unique element object tag
   ``eleNodes`` |listi|                  a list of twelve element nodes in anti clockwise direction startin from the left down corner
   ``mat_1`` |int|                       tag for uniaxial material for central strut behaviour
   ``mat_2`` |int|                       tag for uniaxial material for lateral struts behaviour
   ``Thick`` |float|                     out of plane thickness of the panel
   ``w_tot`` |float |                    ratio of the total strut width to diagonal length of the panel
   ``w1`` |float |                       ratio of central strut width to total strut widht
   ===================================   ===========================================================================

.. seealso::
