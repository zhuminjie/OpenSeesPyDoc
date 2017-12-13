.. include:: sub.txt

Introduction
==============

`OpenSees`_ is an `object-oriented`_ software framework.
It widely uses the class inheritance and object
composition in its design (`McKenna, Scott and Fenves`_).

`OpenSeesPy`_ makes an effort to represent
the OO design at the script level.
All user related OpenSees objects are
exported as python objects even the :class:`model`.
Everything users do will be creating objects
and calling object and class methods.
Users
of OpenSees will have a very different
experience in writing OpenSees scirpts in
a more efficient and organized way. 

**No previous OpenSees experience is needed to learn OpenSeesPy.
But experience of Python does help.**

The document is organized in chapters of OpenSees objects.
Every object has its attributes and methods, which
reassemble original OpenSees commands.
For abstract classes such as :class:`element`, :class:`uniaxialMaterial`,
class methods are defined for creating objects of subclasses.

Examples can be found in the last chapter.


The `OpenSeesPy`_ objects:

#. :class:`model`
#. :class:`beamIntegration`
#. :class:`eleLoad`
#. :class:`element`
#. :class:`geomTransf`
#. :class:`load`
#. :class:`mesh`
#. :class:`mp`
#. :class:`NDMaterial`
#. :class:`node`
#. :class:`pattern`
#. :class:`recorder`
#. :class:`region`
#. :class:`section`
#. :class:`sp`
#. :class:`timeSeries`
#. :class:`uniaxialMaterial`
#. :class:`analysis`
#. :class:`algorithm`
#. :class:`constraints`
#. :class:`integrator`
#. :class:`numberer`
#. :class:`system`
#. :class:`test`
