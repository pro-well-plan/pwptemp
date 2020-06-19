def calc_torque_drag(well, fric=0.24):
    """
    Function to generate the torque and drag profiles. Model Source: SPE-11380-PA
    :param well: a well object with rhod (drill string density), r1 (inner diameter of drill string), r2 (outer diameter
    of drill string), r3 (diameter of the first casing layer or borehole), rhof (fluid density), deltaz (length per pipe
    segment), wob (weight on bit), tbit (torque on bit), azimuth (for each segment) and inclination (for each segment).
    :param fric: sliding friction coefficient between DP-wellbore.
    :return: two lists, drag force and torque
    """

    from math import pi, sin, cos, radians

    unit_pipe_weight = well.rhod * 9.81 * pi * (well.r2 ** 2 - well.r1 ** 2)
    area_a = pi * ((well.r3 ** 2) - (well.r2 ** 2))
    area_ds = pi * (well.r1 ** 2)
    buoyancy = [1 - ((x * area_a) - (x * area_ds)) / (well.rhod * (area_a - area_ds)) for x in well.rhof]
    w = [unit_pipe_weight * well.deltaz * x for x in buoyancy]
    w[0] = 0

    force_1, force_2, force_3 = [well.wob], [well.wob], [well.wob]      # Force at bottom
    torque_1, torque_2, torque_3 = [well.tbit], [well.tbit], [well.tbit]        # Torque at bottom

    for x in reversed(range(1, well.zstep)):
        delta_azi = radians(well.azimuth[x] - well.azimuth[x-1])
        delta_inc = radians(well.inclination[x] - well.inclination[x-1])
        inc_avg = radians((well.inclination[x] + well.inclination[x-1]) / 2)

        # NET NORMAL FORCES
        fn_1 = ((force_1[-1] * delta_azi * sin(inc_avg)) ** 2
                + (force_1[-1] * delta_inc + w[x] * sin(inc_avg)) ** 2) ** 0.5
        fn_2 = ((force_2[-1] * delta_azi * sin(inc_avg)) ** 2
                + (force_2[-1] * delta_inc + w[x] * sin(inc_avg)) ** 2) ** 0.5
        fn_3 = ((force_3[-1] * delta_azi * sin(inc_avg)) ** 2
                + (force_3[-1] * delta_inc + w[x] * sin(inc_avg)) ** 2) ** 0.5

        # DRAG FORCE CALCULATIONS
        delta_ft_1 = w[x] * cos(inc_avg) - fric * fn_1
        delta_ft_2 = w[x] * cos(inc_avg)
        delta_ft_3 = w[x] * cos(inc_avg) + fric * fn_3

        ft_1 = force_1[-1] + delta_ft_1
        ft_2 = force_2[-1] + delta_ft_2
        ft_3 = force_3[-1] + delta_ft_3

        force_1.append(ft_1)
        force_2.append(ft_2)
        force_3.append(ft_3)

        # TORQUE CALCULATIONS
        delta_torque_1 = fric * fn_1 * well.r2
        delta_torque_2 = fric * fn_2 * well.r2
        delta_torque_3 = fric * fn_3 * well.r2

        t_1 = torque_1[-1] + delta_torque_1
        t_2 = torque_2[-1] + delta_torque_2
        t_3 = torque_3[-1] + delta_torque_3

        torque_1.append(t_1)
        torque_2.append(t_2)
        torque_3.append(t_3)

    # Units conversion: N to kN
    force = [[i/1000 for i in force_1[::-1]], [i/1000 for i in force_2[::-1]], [i/1000 for i in force_3[::-1]]]
    torque = [[i/1000 for i in torque_1[::-1]], [i/1000 for i in torque_2[::-1]], [i/1000 for i in torque_3[::-1]]]

    return force, torque

