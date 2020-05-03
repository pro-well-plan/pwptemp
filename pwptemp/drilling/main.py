def temp_time(n, well, log=False, units='metric'):
    """
    Function to calculate the well temperature distribution during drilling at a certain circulation time n.
    :param n: circulation time, hours
    :param well: a well object created from the function set_well()
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :return: a temperature distribution object
    """
    from .initcond import init_cond
    from .heatcoefficients import heat_coef
    from .linearsystem import temp_calc
    from .plot import profile
    from math import log, nan
    import numpy as np
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    deltat = 60
    tstep = int(tcirc / deltat)
    ic = init_cond(well)
    tfm = ic.tfm
    well = well.define_density(ic, cond=0)

    hc = heat_coef(well, deltat)
    temp = temp_calc(well, ic, hc)
    temp.tdsi = temp.tds = temp.ta = temp.t3 = temp.tsr = tfm
    for x in range(len(tfm)):
        if temp.tcsg[x] != nan:
            temp.tcsg[x] = tfm[x]
        if temp.tr[x] != nan:
            temp.tr[x] = tfm[x]
        if temp.toh[x] != nan:
            temp.toh[x] = tfm[x]

    temp_log = [temp]
    time_log = [deltat/60]

    for x in range(tstep):
        well = well.define_density(ic, cond=1)
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
            time_log.append((x+60)/60)

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
                self.temp_log = temp_log[::60]
                self.time_log = time_log[::60]

        def plot(self, tdsi=True, ta=True, tr=False, tcsg=False, tfm=True, sr=False):
            profile(self, tdsi, ta, tr, tcsg, tfm, sr, units)

        def well(self):
            return well

        def behavior(self):
            temp_behavior_drilling = temp_behavior(self)
            return temp_behavior_drilling

        def plot_multi(self, tdsi=True, ta=False, tr=False, tcsg=False, tfm=False, tsr=False):
            plot_multitime(self, tdsi, ta, tr, tcsg, tfm, tsr)

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

        def plot(self):
            from .plot import behavior
            behavior(self)

    return Behavior()


def plot_multitime(temp_dist, tdsi=True, ta=False, tr=False, tcsg=False, tfm=False, tsr=False):
    from .plot import profile_multitime

    values = temp_dist.temp_log
    times = [x for x in temp_dist.time_log]
    profile_multitime(temp_dist, values, times, tdsi=tdsi, ta=ta, tr=tr, tcsg=tcsg, tfm=tfm, tsr=tsr)


# BUILDING GENERAL FUNCTIONS FOR DRILLING MODULE


def temp(n, mdt=3000, casings=[], wellpath_data=[], d_openhole=0.216, grid_length=50, profile='V', build_angle=1, kop=0,
         eob=0, sod=0, eod=0, kop2=0, eob2=0, change_input={}, log=False, visc_eq=True, units='metric'):
    """
    Main function to calculate the well temperature distribution during drilling operation. This function allows to
    set the wellpath and different parameters involved.
    :param n: circulation time, hours
    :param mdt: measured depth of target, m
    :param casings: list of dictionaries with casings characteristics (od, id and depth)
    :param wellpath_data: load own wellpath as a list
    :param d_openhole: diameter of open hole section, m
    :param grid_length: number of cells through depth
    :param profile: type of well to generate. Vertical ('V'), S-type ('S'), J-type ('J') and Horizontal ('H1' or 'H2')
    :param build_angle: build angle, °
    :param kop: kick-off point, m
    :param eob: end of build, m
    :param sod: start of drop, m
    :param eod: end of drop, m
    :param kop2: kick-off point 2, m
    :param eob2: end of build 2, m
    :param change_input: dictionary with parameters to set.
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :param visc_eq: boolean to use the same viscosity in the pipe and annular
    :return: a well temperature distribution object
    """
    from .input import data, set_well
    from .. import wellpath

    tdata = data(casings, d_openhole, units)

    for x in change_input:   # changing default values
        if x in tdata:
            tdata[x] = change_input[x]
        else:
            raise TypeError('%s is not a parameter' % x)

    if len(wellpath_data) == 0:
        depths = wellpath.get(mdt, grid_length, profile, build_angle, kop, eob, sod, eod, kop2, eob2, units)
    else:
        depths = wellpath.load(wellpath_data, grid_length, units)
    well = set_well(tdata, depths, visc_eq, units)
    temp_distribution = temp_time(n, well, log, units)

    return temp_distribution


def input_info(about='all'):
    from .input import info
    info(about)
