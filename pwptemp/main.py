from statistics import mean
from pwptemp.initcond import init_cond
from pwptemp.heatcoefficients import heat_coef
from pwptemp.linearsystem import temp_calc


def temp_time(n, well):
    """
    :param n: # circulating time, h
    :return: circulation time values
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
            self.ta = tc.ta
            self.tr = tc.tr
            self.tcsg = tc.tcsg
            self.toh = tc.toh
            self.tsr = tc.tsr
            self.tfm = ic.tfm
            self.time = time

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
            self.tfm = well.tfm

    return StabTime()


def temp_times(n, x, well):

    temps = []
    for i in range(1, n+1, x):
        x = temp_time(i, well)
        current_temp = [x.tdsi, x.ta, x.tr, x.tcsg, x.tsr, x.tfm, x.time]
        temps.append(current_temp)

    return temps
