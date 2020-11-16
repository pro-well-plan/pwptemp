Well Temperature Distribution while Drilling
============================================

.. autofunction:: pwptemp.calc_temp

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

.. admonition:: Notice!

    The total time of drilling is calculated based on the ROP's set for the sections. The simulation
    assumes a break after each section is drilled (here is when casing is run and cemented) so the temperature
    becomes stable again. i.e. for this particular case, it takes 92.9 hours only *drilling* the whole wellbore.

|temp_drill|

.. |temp_drill| image:: /figures/temp_drill.png
                    :scale: 85%

Web Application
---------------

There is also the web-app based on pwptemp:

.. raw:: html

   <iframe width="560" height="315" src="https://www.youtube.com/embed/1oj_e-XhirQ?start=19" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
