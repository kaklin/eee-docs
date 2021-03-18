================
Cadence Virtuoso
================

Schematic
---------

Tips
****

Using netSet and Net Expressions. In the lower hiererchy cell use Create > Net Expression... and give it a name and a global default value. In the upper hierarchy level use Edit > Net Expression > Available Properties... to connect the net to one existing in the upper hierarchy level. If a component only accepts net connections through netSet, and you want to use a net expression there, use the format ``[@net_name:%:net_name!]``.

Using variables as instance parameters. In the instance parameter insert ``pPar("varname")``. ``varname`` will now appear as a parameter you can set froma higher hierarchy level. N.B. May need to edit the CDF param through the CIW window. Or open a view where the pPar is used and try using the command ``artGenerateHierSymbolCDF(geGetEditCellView())`` in the CIW window.

Series components. e.g. a ring oscillator with series inverters. Input net: ``IN,A<0:9>``. Output net: ``A<0:9>,OUT``.

Shortcuts
*********

.. csv-table::
	:file: schematic_keys.csv
	:header: Function,Key,Notes

Layout
------

Tips
****

To highlight an electrical net, select Connectivity > Nets > Mark... Then use ``F3`` to select the layers via which you want to trace. Turn off NP, PP, CO to prevent highlighting the substrate.

For labels generated inside scripts it's usefule to use Tools -> Create Pins From Labels after importing them into a layout. 

When creating a cell to mosaic, you can draw a rectangle in the ``instance;drawing`` layer to define the instance outline size.

Preferences
***********

``E`` > Dim Major Dots

Options > Selection > Disable "Select objects larger than the window"

Shortcuts
*********

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
