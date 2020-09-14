import numpy as np


def temp_time(n, well, log=True, units='metric', time_delta=900):
    """
    Function to calculate the well temperature distribution during certain production time (n)
    :param n: production time, hours
    :param well: a well object created with the function set_well() from input.py
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :param units: system of units ('metric' or 'english')
    :param time_delta: duration of each time step (seconds)
    :return: a well temperature distribution object
    """
    from .initcond import init_cond
    from .heatcoefficients import heat_coef
    from .linearsystem import temp_calc
    from ..plot import profile
    from math import log, nan
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    deltat = 60 * time
    if type(time_delta) == int:
        deltat = time_delta
    tstep = int(tcirc / deltat)
    ic = init_cond(well)
    tfm = ic.tfm
    tt = ic.tto
    t3 = ic.tco

    well = well.define_viscosity(ic)
    well = well.define_density(ic, cond=0)

    hc = heat_coef(well, deltat, tt, t3)
    temp = temp_calc(well, ic, hc)
    temp.tft = temp.tt = temp.ta = temp.t3 = temp.tsr = tfm
    for x in range(len(tfm)):
        if temp.tc[x] != nan:
            temp.tc[x] = tfm[x]
        if temp.tr[x] != nan:
            temp.tr[x] = tfm[x]
        if temp.toh[x] != nan:
            temp.toh[x] = tfm[x]

    temp_initial = temp
    temp_initial.tft = ic.tfm
    temp_initial.tt = ic.tfm
    temp_initial.ta = ic.tfm

    temp_log = [temp_initial, temp]
    time_log = [0, deltat / 3600]

    for x in range(tstep-1):
        well = well.define_viscosity(ic)
        well = well.define_density(ic, cond=1)

        ic.tfto = temp.tft
        ic.tto = temp.tt
        ic.tao = temp.ta
        ic.tco = temp.t3
        ic.tsr = temp.tsr
        hc_new = heat_coef(well, deltat, ic.tto, ic.tco)
        temp = temp_calc(well, ic, hc_new)

        if units == 'english':
            temp.tft_output = [(i/(5/9)+32) for i in temp.tft]
            temp.tt_output = [(i/(5/9)+32) for i in temp.tt]
            temp.ta_output = [(i/(5/9)+32) for i in temp.ta]
            temp.tc_output = [(i/(5/9)+32) for i in temp.tc if type(i) == np.float64]
            temp.tr_output = [(i/(5/9)+32) for i in temp.tr if type(i) == np.float64]
            temp.tsr_output = [(i/(5/9)+32) for i in temp.tsr]
            temp.md_output = [i*3.28 for i in well.md]

        if log:
            temp_log.append(temp)
            time_log.append(time_log[-1] + time_log[1])

    if units == 'english':
        temp.tft = temp.tft_output
        temp.tt = temp.tt_output
        temp.ta = temp.ta_output
        temp.tc = temp.tc_output
        temp.tr = temp.tr_output
        temp.sr = temp.tsr_output
        temp.md = temp.md_output
        tfm = [(i / (5 / 9) + 32) for i in tfm]

    class TempDist(object):
        def __init__(self):
            self.tft = temp.tft
            self.tt = temp.tt
            self.ta = temp.ta
            self.tc = temp.tc
            self.tr = temp.tr
            self.tsr = temp.tsr
            self.tfm = tfm
            self.time = time
            self.md = well.md
            self.riser = well.riser
            self.deltat = deltat
            self.csgs_reach = temp.csgs_reach
            if log:
                self.temp_log = temp_log
                self.time_log = time_log

        def well(self):
            return well

        def plot(self):
            return profile(self, units, operation='production')

        def behavior(self):
            temp_behavior_production = temp_behavior(self)
            return temp_behavior_production

    return TempDist()


def temp_behavior(temp_dist):

    ta = [x.ta for x in temp_dist.temp_log]

    tout = []

    for n in range(len(ta)):
        tout.append(ta[n][0])

    class Behavior(object):
        def __init__(self):
            self.finaltime = temp_dist.time
            self.tout = tout
            self.tfm = temp_dist.tfm
            self.time = temp_dist.time_log

        def plot(self):
            from ..plot import behavior
            return behavior(self, operation='production')

    return Behavior()


def temp(well_trajectory, n, casings=[], d_openhole=0.216, change_input={}, log=False, units='metric', time_delta=900):
    """
    Main function to calculate the well temperature distribution during production operation. This function allows to
    set the wellpath and different parameters involved.
    :param well_trajectory: wellbore trajectory object
    :param n: production time, hours
    :param casings: list of dictionaries with casings characteristics (od, id and depth)
    :param change_input: dictionary with parameters to set.
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :param units: system of units ('metric' or 'english')
    :param time_delta: duration of each time step (seconds)
    :return: a well temperature distribution object
    """
    from .input import data, set_well

    tdata = data(casings, d_openhole, units)
    for x in change_input:   # changing default values
        if x in tdata:
            tdata[x] = change_input[x]
        else:
            raise TypeError('%s is not a parameter' % x)

    well = set_well(tdata, well_trajectory, units)
    temp_distribution = temp_time(n, well, log, units, time_delta)

    return temp_distribution


def input_info(about='all'):
    from .input import info
    info(about)
