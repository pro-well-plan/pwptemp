from statistics import mean
from pwptemp.InitCond import init_cond
from pwptemp.HeatCoefficients import heat_coef
from pwptemp.LinearSystem import temp_calc

def temp_time(n,mw,tvd,deltaz,zstep):
    """
    :param n: # circulating time, h
    :return: circulation time values
    """
    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    tstep = 1
    deltat = tcirc / tstep

    Tdsio, Tdso, Tao, Tcsgo, Tsro, Tfm = init_cond(mw.ts, mw.riser, mw.wtg, mw.gt, zstep, tvd, deltaz)

    c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5w, c5e, c5t, c4z1, c4e1, \
    c4w1, c4t1, c5z1, c5w1, c5e1, c5t1, c4z2, c4e2, c4w2, c4t2, c5z2, c5w2, c5e2, c5t2, c4z3, c4e3, c4w3, c4t3, c5z3, \
    c5w3, c5e3, c5t3, c4z4, c4e4, c4w4, c4t4, c5z4, c5w4, c5e4, c5t4, c4z5, c4e5, c4w5, c4t5, c5z5, c5w5, c5e5, c5t5 = heat_coef(
        mw.rhol, mw.cl, mw.vp, mw.h1, mw.r1, mw.qp, mw.lambdal, mw.r2, mw.h2, mw.rhod, mw.cd, mw.va, mw.r3, mw.h3,
        mw.qa, mw.lambdar, mw.lambdarw,
        mw.lambdaw, mw.cr, mw.cw, mw.rhor, mw.rhow, mw.r4, mw.r5, mw.rfm, mw.lambdac, mw.lambdacsr, mw.lambdasr,
        mw.lambdasrfm, mw.cc, mw.csr,
        mw.rhoc, mw.rhosr, mw.lambdafm, mw.cfm, mw.rhofm, deltaz, deltat, mw.lambdasr2, mw.lambdasr3, mw.lambdacsr2,
        mw.lambdacsr3, mw.lambdasrfm2,
        mw.lambdasrfm3, mw.csr2, mw.csr3)

    Tdsi, Ta, Tr, Tcsg, Tsr = temp_calc(mw.tin, Tdsio, Tdso, Tao, Tcsgo, Tsro, c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t,
                                        c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t,
                                        c5z, c5w, c5e, c5t, c4z1, c4e1, c4w1, c4t1, c5z1, c5w1, c5e1, c5t1, c4z2, c4e2,
                                        c4w2, c4t2, c5z2, c5w2, c5e2, c5t2, c4z3,
                                        c4e3, c4w3, c4t3, c5z3, c5w3, c5e3, c5t3, c4z4, c4e4, c4w4, c4t4, c5z4, c5w4,
                                        c5e4, c5t4, c4z5, c4e5, c4w5, c4t5, c5z5,
                                        c5w5, c5e5, c5t5, zstep, mw.riser, mw.csgc, mw.csgs, mw.csgi)

    return Tdsi, Ta, Tr, Tcsg, Tsr, Tfm


def stab_time():
    Ta = []
    for n in range(1,3):
        Ta.append(temp_time(n)[1])

    valor = mean(Ta[0]) - mean(Ta[1])
    finaltime = 2

    while abs(valor) >= 0.01:
        Ta.append(temp_time(finaltime+1)[1])
        valor = mean(Ta[finaltime]) - mean(Ta[finaltime-1])
        finaltime = finaltime+1

    Tbot = []
    Tout = []

    for n in range(finaltime):
        Tbot.append(Ta[[n][-1]])
        Tout.append(Ta[[n][0]])

    return finaltime, Tbot, Tout


