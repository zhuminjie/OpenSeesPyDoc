FSI functions included in normal OpenSees functions
===================================================


PFEM Analysis
-------------

The :ref:`PFEM-Analysis` is one  type of :doc:`analysis`::

  analysis('PFEM', dtmax, dtmin, gravity)

PFEM Integrator
---------------

The :ref:`PFEM-Integrator` is one  type of :doc:`integrator`::

  integrator('PFEM')


PFEM Test
---------

The :ref:`PFEM-Test` is one type of :doc:`test`::

  test('PFEM',tolv,tolp,tolrv,tolrp,tolvrel,tolprel,maxIter[,maxIncr[,printFlag[,normType]]])



PFEM System
-----------

The :ref:`PFEM-System` is one type of :doc:`system`::

  system('PFEM', opt)


