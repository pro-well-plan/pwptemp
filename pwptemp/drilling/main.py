from statistics import mean
import numpy as np
from pwptemp.drilling.initcond import init_cond
from pwptemp.drilling.heatcoefficients import heat_coef
from pwptemp.drilling.linearsystem import temp_calc
from pwptemp.drilling.plot import profile, behavior
from pwptemp.drilling.analysis import param_effect


def temp_time(n, well):
    """
    :param n:
    :param well:
    :return:
    """
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    tstep = 1
    deltat = tcirc / tstep
    ic = init_cond(well)
    hc = heat_coef(well, deltat)
    tc = temp_calc(well, ic, hc)

    class TempDist(object):
        def __init__(self):
            self.tdsi = tc.tdsi
            self.tds = tc.tds
            self.ta = tc.ta
            self.tr = tc.tr
            self.tcsg = tc.tcsg
            self.toh = tc.toh
            self.tsr = tc.tsr
            self.tfm = ic.tfm
            self.time = time
            self.md = well.md
            self.riser = well.riser
            self.csgs_reach = tc.csgs_reach

        def plot(self):
            profile(self)

        def effect(self):
            effect = param_effect(self, well)
            return effect

        def well(self):
            return well

    return TempDist()


def stab_time(well):
    ta = []
    for n in range(1, 3):
        ta.append(temp_time(n, well).ta)

    valor = mean(ta[0]) - mean(ta[1])
    finaltime = 2

    while abs(valor) >= 0.01:
        ta.append(temp_time(finaltime+1, well).ta)
        valor = mean(ta[finaltime]) - mean(ta[finaltime-1])
        finaltime = finaltime + 1

    tbot = []
    tout = []

    for n in range(finaltime):
        tbot.append(ta[n][-1])
        tout.append(ta[n][0])

    class StabTime(object):
        def __init__(self):
            self.finaltime = finaltime
            self.tbot = tbot
            self.tout = tout
            self.tfm = init_cond(well).tfm

        def plot(self):
            behavior(self)

    return StabTime()


def temp_times(n, x, well):

    temps = []
    for i in list(np.arange(x, n+x, x)):
        current_temp = temp_time(i, well)
        temps.append(current_temp)

    return temps
