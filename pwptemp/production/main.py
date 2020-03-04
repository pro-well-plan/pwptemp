def temp_time(n, well):
    """
    :param n:
    :param well:
    :return:
    """
    from .initcond import init_cond
    from .heatcoefficients import heat_coef
    from .linearsystem import temp_calc
    from .plot import profile
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    deltat = 60
    tstep = int(tcirc / deltat)
    ic = init_cond(well)
    tfm = ic.tfm
    tt = ic.tto
    tcsg = ic.tcsgo
    hc = heat_coef(well, deltat, tt, tcsg)
    temp = temp_calc(well, ic, hc)
    for x in range(1, tstep):
        ic_new = ic
        ic_new.tfto = temp.tft
        ic.tto = temp.tt
        ic.tao = temp.ta
        ic.tcsgo = temp.tcsg
        ic.tsr = temp.tsr
        tt_new = temp.tt
        tcsg_new = temp.tcsg
        hc_new = heat_coef(well, deltat, tt_new, tcsg_new)
        temp = temp_calc(well, ic_new, hc_new)

    class TempDist(object):
        def __init__(self):
            self.tft = temp.tft
            self.tt = temp.tt
            self.ta = temp.ta
            self.tcsg = temp.tcsg
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


def temp(n, mdt=3000, casings=[], wellpath_data=[], bit=0.216, deltaz=50, profile='V', build_angle=1, kop=0, eob=0,
             sod=0, eod=0, kop2=0, eob2=0, change_input={}):
    from .input import data, set_well
    from .. import wellpath
    tdata = data(casings, bit)
    for x in change_input:   # changing default values
        if x in tdata:
            tdata[x] = change_input[x]
        else:
            raise TypeError('%s is not a parameter' % x)
    if len(wellpath_data) == 0:
        depths = wellpath.get(mdt, deltaz, profile, build_angle, kop, eob, sod, eod, kop2, eob2)
    else:
        depths = wellpath.load(wellpath_data, deltaz)
    well = set_well(tdata, depths)
    temp_distribution = temp_time(n, well)

    return temp_distribution