================
Cadence Virtuoso
================

Schematic
---------

.. csv-table::
	:file: schematic_keys.csv
	:header: Function,Key,Notes

Layout
------

.. csv-table::
	:file: layout_keys.csv
	:header: Function,Key,Notes

Library
-------

Find and delete locks in library

.. code-block:: bash

	find . -name "*lck*"
	find . -name "*lck*" -delete

ADE Explorer
------------

Useful Expressions
******************

Plot a digital bus from analog waveforms

.. code-block::

	awvCreateBus("SIGNAL" awvAnalog2Digital(list(VT("/SIGNAL<7>") VT("/SIGNAL<6>") VT("/SIGNAL<5>") VT("/SIGNAL<4>") VT("/SIGNAL<3>") VT("/SIGNAL<2>") VT("/SIGNAL<1>") VT("/SIGNAL<0>")) nil nil 0.5 nil "centre") "Unsigned Decimal")

Adjust list() as needed, MSB first. Example for 8 bit signal.

0.5 is the threshold.

"Unsigned Decimal" can be one of: "Binary" "Signed Decimal"


ADE Assembler
-------------

Customization Script
--------------------

https://relyveld.wordpress.com/cadence-page/
