def heat_coef(well, deltat, tt, t3):
    """
    Calculate heat transfer coefficients for each cell.
    :param t3: current temperature profile at section 3 (first casing)
    :param tt: current temperature profile at tubing wall
    :param well: a well object created from the function set_well()
    :param deltat: duration of each time step (seconds)
    :return: list with distribution of heat transfer coefficients
    """

    from math import pi, log
    from numpy import interp
    
    sections = [well.wd]
    if len(well.casings) > 0 and well.casings[0, 2] > 0:
        for i in range(len(well.casings))[::-1]:
            sections.append(well.casings[i, 2])

    vb = well.q / (pi * well.r3 ** 2)
    cbz = ((well.rhof[-1] * well.cf * vb) / well.deltaz) / 2  # Vertical component (North-South)
    cbe = (2 * well.h1[-1] / well.r3) / 2  # East component
    cbt = well.rhof[-1] * well.cf / deltat  # Time component

    # Creating empty lists

    # Section 1: Fluid in Tubing
    c1z = []
    c1e = []
    c1 = []
    c1t = []

    # Section 2: Tubing Wall
    c2z = []
    c2e = []
    c2w = []
    c2t = []

    # Section 3: Fluid in Annulus
    c3z = []
    c3e = []
    c3w = []
    c3t = []

    # Section 4: First casing
    c4z = []
    c4e = []
    c4w = []
    c4t = []

    # Section 5: Surrounding Space
    c5z = []
    c5e = []
    c5w = []
    c5t = []

    in_section = 1
    section_checkpoint = sections[0]

    for x in range(well.zstep):
        if x*well.deltaz >= section_checkpoint and in_section < len(sections)+1:
            in_section += 1
            if section_checkpoint != sections[-1]:
                section_checkpoint = sections[in_section-1]

        gr_t = 9.81 * well.alpha * abs((tt[x] - t3[x])) * (well.rhof_a[x] ** 2) * (well.dti ** 3) / (well.visc_a[x]**2)
        gr_c = 9.81 * well.alpha * abs((tt[x] - t3[x])) * (well.rhof_a[x] ** 2) * (((well.r3 - well.r2) * 2) ** 3) / (
                    well.visc_a[x] ** 2)
        ra_t = gr_t * well.pr_a[x]
        ra_c = gr_c * well.pr_a[x]
        inc = [0, 30, 45, 60, 90]
        c_base = [0.069, 0.065, 0.059, 0.057, 0.049]
        c = interp(well.inclination[x], inc, c_base, right=0.049)
        nu_a_t = c * (ra_t ** (1/3)) * (well.pr_a[x] ** 0.074)
        nu_a_c = c * (ra_c ** (1/3)) * (well.pr_a[x] ** 0.074)
        h2 = well.lambdaf_a * nu_a_t / (well.r2 * log(well.r3/well.r2))
        h3 = well.lambdaf_a * nu_a_c / (well.r2 * log(well.r3/well.r2))
        h3r = h3
        lambdal_eq = well.lambdaf_a * nu_a_t

        # fluid inside tubing
        qp = 0.2 * well.q * 2 * (well.f_p[x] * well.rhof[x] * (well.vp ** 2) *
                                 (well.md[-1] / (well.dti * 127.094 * 10 ** 6)))

        c1z.append(((well.rhof[x] * well.cf * well.vp) / well.deltaz) / 2)  # Vertical component (North-South)
        c1e.append((2 * well.h1[x] / well.r1) / 2)  # East component
        c1.append(qp / (pi * (well.r1 ** 2)))  # Heat source term
        c1t.append(well.rhof[x] * well.cf / deltat)  # Time component

        # tubing wall
        c2z.append((well.lambdat / (well.deltaz ** 2)) / 2)  # Vertical component (North-South)
        c2e.append((2 * well.r2 * h2 / ((well.r2 ** 2) - (well.r1 ** 2))) / 2)  # East component
        c2w.append((2 * well.r1 * well.h1[x] / ((well.r2 ** 2) - (well.r1 ** 2))) / 2)  # West component
        c2t.append(well.rhot * well.ct / deltat)  # Time component

        if in_section == 1:
            lambda4 = well.lambdar  # Thermal conductivity of the casing (riser in this section)
            lambda5 = well.lambdaw  # Thermal conductivity of the surrounding space (seawater)
            lambda45 = (lambda4 * (well.r4r - well.r3r) + lambda5 * (well.r5 - well.r4r)) / (
                    well.r5 - well.r3r)  # Comprehensive Thermal conductivity of the casing (riser) and
                                         # surrounding space (seawater)
            lambda56 = well.lambdaw  # Comprehensive Thermal conductivity of the surrounding space (seawater) and
                                     # formation (seawater)
            c4 = well.cr  # Specific Heat Capacity of the casing (riser)
            c5 = well.cw  # Specific Heat Capacity of the surrounding space (seawater)
            rho4 = well.rhor  # Density of the casing (riser)
            rho5 = well.rhow  # Density of the surrounding space (seawater)

            # fluid inside annular
            c3z.append((lambdal_eq / (well.deltaz ** 2)) / 2)  # Vertical component (North-South)
            c3e.append((2 * well.r3 * h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2)  # East component
            c3w.append((2 * well.r2 * h2 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2)  # West component
            c3t.append(well.rhof_a[x] * well.cf_a / deltat)  # Time component

        else:
            # fluid inside annular
            c3z.append((lambdal_eq / (well.deltaz ** 2)) / 2)  # Vertical component (North-South)
            c3e.append((2 * well.r3 * h3r / ((well.r3r ** 2) - (well.r2 ** 2))) / 2)  # East component
            c3w.append((2 * well.r2 * h2 / ((well.r3r ** 2) - (well.r2 ** 2))) / 2)  # West component
            c3t.append(well.rhof_a[x] * well.cf_a / deltat)  # Time component

        if 1 < in_section < len(sections):

            # calculation for surrounding space
            # thickness
            tcsr = 0
            tcem = 0
            for i in range(len(well.casings) - in_section):
                tcsr += (well.casings[i + 1, 0] - well.casings[i + 1, 1]) / 2
                tcem += (well.casings[i + 1, 1] - well.casings[i, 0]) / 2

                tcem += (well.casings[len(well.casings) - in_section + 1, 1] -
                         well.casings[len(well.casings) - in_section, 0]) / 2
            if in_section == 2:
                tcem += (well.dsro - well.casings[-1, 0])
            xcsr = tcsr / (well.r5 - well.r4)  # fraction of surrounding space that is casing
            xcem = tcem / (well.r5 - well.r4)  # fraction of surrounding space that is cement
            xfm = 1 - xcsr - xcem  # fraction of surrounding space that is formation

            # thermal conductivity
            lambdasr = well.lambdac * xcsr + well.lambdacem * xcem + well.lambdafm * xfm
            lambdacsr = (well.lambdac * (well.r4 - well.r3) + lambdasr * (well.r5 - well.r4)) / (well.r5 - well.r3)
            lambdasrfm = (well.lambdac * (well.r5 - well.r4) + lambdasr *   (well.rfm - well.r5)) / (well.rfm - well.r4)

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

        if in_section == len(sections)+1:
            lambda4 = well.lambdafm
            lambda45 = well.lambdafm
            lambda5 = well.lambdafm
            lambda56 = well.lambdafm
            c4 = well.cfm  # Specific Heat Capacity of the casing (formation)
            c5 = well.cfm  # Specific Heat Capacity of the surrounding space (formation)
            rho4 = well.rhofm  # Density of the casing (formation)
            rho5 = well.rhofm  # Density of the surrounding space (formation)

        # first casing wall
        c4z.append((lambda4 / (well.deltaz ** 2)) / 2)
        c4e.append((2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2)
        c4w.append((2 * well.r3 * h3 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2)
        c4t.append(rho4 * c4 / deltat)

        # surrounding space
        c5z.append((lambda5 / (well.deltaz ** 2)) / 2)
        c5w.append((lambda56 / (well.r5 * (well.r5 - well.r4) * log(well.r5 / well.r4))) / 2)
        c5e.append((lambda56 / (well.r5 * (well.r5 - well.r4) * log(well.rfm / well.r5))) / 2)
        c5t.append(rho5 * c5 / deltat)

    hc_1 = [c1z, c1e, c1, c1t]
    hc_2 = [c2z, c2e, c2w, c2t]
    hc_3 = [c3z, c3e, c3w, c3t]
    hc_4 = [c4z, c4e, c4w, c4t]
    hc_5 = [c5z, c5e, c5w, c5t]
    coefficients = [hc_1, hc_2, hc_3, hc_4, hc_5, cbe, cbt, cbz]

    return coefficients

