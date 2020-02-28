===========
Cadence ADE
===========


Useful Expressions
------------------
Plot a digital bus from analog waveforms

awvCreateBus("BUSNAME" awvAnalog2Digital(list(VT("/signal1") VT("/signal2")) nil nil 0.5 nil "centre") "Unsigned Decimal")

Extend list() as needed, MSB first.
0.5 is the threshold.
"Unsigned Decimal" can be one of: "Binary" "Signed Decimal"


Explorer
--------

Assembler
---------
