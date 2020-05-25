======
MOSFET
======


Threshold Voltage
=================
Dependent on the MOSFET material properties which are determined by the manufacture process.

.. math:: 

	V_t = 2\phi_b + \frac{\sqrt{2 \epsilon_{Si} q N_A 2\phi_b} }{C_{ox}} + V_{fb}

where :math:`\phi_b=V_T \ln{(\frac{N_A}{n_i})}` is the bulk potential, :math:`N_A` is carrier density in the doped substrate, :math:`n_i` is the intrinsic carrier concentration in undoped silicon


**Body Effect**

.. math:: V_t=V_{t0} - \gamma(\sqrt{\phi + V_{BS}}-\sqrt{\phi})

.. math:: \gamma = \frac{\sqrt{2\epsilon_{Si}qN}}{C_{ox}}


Operating Regions
=================

Sub-threshold
-------------
Also referred to as cutoff region, or operating in weak-inversion.

Conditional on :math:`V_{GS} < V_t`.

**Simple**

.. math:: 

	I_D = 0

**More accurate**

.. math:: 

	I_D = \mu C_{ox} \frac{W}{L} V_T^2 (n-1) e^{\frac{V_{GS}-V_t}{nV_T}} (1-e^{\frac{-V_{DS}}{V_T}})

where :math:`n = \frac{C_{ox} + C_{dep}}{C_{ox}} > 1`

We can also define the subthreshold swing :math:`S` , that is the change in :math:`V_{GS}` needed for a 10 times change in current.

.. math:: I_D \propto e^{\frac{V_{GS}}{nV_T}}

.. math::  \Delta V_{GS} = n V_T \ln{10}

.. math:: S = n \times 60 \text{mV per decade}

Linear region
-------------
Also known as the triode mode, or ohmic mode.

Conditional on :math:`V_{GS} > V_t` and :math:`V_{DS} < V_{GS}-V_t`.

.. math::

	I_D = \mu C_{ox} \frac{W}{L} \left[(V_{GS} - V_t)V_{DS} - \frac{V_{DS}^2}{2}\right] (1+ \lambda V_{DS})


Saturation region
-----------------
Conditional on :math:`V_{GS} > V_t` and :math:`V_{DS} > V_{GS}-V_t`.

DC current:

.. math::

	I_D = \frac{1}{2} \mu C_{ox} \frac{W}{L} (V_{GS} - V_t)^2 (1+ \lambda V_{DS})

Small signal transconductance:

.. math::
	g_m=

**Term Definitions and Useful Equations**

:math:`V_{GS}-V_t` is the overdrive voltage, also referred to as :math:`V_{DSsat}`, or :math:`V_{ov}`.

:matH:`V_T` is the thermal voltage :math:`V_T=kT/q`, where  :math:`T` is the absolute temperature in Kelvin, :math:`k` is the Boltzman constant and :math:`q` is the elementary charge. 

:math:`V_T=25.86` mV at 300K.

:math:`K'=\mu_0 C_{ox}`

:math:`C_{ox}=\epsilon_{ox} / t_{ox}`

:math:`\beta = K' \frac{W}{L}`

.. Models
.. ======
.. BSIM
.. ----

.. EKV
.. ---

