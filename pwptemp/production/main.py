def temp_time(n, well):
    """
    Function to calculate the well temperature distribution during certain production time (n)
    :param n: production time, hours
    :param well: a well object created with the function set_well() from input.py
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

    from .fluid import initial_density, calc_density
    well.rhof, rhof_initial = initial_density(well, ic, section='tubing')
    well.rhof_a, rhof_a_initial = initial_density(well, ic, section='annular')
    well.re_p = [x * well.vp * 2 * well.r1 / well.visc for x in well.rhof]  # Reynolds number inside tubing
    well.f_p = [1.63 / log(6.9 / x) ** 2 for x in well.re_p]  # Friction factor inside drill pipe
    well.nu_dpi = [0.027 * (x ** (4 / 5)) * (well.pr ** (1 / 3)) * (1 ** 0.14) for x in well.re_p]
    # convective heat transfer coefficients, W/(m^2*°C)
    well.h1 = [well.lambdaf * x / well.dti for x in well.nu_dpi]  # Tubing inner wall

    hc = heat_coef(well, deltat, tt, tc)
    temp = temp_calc(well, ic, hc)
    for x in range(1, tstep):
        well.rhof = calc_density(well, ic, rhof_initial, section='tubing')
        well.rhof_a = calc_density(well, ic, rhof_a_initial, section='annular')
        well.re_p = [x * well.vp * 2 * well.r1 / well.visc for x in well.rhof]  # Reynolds number inside tubing
        well.f_p = [1.63 / log(6.9 / x) ** 2 for x in well.re_p]  # Friction factor inside drill pipe
        well.nu_dpi = [0.027 * (x ** (4 / 5)) * (well.pr ** (1 / 3)) * (1 ** 0.14) for x in well.re_p]
        # convective heat transfer coefficients, W/(m^2*°C)
        well.h1 = [well.lambdaf * x / well.dti for x in well.nu_dpi]  # Tubing inner wall

        ic.tfto = temp.tft
        ic.tto = temp.tt
        ic.tao = temp.ta
        ic.tco = temp.tc
        ic.tsr = temp.tsr
        hc_new = heat_coef(well, deltat, ic.tto, ic.tco)
        temp = temp_calc(well, ic, hc_new)

    class TempDist(object):
        def __init__(self):
            self.tft = temp.tft
            self.tt = temp.tt
            self.ta = temp.ta
            self.tc = temp.tc
            self.tsr = temp.tsr
            self.tfm = tfm
            self.time = time
            self.md = well.md
            self.riser = well.riser
            self.deltat = deltat

        def well(self):
            return well

        def plot(self, sr=True):
            profile(self, sr)

    return TempDist()


def temp(n, mdt=3000, casings=[], wellpath_data=[], d_openhole=0.216, grid_length=50, profile='V', build_angle=1, kop=0,
         eob=0, sod=0, eod=0, kop2=0, eob2=0, change_input={}):
    """
    Main function to calculate the well temperature distribution during production operation. This function allows to
    set the wellpath and different parameters involved.
    :param n: production time, hours
    :param mdt: measured depth of target
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
    temp_distribution = temp_time(n, well)

    return temp_distribution
