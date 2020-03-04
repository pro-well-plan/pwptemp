import math
import numpy as np


def heat_coef(well, deltat):
    sections = len(well.casings) + 2  # sections = # of casings + riser section + open hole section

    # HEAT SOURCE TERMS

        # 1. heat coefficients at bottom

    J = 4.1868    # Joule's constant  [Nm/cal]
    qbit = (1/J)*(1-well.bit_n)*(well.wob*well.rop+2*math.pi*(well.rpm / 60)*well.tbit) \
           + (well.rhol/(2*9.81)) * 0.7 * (well.q/(0.95*well.an))**2

    vbit = well.q / well.an
    cbz = ((well.rhol * well.cl * vbit) / well.deltaz) / 2  # Vertical component (North-South)
    cbe = (2 * well.h1 / well.r3) / 2  # East component
    cb = qbit / well.an  # Heat source term
    cbt = well.rhol * well.cl / deltat  # Time component

        # 2. heat coefficients fluid inside drill pipe

    qp = 2 * math.pi * (well.rpm / 60) * well.t + 0.2 * 2 * (well.f_p * well.rhol * (well.vp ** 2) * (well.md[-1] /
            (well.ddi * 127.094 * 10 ** 6)))

        # 3. heat coefficients fluid inside annular

    qa = (0.085 * (2 * 0.3832 * well.md[-1] / ((well.r3 - well.r2) * (127.094 * 10 ** 6))) * \
         ((2 * (0.7 + 1) * well.q) / (0.7 * math.pi * (well.r3 + well.r2) *
            (well.r3 - well.r2) ** 2)) ** 0.7) * (1 + (3/2) * well.dp_e**2)

    coefficients = []
    for x in range(sections):
        total = []
        # fluid inside drill string
        c1z = ((well.rhol * well.cl * well.vp) / well.deltaz) / 2  # Vertical component (North-South)
        c1e = (2 * well.h1 / well.r1) / 2  # East component
        c1 = qp / (math.pi * (well.r1 ** 2))  # Heat source term
        c1t = well.rhol * well.cl / deltat  # Time component
        total.append([c1z, c1e, c1, c1t])

        # drill string wall
        c2z = (well.lambdad / (well.deltaz ** 2)) / 2  # Vertical component (North-South)
        c2e = (2 * well.r2 * well.h2 / ((well.r2 ** 2) - (well.r1 ** 2))) / 2  # East component
        c2w = (2 * well.r1 * well.h1 / ((well.r2 ** 2) - (well.r1 ** 2))) / 2  # West component
        c2t = well.rhod * well.cd / deltat  # Time component
        total.append([c2z, c2e, c2w, c2t])

        # fluid inside annular
        c3z = (well.rhol * well.cl * well.va / well.deltaz) / 2  # Vertical component (North-South)
        c3e = (2 * well.r3 * well.h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2  # East component
        c3w = (2 * well.r2 * well.h2 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2  # West component
        c3 = qa / (math.pi * ((well.r3 ** 2) - (well.r2 ** 2)))  # Heat source term
        c3t = well.rhol * well.cl / deltat  # Time component
        total.append([c3z, c3e, c3w, c3, c3t])

        if x == 0:
            lambda4 = well.lambdar  # Thermal conductivity of the casing (riser in this section)
            lambda5 = well.lambdaw  # Thermal conductivity of the surrounding space (seawater)
            lambda45 = (lambda4 * (well.r4r - well.r3r) + lambda5 * (well.r5 - well.r4r)) / (
                    well.r5 - well.r3r)  # Comprehensive Thermal conductivity of the casing (riser) and surrounding space (seawater)
            lambda56 = well.lambdaw  # Comprehensive Thermal conductivity of the surrounding space (seawater) and formation (seawater)
            c4 = well.cr  # Specific Heat Capacity of the casing (riser)
            c5 = well.cw  # Specific Heat Capacity of the surrounding space (seawater)
            rho4 = well.rhor  # Density of the casing (riser)
            rho5 = well.rhow  # Density of the surrounding space (seawater)

        if 0 < x < sections - 1:

            # calculation for surrounding space
            # thickness
            tcsr = 0
            tcem = 0
            for i in range(len(well.casings) - x):
                tcsr += (well.casings[i + 1, 0] - well.casings[i + 1, 1]) / 2
                tcem += (well.casings[i + 1, 1] - well.casings[i, 0]) / 2
            if x > 1:
                tcem += (well.casings[len(well.casings)-x+1, 1] - well.casings[len(well.casings)-x, 0]) / 2
            if x == 1:
                tcem += (well.dsro - well.casings[-1, 0])
            xcsr = tcsr / (well.r5 - well.r4)  # fraction of surrounding space that is casing
            xcem = tcem / (well.r5 - well.r4)  # fraction of surrounding space that is cement
            xfm = 1 - xcsr - xcem  # fraction of surrounding space that is formation

            # thermal conductivity
            lambdasr = well.lambdac * xcsr + well.lambdacem * xcem + well.lambdafm * xfm
            lambdacsr = (well.lambdac * (well.r4 - well.r3) + lambdasr * (well.r5 - well.r4)) / (well.r5 - well.r3)
            lambdasrfm = (well.lambdac * (well.r5 - well.r4) + lambdasr * (well.rfm - well.r5)) / (well.rfm - well.r4)

            # Specific Heat Capacity
            csr = (well.cc * tcsr + well.ccem * tcem) / (well.r5 - well.r4)

            # Density
            rhosr = xcsr * well.rhoc + xcem * well.rhocem + xfm * well.rhofm

            lambda4 = well.lambdac
            lambda45 = lambdacsr
            lambda5 = lambdasr
            lambda56 = lambdasrfm
            c4 = well.cc  # Specific Heat Capacity of the casing
            c5 = csr  # Specific Heat Capacity of the surrounding space
            rho4 = well.rhoc  # Density of the casing
            rho5 = rhosr  # Density of the surrounding space

        if x == sections - 1:
            lambda4 = well.lambdafm
            lambda45 = well.lambdafm
            lambda5 = well.lambdafm
            lambda56 = well.lambdafm
            c4 = well.cfm  # Specific Heat Capacity of the casing (formation)
            c5 = well.cfm  # Specific Heat Capacity of the surrounding space (formation)
            rho4 = well.rhofm  # Density of the casing (formation)
            rho5 = well.rhofm  # Density of the surrounding space (formation)

        # first casing wall
        c4z = (lambda4 / (well.deltaz ** 2)) / 2
        c4e = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
        c4w = (2 * well.r3 * well.h3 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
        c4t = rho4 * c4 / deltat
        total.append([c4z, c4e, c4w, c4t])

        # surrounding space
        c5z = (lambda5 / (well.deltaz ** 2)) / 2
        c5w = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.r5 / well.r4))) / 2
        c5e = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.rfm / well.r5))) / 2
        c5t = rho5 * c5 / deltat
        total.append([c5z, c5e, c5w, c5t])

        coefficients.append(total)

    coefficients = [np.asarray(coefficients), cb, cbe, cbt, cbz]

    return coefficients

