def temp_time(n, well, log=False):
    """
    Function to calculate the well temperature distribution during certain production time (n)
    :param n: production time, hours
    :param well: a well object created with the function set_well() from input.py
    :param log: save distributions between initial time and circulation time n (each 1 hour)
    :return: a well temperature distribution object
    """
    from .initcond import init_cond
    from .heatcoefficients import heat_coef
    from .linearsystem import temp_calc
    from .plot import profile
    from math import log
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    deltat = 60
    tstep = int(tcirc / deltat)
    ic = init_cond(well)
    tfm = ic.tfm
    tt = ic.tto
    tc = ic.tco

    well = well.define_density(ic, cond=0)

    hc = heat_coef(well, deltat, tt, tc)
    temp = temp_calc(well, ic, hc)
    temp_log = []

    for x in range(1, tstep):
        well = well.define_density(ic, cond=1)

        ic.tfto = temp.tft
        ic.tto = temp.tt
        ic.tao = temp.ta
        ic.tco = temp.tc
        ic.tsr = temp.tsr
        hc_new = heat_coef(well, deltat, ic.tto, ic.tco)
        temp = temp_calc(well, ic, hc_new)

        if log:
            temp_log.append(temp)

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
            if log:
                self.temp_log = temp_log[::60]

        def well(self):
            return well

        def plot(self, sr=True):
            profile(self, sr)

    return TempDist()


def temp(n, mdt=3000, casings=[], wellpath_data=[], d_openhole=0.216, grid_length=50, profile='V', build_angle=1, kop=0,
         eob=0, sod=0, eod=0, kop2=0, eob2=0, change_input={}, log=False):
    """
    Main function to calculate the well temperature distribution during production operation. This function allows to
    set the wellpath and different parameters involved.
    :param n: production time, hours
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
    :return: a well temperature distribution object
    """
    from .input import data, set_well
    from .. import wellpath
    tdata = data(casings, d_openhole)
    for x in change_input:   # changing default values
        if x in tdata:
            tdata[x] = change_input[x]
        else:
            raise TypeError('%s is not a parameter' % x)
    if len(wellpath_data) == 0:
        depths = wellpath.get(mdt, grid_length, profile, build_angle, kop, eob, sod, eod, kop2, eob2)
    else:
        depths = wellpath.load(wellpath_data, grid_length)
    well = set_well(tdata, depths)
    temp_distribution = temp_time(n, well, log)

    return temp_distribution
