====
eldo
====

Stop simulation when signal OUTPUT rises past 0.3V.

.. code::

	.EXTRACT XUP(V(OUTPUT), 0.3)
	.OPTION AUTOSTOP=1 

Exclude nets from global V probe

.. code::

	.PROBE V 
	+ EXCEPT=NET*     ! Remove all nets not explicitly named
	+ EXCEPT=XI0.NET* ! Remove all not explicitly named nets in XI0
	+ EXCEPT=X*.XG*   ! Remove all nets inside digital gates 
