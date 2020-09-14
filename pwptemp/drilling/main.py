def temp_time(n, well, log=True, units='metric', density_constant=False, time_delta=None, fric=0.24):
    """
    Function to calculate the well temperature distribution during drilling at a certain circulation time n.
    :param n: circulation time, hours
    :param well: a well object created from the function set_well()
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :param units: system of units ('metric' or 'english')
    :param density_constant: keep the fluid density as a constant
    :param time_delta: duration of each time step (seconds)
    :param fric: sliding friction coefficient between DP-wellbore.
    :return: a temperature distribution object
    """
    from .initcond import init_cond
    from .heatcoefficients import heat_coef
    from .linearsystem import temp_calc
    from ..plot import profile
    from math import log, nan
    import numpy as np
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    deltat = 60 * time
    if type(time_delta) == int:
        deltat = time_delta
    tstep = int(tcirc / deltat)
    ic = init_cond(well)
    tfm = ic.tfm
    well = well.define_viscosity(ic)
    well = well.define_density(ic, cond=0, fric=fric)
    if density_constant:
        deltat = tcirc
        tstep = 1
    hc = heat_coef(well, deltat)
    temp = temp_calc(well, ic, hc)

    if not density_constant:
        temp.tdsi = temp.tds = temp.ta = temp.t3 = temp.tsr = tfm
        for x in range(len(tfm)):
            if temp.tcsg[x] != nan:
                temp.tcsg[x] = tfm[x]
            if temp.tr[x] != nan:
                temp.tr[x] = tfm[x]
            if temp.toh[x] != nan:
                temp.toh[x] = tfm[x]

    temp_initial = temp
    temp_initial.tdsi = ic.tfm
    temp_initial.tds = ic.tfm
    temp_initial.ta = ic.tfm

    temp_log = [temp_initial, temp]
    time_log = [0, deltat / 3600]

    for x in range(tstep-1):
        if tstep > 1:
            well = well.define_viscosity(ic)
            well = well.define_density(ic, cond=1, fric=fric)
            ic.tdsio = temp.tdsi
            ic.tdso = temp.tds
            ic.tao = temp.ta
            ic.tcsgo = temp.t3
            ic.tsr = temp.tsr
            hc_new = heat_coef(well, deltat)
            temp = temp_calc(well, ic, hc_new)

        if units == 'english':
            temp.tdsi_output = [(i/(5/9)+32) for i in temp.tdsi]
            temp.tds_output = [(i/(5/9)+32) for i in temp.tds]
            temp.ta_output = [(i/(5/9)+32) for i in temp.ta]
            temp.tcsg_output = [(i/(5/9)+32) for i in temp.tcsg if type(i) == np.float64]
            temp.tr_output = [(i/(5/9)+32) for i in temp.tr if type(i) == np.float64]
            temp.tsr_output = [(i/(5/9)+32) for i in temp.tsr]
            temp.md_output = [i*3.28 for i in well.md]

        if log:
            temp_log.append(temp)
            time_log.append(time_log[-1] + time_log[1])

    if units == 'english':
        temp.tdsi = temp.tdsi_output
        temp.tds = temp.tds_output
        temp.ta = temp.ta_output
        temp.tcsg = temp.tcsg_output
        temp.tr = temp.tr_output
        temp.sr = temp.tsr_output
        temp.md = temp.md_output
        tfm = [(i / (5 / 9) + 32) for i in tfm]

    class TempDist(object):
        def __init__(self):
            self.tdsi = temp.tdsi
            self.tds = temp.tds
            self.ta = temp.ta
            self.tr = temp.tr
            self.tcsg = temp.tcsg
            self.toh = temp.toh
            self.tsr = temp.tsr
            self.tfm = tfm
            self.time = time
            self.md = well.md
            self.riser = well.riser
            self.csgs_reach = temp.csgs_reach
            self.deltat = deltat
            if log:
                self.temp_log = temp_log
                self.time_log = time_log

        def plot(self):
            return profile(self, units, operation='drilling')

        def well(self):
            return well

        def behavior(self):
            temp_behavior_drilling = temp_behavior(self)
            return temp_behavior_drilling

    return TempDist()


def temp_behavior(temp_dist):

    ta = [x.ta for x in temp_dist.temp_log]
    tbot = []
    tout = []

    for n in range(len(ta)):
        tbot.append(ta[n][-1])
        tout.append(ta[n][0])

    class Behavior(object):
        def __init__(self):
            self.finaltime = temp_dist.time
            self.tbot = tbot
            self.tout = tout
            self.tfm = temp_dist.tfm
            self.time = temp_dist.time_log

        def plot(self):
            from ..plot import behavior
            return behavior(self, operation='drilling')

    return Behavior()

# BUILDING GENERAL FUNCTIONS FOR DRILLING MODULE


def temp(well_trajectory, n, casings=[], d_openhole=0.216, change_input={}, log=True, visc_eq=True, units='metric',
         density_constant=False, time_delta=None, fric=0.24):
    """
    Main function to calculate the well temperature distribution during drilling operation. This function allows to
    set the wellpath and different parameters involved.
    :param well_trajectory: wellbore trajectory object
    :param n: circulation time, hours
    :param casings: list of dictionaries with casings characteristics (od, id and depth)
    :param d_openhole: diameter of open hole section, m
    :param change_input: dictionary with parameters to set.
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :param visc_eq: boolean to use the same viscosity in the pipe and annular
    :param units: system of units ('metric' or 'english')
    :param density_constant: keep the fluid density as a constant
    :param time_delta: duration of each time step (seconds)
    :param fric: sliding friction coefficient between DP-wellbore.
    :return: a well temperature distribution object
    """
    from .input import data, set_well

    tdata = data(casings, d_openhole, units)

    for x in change_input:   # changing default values
        if x in tdata:
            tdata[x] = change_input[x]
        else:
            raise TypeError('%s is not a parameter' % x)

    well = set_well(tdata, well_trajectory, visc_eq, units)
    temp_distribution = temp_time(n, well, log, units, density_constant, time_delta, fric)

    return temp_distribution


def input_info(about='all'):
    from .input import info
    info(about)
