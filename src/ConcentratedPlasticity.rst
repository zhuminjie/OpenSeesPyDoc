.. _ConcentratedPlasticity:

ConcentratedPlasticity
^^^^^^^^^^^^^^^^^^^^^^

This command creates a Concentrated-Plasticity beamIntegration object. This integration places one plastic-rotation integration point at each element end and three elastic-curvature integration points along the length.

.. function:: beamIntegration ConcentratedPlasticity $integrationTag $secTagI $secTagJ $secTagE

.. function:: beamIntegration('ConcentratedPlasticity',integrationTag,secTagI,secTagJ,secTagE)

.. list-table:: 
   :widths: 10 10 40
   :header-rows: 1

   * - Argument
     - Type
     - Description
   * - $integrationTag
     - |integer|
     - Integer tag identifying beamIntegration
   * - $secTagI 
     - |integer|
     - Tag of previously-defined section object for plastic "deformations" of the plastic hinge at node-I end of the element. (see note 1 below)
   * - $secTagJ
     - |integer| 
     - Tag of previously-defined section object for plastic "deformations" of the plastic hinge at node-J end of the element. (see note 1 below)
   * - $secTagE 
     - |integer| 
     - Tag of previously-defined Elastic section object elastic behavior along element length. (see note 2 below)
   

Note 1: The plastic-deformations behavior at the element ends represents finite plastic deformations. E.g. Bending must be defined in terms of bending moment vs plastic rotation, Axial must be defined in terms of axial force vs plastic axial deformations, etc. Because this integration defines flexibilities, you do not need to add rigid behavior for elastic deformation components, as they are already taken care of by the elastic segment.

Note 2: Use an elastic section which defines elastic moment-curvature, force-strain deformations

Code Developed (2023) by: |Silvia Mazzoni (Silvia's Brainery) & Michael Scott (Oregon State University)|
