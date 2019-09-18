def param_effect(Tdsi, Ta, Toh, well):

    import math
    # Eq coefficients - Inside Drill String
    deltaz = 50
    c1z = ((well.rhol * well.cl * well.vp) / deltaz) / 2  # Vertical component for fluid inside drill string
    c1 = well.qp / (math.pi * (well.r1 ** 2))  # Heat source term for fluid inside drill string
    c3e = (2 * well.r3 * well.h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2  # East component for fluid inside annular
    c3 = well.qa / (math.pi * ((well.r3 ** 2) - (well.r2 ** 2)))  # Heat source term for fluid inside annular

    total = (c1z * abs(Tdsi[-1] - Tdsi[-2]) + c1 + c3e * abs(Ta[-1] - Toh[-1]) + c3)

    p1 = c1z * abs(Tdsi[-1] - Tdsi[-2]) / total
    p1 = round(p1*100, 2)  # Effect of the mud circulation
    p2 = (c1 + c3) / total
    p2 = round(p2*100, 2)  # Effect of heat source terms
    p3 = c3e * abs(Ta[-1] - Toh[-1]) / total  # Effect of the formation
    p3 = round(p3 * 100, 2)

    effect = [p1, p2, p3]

    return effect


def hs_effect(well):

    import math
    pi = math.pi
    rps = well.rpm / 60
    p1 = 2*pi*rps*well.t / well.qp
    p1 = round(p1*100, 2)  # Effect of Drill String Rotation in Heat Source Term Qp
    p2 = round((100 - p1), 2)  # Effect of Friction in Heat Source Term Qp
    p3 = 0.05*(well.wob * well.rop + 2 * pi * rps * well.tbit) / well.qa
    p3 = round(p3 * 100, 2)  # Effect of Drill String Rotation in Heat Source Term Qa
    p4 = round((100 - p3), 2)  # Effect of Friction in Heat Source Term Qa

    effect = [p1, p2, p3, p4]

    return effect


def hs_ratio(well):

    result = round(well.qp/well.qa, 2)

    return result
