.. include:: sub.txt

Section Object
=======================

.. class:: section()

   A python :class:`section` object
   is a wrapper to the OpenSees ``Section`` object.

   .. note::
   
      One cannot create an :class:`section` object
      directly, but only through :ref:`section-class-methods`.


Object attributes
-------------------

.. attribute:: section.tag
      
   An object attribute (get) |int|.
   The tag of the :class:`section` object.

.. attribute:: section.deformation
      
   An object attribute (get/set) |listf|.
   The section deformation.

.. attribute:: section.stress

   An object attribute (get) |listf|.
   The section stress.

.. attribute:: section.tangent

   An object attribute (get) |listl|.
   The section tangent.


Object methods
-------------------

#. :meth:`section.__str__`
#. :meth:`section.remove`
		  
.. method:: section.__str__()

   The string reprsentation of the :class:`section`. Usually
   used in the |print| function.

.. method:: section.remove()

   Remove the corresponding OpenSees ``Section`` object.
	       
   .. seealso::

      :meth:`node.remove`


.. _section-class-methods:

Class methods
--------------

#. :meth:`section.Elastic`

.. classmethod:: section.Elastic(tag, E, A, Iz, Iy=0.0, G=0.0, J=0.0, alphaY=0.0, alphaZ=0.0)

   Create a Elastic :class:`section` object. The inclusion of shear deformations is optional.
   The elastic section can be used in the nonlinear beam column elements, which is useful in the initial stages of developing a complex model.

   ========================   =============================================================
   ``tag`` |int|              :class:`section` tag.
   ``E`` |float|              Tangent stiffness.
   ``A`` |float|              Cross-sectional area of section.
   ``Iz`` |float|             Second moment of area about the local z-axis.
   ``Iy`` |float|             Second moment of area about the local y-axis.
		              (required for 3D analysis).
   ``G`` |float|              Shear Modulus
		              (optional for 2D analysis, required for 3D analysis).
   ``J`` |float|              Torsional moment of inertia of section
		              (required for 3D analysis).
   ``alphaY`` |float|         Shear shape factor along the local y-axis (optional).
   ``alphaZ`` |float|         Shear shape factor along the local z-axis (optional).
   ========================   =============================================================

Examples
----------

::

     sec = section.Elastic(1, E=1e6, A=0.1, Iz=1e4)
     print(sec)

