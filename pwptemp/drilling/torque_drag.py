from math import pi, sin, cos, radians


def calc_torque_drag(well):
    """
    Function to generate the torque and drag profiles. Model Source: SPE-11380-PA
    :param well: a well object with rhod (drill string density), r1 (inner diameter of drill string), r2 (outer diameter
    of drill string), r3 (diameter of the first casing layer or borehole), rhof (fluid density), deltaz (length per pipe
    segment), wob (weight on bit), tbit (torque on bit), azimuth (for each segment) and inclination (for each segment).
    :return: two lists, drag force and torque
    """
    fric = 0.24
    unit_pipe_weight = well.rhod * 9.81 * pi * (well.r2 ** 2 - well.r1 ** 2)
    area_a = pi * ((well.r3 ** 2) - (well.r2 ** 2))
    area_ds = pi * (well.r1 ** 2)
    buoyancy = [1 - ((x * area_a) - (x * area_ds)) / (well.rhod * (area_a - area_ds)) for x in well.rhof]
    w = [unit_pipe_weight * well.deltaz * x for x in buoyancy]
    w[0] = 0
    force = [well.wob]
    torque = [well.tbit]
    for x in reversed(range(1, well.zstep)):
        delta_azi = radians(well.azimuth[x] - well.azimuth[x-1])
        delta_inc = radians(well.inclination[x] - well.inclination[x-1])
        inc_avg = radians((well.inclination[x] + well.inclination[x-1]) / 2)

        fn = ((force[-1] * delta_azi * sin(inc_avg))**2 + (force[-1] * delta_inc + w[x] * sin(inc_avg))**2) ** 0.5
        delta_ft = w[x] * cos(inc_avg) - fric * fn
        ft = force[-1] + delta_ft

        force.append(ft)

        delta_torque = fric * fn * well.r2
        t = torque[-1] + delta_torque
        torque.append(t)

    return [i/1000 for i in force[::-1]], [i/1000 for i in torque[::-1]]

