from .inputs import inputs_dict
from .well_system import set_well
from .linearsystem import calc_temperature_distribution
from .plot import plot_behavior, plot_distribution


def calc_temp(time, trajectory, casings=None, set_inputs=None, operation='drilling'):
    """
    Function to calculate the well temperature distribution during a specific operation at a certain time.
    :param time: operational time, hours
    :param trajectory: wellbore trajectory object
    :param casings: list of dictionaries with casings characteristics (od, id and depth)
    :param set_inputs: dictionary with parameters to set.
    :param operation: define operation type. ('drilling', 'circulating')
    :return: a well temperature distribution object
    """

    tcirc = time * 3600     # circulating time, s
    time_steps_no = 1200     # dividing time in 120 steps
    time_step = tcirc / time_steps_no       # seconds per time step

    tdata = inputs_dict(casings)

    if set_inputs is not None:
        for x in set_inputs:  # changing default values
            if x in tdata:
                tdata[x] = set_inputs[x]
            else:
                raise TypeError('%s is not a parameter' % x)

    md_initial = 1000
    md_final = trajectory.md[-1]
    rop = (md_final - md_initial) / tcirc       # m/s

    well = set_well(tdata, trajectory)
    log_temp_values(well, initial=True)     # log initial temperature distribution
    well.delta_time = time_step
    time_n = time_step
    bit_position = int((rop * time_n + md_initial) / well.depth_step)  # drill bit position, cell
    print(bit_position)
    well.op = operation
    well = calc_temperature_distribution(well, time_step, bit_position)
    well = define_temperatures(well, bit_position)
    log_temp_values(well, time_n)
    for x in range(time_steps_no - 1):

        if time_steps_no > 1:
            time_n += time_step
            bit_position = int((rop * time_n + md_initial) / well.depth_step)  # drill bit position, cell
            well = calc_temperature_distribution(well, time_step, bit_position)
            well = define_temperatures(well, bit_position)
            log_temp_values(well, time_n)
            well.time = time_n
            #if x in [30, 50, 80, 100]:
                #plot_distribution(well).show()

    well.time = time
    print(bit_position)

    return well


def define_temperatures(well, bit_position):
    """
    Make the temperature values more reachable since they are is a dictionary along the entire well. Once this function
    takes place, the temperatures will be available as lists.
    :return: a dictionary with lists of temperature values and also a list with respective depth points.
    """

    temp_in_pipe = [x['temp'] for x in well.sections[0][:bit_position+1]] + [None] * (well.cells_no - (bit_position + 1))
    temp_pipe = [x['temp'] for x in well.sections[1][:bit_position+1]] + [None] * (well.cells_no - (bit_position + 1))
    temp_annulus = [x['temp'] for x in well.sections[2][:bit_position+1]] + [None] * (well.cells_no - (bit_position + 1))
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


def temperature_behavior(well):
    time = [x['time'] for x in well.temp_log]
    temp_bottom = [x['in_pipe'][-1] for x in well.temp_log]
    temp_outlet = [x['annulus'][0] for x in well.temp_log]
    temp_max = [max(x['annulus']) for x in well.temp_log]
    temp_fm = [well.temp_fm[-1]] * len(time)

    class TempBehavior(object):
        def __init__(self):
            self.time = time
            self.bottom = temp_bottom
            self.outlet = temp_outlet
            self.max = temp_max
            self.formation_td = temp_fm

        def plot(self, title=True):
            fig = plot_behavior(self, title)

            return fig

    return TempBehavior()
