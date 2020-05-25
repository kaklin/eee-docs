===============
Silicon Bandgap
===============

Dependence on temperature [#]_
------------------------------

.. math::
    E_g(T) = E_g(0) - \frac{\alpha T^2}{T + \beta }

where for silicon :math:`E_g(0)` is 1.166eV, :math:`\alpha` and :math:`\beta` are empirical fitting parameters 0.473meV/K and 636K respectively.

.. plot:: physics/bandgap_vs_temp.py

.. [#] https://ecee.colorado.edu/~bart/book/book/chapter2/ch2_3.htm
