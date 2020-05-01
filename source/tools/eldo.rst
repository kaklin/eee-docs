====
eldo
====

Stop simulation when signal OUTPUT rises past 0.3V.

.. code::

	.EXTRACT XUP(V(OUTPUT), 0.3)
	.OPTION AUTOSTOP=1 

Exclude nets from global V probe

.. code::

	.PROBE V EXCEPT=NET
	+ EXCEPT=XI0.N*
