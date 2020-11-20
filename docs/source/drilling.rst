Well Temperature Distribution while Drilling
============================================

.. autofunction:: pwptemp.calc_temp

.. autofunction:: pwptemp.temperature_behavior

Example
-------

.. code-block:: python

    >>> import pwptemp as pt
    >>> import well_profile as wp

    >>> trajectory = wp.load('trajectory1.xlsx', equidistant=True)      # using well_profile to load a trajectory

    >>> casings = [{'od': 8, 'id':7, 'depth': 1200},        # creating 3 casings with respective parameters
    >>>            {'od': 10, 'id':9, 'depth': 1500},       # diameter [in] and depth [m]
    >>>            {'od': 12, 'id':11, 'depth': 2400}]

    >>> rop_list = [50, 45, 40, 35]     # setting respective ROP [m/h] for each section

    >>> well = pt.calc_temp(trajectory,     # calculate the well temperature distribution using pwptemp
    >>>                     casings,
    >>>                     set_inputs={'water_depth': 0, 'temp_inlet': 20, 'rop':rop_list}

    >>> pt.plot_distribution(well).show()

|temp_drill|

|temp_behavior|

.. |temp_drill| image:: /figures/temp_drill.png
                    :scale: 85%

.. |temp_behavior| image:: /figures/temp_behavior.png
                    :scale: 85%

.. admonition:: Notice!

    The total time of drilling is calculated based on the ROP's set for the sections. The simulation
    assumes a break after each section is drilled (here is when casing is run and cemented) so the temperature
    becomes stable again. i.e. for this particular case, it takes 92.9 hours only *drilling* the whole wellbore.

The table below shows the available inputs that can be set when using the parameter *set_inputs*

+------------------+------------------+
|       Name       |      Units       |
+==================+==================+
|    temp_inlet    | °C               |
+------------------+------------------+
|   temp_surface   | °C               |
+------------------+------------------+
|   water_depth    | in               |
+------------------+------------------+
|     pipe_id      | in               |
+------------------+------------------+
|     pipe_od      | in               |
+------------------+------------------+
|     riser_id     | in               |
+------------------+------------------+
|     riser_od     | in               |
+------------------+------------------+
| fm_diam          | in               |
+------------------+------------------+
| flowrate         | m3/min           |
+------------------+------------------+
| Thermal Conductivities------------- |
+------------------+------------------+
| tc_fluid         |  W / (m °C)      |
+------------------+------------------+
| tc_csg           | W / (m °C)       |
+------------------+------------------+
| tc_cem           | W / (m °C)       |
+------------------+------------------+
| tc_pipe          | W / (m °C)       |
+------------------+------------------+
| tc_fm            | W / (m °C)       |
+------------------+------------------+
| tc_riser         | W / (m °C)       |
+------------------+------------------+
| tc_seawater      | W / (m °C)       |
+------------------+------------------+
| Specific Heat Capacities----------- |
+------------------+------------------+
| shc_fluid        | J / (kg °C)      |
+------------------+------------------+
| shc_csg          | J / (kg °C)      |
+------------------+------------------+
| shc_cem          | J / (kg °C)      |
+------------------+------------------+
| shc_pipe         | J / (kg °C)      |
+------------------+------------------+
| shc_riser        | J / (kg °C)      |
+------------------+------------------+
| shc_seawater     | J / (kg °C)      |
+------------------+------------------+
| shc_fm           | J / (kg °C)      |
+------------------+------------------+
| Densities-------------------------- |
+------------------+------------------+
| rho_fluid        | sg               |
+------------------+------------------+
| rho_pipe         | sg               |
+------------------+------------------+
| rho_csg          | sg               |
+------------------+------------------+
| rho_riser        | sg               |
+------------------+------------------+
| rho_fm           | sg               |
+------------------+------------------+
| rho_seawater     | sg               |
+------------------+------------------+
| rho_cem          | sg               |
+------------------+------------------+
| Others----------------------------- |
+------------------+------------------+
| th_grad_fm       | °C/m             |
+------------------+------------------+
| th_grad_seawater | °C/m             |
+------------------+------------------+
| hole_diam        | m                |
+------------------+------------------+
| rpm              | rev. per min.    |
+------------------+------------------+
| tbit             | kN*m             |
+------------------+------------------+
| wob              | kN               |
+------------------+------------------+
| rop              | m/h              |
+------------------+------------------+
| an               | in^2             |
+------------------+------------------+
| bit_n            | 0 to 1           |
+------------------+------------------+
| dp_e             | 0 to 1           |
+------------------+------------------+
| thao_o           | Pa               |
+------------------+------------------+
| beta             | Pa               |
+------------------+------------------+
| alpha            | 1/°C             |
+------------------+------------------+
| k                | Pa*s^n           |
+------------------+------------------+
| n                | dimensionless    |
+------------------+------------------+
| visc             | cP               |
+------------------+------------------+


Web Application
---------------

There is also the web-app based on pwptemp:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/op7ZYzlYNn4" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>