from statistics import mean
from pwptemp.InitCond import init_cond
from pwptemp.HeatCoefficients import heat_coef
from pwptemp.LinearSystem import temp_calc

def temp_time(n, well, tvd, deltaz, zstep):
    """
    :param n: # circulating time, h
    :return: circulation time values
    """
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    tstep = 1
    deltat = tcirc / tstep

    Tdsio, Tdso, Tao, Tcsgo, Tsro, Tfm = init_cond(well.ts, well.riser, well.wtg, well.gt, zstep, tvd, deltaz)

    c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5w, c5e, c5t, c4z1, c4e1, \
    c4w1, c4t1, c5z1, c5w1, c5e1, c5t1, c4z2, c4e2, c4w2, c4t2, c5z2, c5w2, c5e2, c5t2, c4z3, c4e3, c4w3, c4t3, c5z3, \
    c5w3, c5e3, c5t3, c4z4, c4e4, c4w4, c4t4, c5z4, c5w4, c5e4, c5t4, c4z5, c4e5, c4w5, c4t5, c5z5, c5w5, c5e5, \
    c5t5 = heat_coef(well.rhol, well.cl, well.vp, well.h1, well.r1, well.qp, well.lambdal, well.r2, well.h2, well.rhod,
                     well.cd, well.va, well.r3, well.h3, well.qa, well.lambdar, well.lambdarw, well.lambdaw, well.cr,
                     well.cw, well.rhor, well.rhow, well.r4, well.r5, well.rfm, well.lambdac, well.lambdacsr,
                     well.lambdasr, well.lambdasrfm, well.cc, well.csr, well.rhoc, well.rhosr, well.rhosr2, well.rhosr3,
                     well.lambdafm, well.cfm, well.rhofm, deltaz, deltat, well.lambdasr2, well.lambdasr3,
                     well.lambdacsr2, well.lambdacsr3, well.lambdasrfm2, well.lambdasrfm3, well.csr2, well.csr3)

    Tdsi, Ta, Tr, Tcsg, Tsr = temp_calc(well.tin, Tdsio, Tdso, Tao, Tcsgo, Tsro, c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t,
                                        c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t,
                                        c5z, c5w, c5e, c5t, c4z1, c4e1, c4w1, c4t1, c5z1, c5w1, c5e1, c5t1, c4z2, c4e2,
                                        c4w2, c4t2, c5z2, c5w2, c5e2, c5t2, c4z3,
                                        c4e3, c4w3, c4t3, c5z3, c5w3, c5e3, c5t3, c4z4, c4e4, c4w4, c4t4, c5z4, c5w4,
                                        c5e4, c5t4, c4z5, c4e5, c4w5, c4t5, c5z5,
                                        c5w5, c5e5, c5t5, zstep, well.riser, well.csgc, well.csgs, well.csgi)

    return Tdsi, Ta, Tr, Tcsg, Tsr, Tfm, time


def stab_time(well, tvd, deltaz, zstep):
    Ta = []
    for n in range(1,3):
        Ta.append(temp_time(n, well, tvd, deltaz, zstep)[1])

    valor = mean(Ta[0]) - mean(Ta[1])
    finaltime = 2

    while abs(valor) >= 0.01:
        Ta.append(temp_time(finaltime+1, well, tvd, deltaz, zstep)[1])
        valor = mean(Ta[finaltime]) - mean(Ta[finaltime-1])
        finaltime = finaltime + 1

    Tbot = []
    Tout = []

    for n in range(finaltime):
        Tbot.append(Ta[n][-1])
        Tout.append(Ta[n][0])

    return finaltime, Tbot, Tout


def temp_times(n, x, well, tvd, deltaz, zstep):

    temps = []
    for i in range(1, n+1, x):
        Tdsi, Ta, Tr, Tcsg, Tsr, Tfm, time = temp_time(i, well, tvd, deltaz, zstep)
        current_temp = [Tdsi, Ta, Tr, Tcsg, Tsr, Tfm, time]
        temps.append(current_temp)

    return temps

