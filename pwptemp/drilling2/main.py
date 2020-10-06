from .inputs import inputs_dict
from .well_system import set_well
from .linearsystem import calc_temperature_distribution


def calc_temp(time, trajectory, casings=None, set_inputs=None):
    tcirc = time * 3600     # circulating time, s
    time_steps_no = 120     # dividing time in 120 steps
    time_step = tcirc / time_steps_no       # seconds per time step

    tdata = inputs_dict(casings)

    if set_inputs is not None:
        for x in set_inputs:  # changing default values
            if x in tdata:
                tdata[x] = set_inputs[x]
            else:
                raise TypeError('%s is not a parameter' % x)

    well = set_well(tdata, trajectory)
    log_temp_values(well, initial=True)     # log initial temperature distribution
    well.delta_time = time_step
    well = calc_temperature_distribution(well, time_step)
    well = define_temperatures(well)
    time = time_step
    log_temp_values(well, time)
    for x in range(time_steps_no - 1):

        if time_steps_no > 1:
            time += time_step
            well = calc_temperature_distribution(well, time_step)
            well = define_temperatures(well)
            log_temp_values(well, time)

    well.time = time

    return well


def define_temperatures(well):
    """
    Make the temperature values more reachable since they are is a dictionary along the entire well. Once this function
    takes place, the temperatures will be available as lists.
    :return: a dictionary with lists of temperature values and also a list with respective depth points.
    """

    temp_in_pipe = [x['temp'] for x in well.sections[0]]
    temp_pipe = [x['temp'] for x in well.sections[1]]
    temp_annulus = [x['temp'] for x in well.sections[2]]
    temp_casing = []
    temp_riser = []
    temp_sr = [x['temp'] for x in well.sections[4]]
    for y, x in enumerate(well.md):

        if well.riser_cells > 0 and x < well.water_depth:
            temp_casing.append(None)
            temp_riser.append(well.sections[3][y]['temp'])
        else:
            temp_riser.append(None)
            if x <= well.casings[0, 2]:
                temp_casing.append(well.sections[3][y]['temp'])
            else:
                temp_casing.append(None)

    well.temperatures = {'md': well.md,
                         'formation': well.temp_fm,
                         'in_pipe': temp_in_pipe,
                         'pipe': temp_pipe,
                         'annulus': temp_annulus,
                         'casing': temp_casing,
                         'riser': temp_riser,
                         'sr': temp_sr}

    return well


def log_temp_values(well, time=0, initial=False):
    time = round(time/3600, 2)
    if initial:
        well.temp_log = [{'time': time,
                          'in_pipe': well.temp_fm,
                          'pipe': well.temp_fm,
                          'annulus': well.temp_fm,
                          'casing': well.temp_fm,
                          'riser': well.temp_fm,
                          'sr': well.temp_fm}]
    else:
        well.temp_log.append(
            {'time': time,
             'in_pipe': [x['temp'] for x in well.sections[0]],
             'pipe': [x['temp'] for x in well.sections[1]],
             'annulus': well.temperatures['annulus'],
             'casing': well.temperatures['casing'],
             'riser': well.temperatures['riser'],
             'sr': well.temperatures['sr']}
        )
