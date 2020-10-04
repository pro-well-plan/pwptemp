import numpy as np
from .inputs import inputs_dict
from .well_system import set_well
from .linearsystem import calc_temperature_distribution


def calc_temp(time, trajectory, casings=None, set_inputs=None):
    tcirc = time * 3600  # circulating time, s
    time_step = tcirc / 120
    tstep = int(tcirc / time_step)

    tdata = inputs_dict(casings)

    if set_inputs is not None:
        for x in set_inputs:  # changing default values
            if x in tdata:
                tdata[x] = set_inputs[x]
            else:
                raise TypeError('%s is not a parameter' % x)

    well = set_well(tdata, trajectory)
    well.delta_time = time_step
    well = calc_temperature_distribution(well, time_step)

    for x in range(tstep - 1):
        if tstep > 1:
            well = calc_temperature_distribution(well, time_step)

    well = define_temperatures(well)
    well.time = time

    return well


def define_temperatures(well):
    """
    Make the temperature values more reachable since they are is a dictionary along the entire well. Once this function
    takes place, the temperatures will be available as lists.
    :return: a dictionary with lists of temperature values and also a list with respective depth points.
    """
    new_md = list(np.linspace(0, well.md[-1], num=int(well.md[-1]/8)))
    temp_fm = []
    temp_in_pipe = []
    temp_pipe = []
    temp_annulus = []
    temp_casing = []
    temp_riser = []
    temp_sr = []
    for x in new_md:
        temp_fm.append(np.interp(x, well.md, well.temp_fm))
        temp_in_pipe.append(np.interp(x, well.md, [x['temp'] for x in well.sections[0]]))
        temp_pipe.append(np.interp(x, well.md, [x['temp'] for x in well.sections[1]]))
        temp_annulus.append(np.interp(x, well.md, [x['temp'] for x in well.sections[2]]))
        temp_sr.append(np.interp(x, well.md, [x['temp'] for x in well.sections[4]]))

        if well.riser_cells > 0 and x < well.water_depth:
            temp_casing.append(None)
            temp_riser.append(np.interp(x, well.md, [x['temp'] for x in well.sections[3]]))
        else:
            temp_riser.append(None)
            if x <= well.casings[0, 2]:
                temp_casing.append(np.interp(x, well.md, [x['temp'] for x in well.sections[3]]))
            else:
                temp_casing.append(None)

    well.temperatures = {'md': new_md,
                         'formation': temp_fm,
                         'in_pipe': temp_in_pipe,
                         'pipe': temp_pipe,
                         'annulus': temp_annulus,
                         'casing': temp_casing,
                         'riser': temp_riser,
                         'sr': temp_sr}

    return well
