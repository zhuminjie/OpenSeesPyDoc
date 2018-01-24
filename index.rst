.. OpenSeesPy documentation master file, created by
   sphinx-quickstart on Tue Sep 26 12:56:27 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. include:: sub.txt

.. warning::

   The OpenSeesPy library is still in beta version.
   Please send any questions and
   comments to `zhum@oregonstate.edu <zhum@oregonstate.edu>`_.

The OpenSeesPy Library
======================================
`OpenSeesPy`_ is a `Python 3`_ interpreter of `OpenSees`_,
which can be imported as,

::

  import sys
  sys.path.append('/path/to/OpenSeesPy')

  from opensees import*

It strictly follows 
the `commands <http://opensees.berkeley.edu/wiki/index.php/Command_Manual>`_
of the Tcl version
of `OpenSees`_. Here are
some examples of comparison between Tcl and Python commands:

* :ref:`OpenSees-Model-Command`
* :ref:`OpenSees-Node-Command`
* :ref:`OpenSees-Truss-Command`
* :ref:`OpenSees-Fix-Command`
* :ref:`OpenSees-LinearTimeSeries-Command`
* :ref:`OpenSees-Pattern-Command`
* :ref:`OpenSees-Steel01-Command`
* :ref:`OpenSees-ElasticIsotropic-Command`
* :ref:`OpenSees-FiberSection-Command`
* :ref:`OpenSees-LinearTransformation-Command`

Some Tcl commands are modified or changed and new
python commands are added. Those commands are summarized
below.

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Changed Commands

   node
   block2D
   block3D
   ForceBeamColumn
   dispBeamColumn
   analyze

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: New Commands

   mesh
   pvdRecorder
   pfemIntegrator
   pfemSystem
   pfemTest
   pfemAnalysis
   beamIntegration

Examples of OpenSees can be found below.

.. toctree::
   :maxdepth: 2
   :numbered:
   :caption: Tutorials

   truss
   nonlinearTruss

.. _OpenSees-Model-Command:

Model Command Comparison
------------------------

Tcl `Model Command <http://opensees.berkeley.edu/wiki/index.php/Model_command>`_

.. code-block:: tcl

   model basic -ndm $ndm -ndf $ndf

Python Model Command

.. code-block:: python

   model('basic','-ndm',ndm,'-ndf',ndf)

.. _OpenSees-Node-Command:

Node Command Comparison
-----------------------
		
Tcl `Node Command <http://opensees.berkeley.edu/wiki/index.php/Node_command>`_

.. code-block:: tcl

   node $nodeTag $x $y

Python Node Command

.. code-block:: python

   node(nodeTag, x, y)

   crds = [x,y]
   node(nodeTag, *crds)

where in the second form ``crds`` is a python |list| which can be unpacked using ``*crds``.

.. _OpenSees-Truss-Command:

Element Command Comparison
--------------------------
		
Tcl `Truss Element Command <http://opensees.berkeley.edu/wiki/index.php/Truss_Element>`_

.. code-block:: tcl

   element truss $eleTag $iNode $jNode $A $matTag

Python Truss Element Command

.. code-block:: python

   element('truss', eleTag, iNode, jNode, A, matTag)

   eleArgs = ['truss', eleTag, iNode, jNode, A, matTag]
   element(*eleArgs)

where in the second form ``eleArgs`` is a python |list| which can be unpacked using ``*eleArgs``.

.. _OpenSees-Fix-Command:

Fix Command Comparison
----------------------
		
Tcl `Fix Command <http://opensees.berkeley.edu/wiki/index.php/Fix_Command>`_

.. code-block:: tcl

   fix $nodeTag 1 1 1

Python Fix Command

.. code-block:: python

   fix(nodeTag, 1,1,1)

   vals = [1,1,1]
   fix(nodeTag, *vals)

where in the second form ``vals`` is a python |list| which can be unpacked using ``*vals``.

.. _OpenSees-LinearTimeSeries-Command:

TimeSeries Command Comparison
-----------------------------
		
Tcl `Linear TimeSeries Command <http://opensees.berkeley.edu/wiki/index.php/Linear_TimeSeries>`_

.. code-block:: tcl

   timeSeries Linear $tag

Python Linear TimeSeries Command

.. code-block:: python

   timeSeries('Linear', tag)


.. _OpenSees-Pattern-Command:

Pattern Command Comparison
--------------------------

Tcl `Plain Pattern Command <http://opensees.berkeley.edu/wiki/index.php/Plain_Pattern>`_

.. code-block:: tcl

   pattern Plain $patternTag $tsTag {
       load $nodeTag $Px $Py
       eleLoad -ele $eleTag1 $eleTag2 -type -beamUniform $Wy
       sp $nodeTag $dofTag $dofValue
   }

Python Plain Pattern Command

.. code-block:: python

   pattern('Plain', patternTag, tsTag)
   eleLoad('-ele', eleTag1, eleTag2, '-type', '-beamUniform', Wy)
   load(nodeTag, Py, Py)
   sp(nodeTag, dofTag, dofValue)


.. _OpenSees-Steel01-Command:

UniaxialMaterial Command Comparison
-----------------------------------

Tcl `Steel01 UniaxialMaterial Command <http://opensees.berkeley.edu/wiki/index.php/Steel01_Material>`_

.. code-block:: tcl

   uniaxialMaterial Steel01 $matTag $Fy $E0 $b 

Python Steel01 UniaxialMaterial Command

.. code-block:: python

   uniaxialMaterial('Steel01', matTag, Fy, E0, b)

   prop = [Fy, E0, b]
   uniaxialMaterial('Steel01', matTag, *prop)

where in the second form ``prop`` is a python |list| which can be unpacked using ``*prop``.

.. _OpenSees-ElasticIsotropic-Command:

NDMaterial Command Comparison
-----------------------------

Tcl `ElasticIsotropic NDMaterial Command <http://opensees.berkeley.edu/wiki/index.php/Elastic_Isotropic_Material>`_

.. code-block:: tcl

   nDMaterial ElasticIsotropic $matTag $E $v 

Python ElasticIsotropic NDMaterial Command

.. code-block:: python

   
   nDMaterial('ElasticIsotropic', matTag, E, v)

   prop = [E, v]
   nDMaterial('ElasticIsotropic', matTag, *prop)

where in the second form ``prop`` is a python |list| which can be unpacked using ``*prop``.


.. _OpenSees-FiberSection-Command:

Section Command Comparison
--------------------------

Tcl `Fiber Section Command <http://opensees.berkeley.edu/wiki/index.php/Fiber_Section>`_

.. code-block:: tcl

   section Fiber $secTag {
       fiber $yLoc $zLoc $A $matTag
   }

Python Plain Pattern Command

.. code-block:: python

   section('Fiber', secTag)
   fiber(yLoc,zLoc,A,matTag)

Same as the :ref:`OpenSees-Pattern-Command`,
subcommands are added to the last :ref:`OpenSees-FiberSection-Command`.


.. _OpenSees-LinearTransformation-Command:

Transformation Command Comparison
---------------------------------

Tcl `Linear Transformation Command <http://opensees.berkeley.edu/wiki/index.php/Linear_Transformation>`_

.. code-block:: tcl

   geomTransf Linear $transfTag

Python Plain Pattern Command

.. code-block:: python

   geomTransf('Linear', transfTag)




