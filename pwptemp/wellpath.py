from numpy import interp, arange
from math import radians, sin, cos


def get(mdt, deltaz, kop=0, eob=0, build_angle=0, profile='vertical', sod=0, eod=0):
    if profile == 'vertical':        # WELLPROFILE for vertical well
        md = list(arange(0, mdt + deltaz, deltaz))  # Measured Depth from RKB, m
        tvd = md   # True Vertical Depth from RKB, m
        zstep = len(md)  # Number of cells from RKB up to the bottom

    if profile == 'J':        # J-type well
        # Vertical section
        md = list(arange(0, mdt + deltaz, deltaz))  # Measured Depth from RKB, m
        tvd = md[:round(kop / deltaz) + 1]  # True Vertical Depth from RKB, m
        s = eob - kop
        theta = radians(build_angle)
        r = s / theta
        z_displacement = (r * sin(theta)) / round((eob - kop) / deltaz)

        # Build section
        for x in range(round(kop / deltaz), round(eob / deltaz)):
            tvd.append(tvd[x] + z_displacement)
        z_displacement = (deltaz * cos(theta))

        # Tangent section
        for x in range(round(eob / deltaz) + 1, len(md)):
            tvd.append(tvd[x-1] + z_displacement)
        zstep = len(md)

    if profile == 'S':  # S-type well
        # Vertical section
        md = list(arange(0, mdt + deltaz, deltaz))  # Measured Depth from RKB, m
        tvd = md[:round(kop / deltaz) + 1]  # True Vertical Depth from RKB, m
        # Build section
        s = eob - kop
        theta = radians(build_angle)
        r = s / theta
        z_displacement = (r * sin(theta)) / round((eob - kop) / deltaz)
        for x in range(round(kop / deltaz), round(eob / deltaz)):
            tvd.append(tvd[x] + z_displacement)
        z_displacement = (deltaz * cos(theta))

        # Tangent section
        for x in range(round(eob / deltaz)+1, round(sod / deltaz)):
            tvd.append(tvd[x-1] + z_displacement)
        zstep = len(md)

        # Drop section
        s = eod - sod
        theta = radians(build_angle)
        r = s / theta
        z_displacement = (r * sin(theta)) / round((eod - sod) / deltaz)
        for x in range(round(sod / deltaz), round(eod / deltaz)):
            tvd.append(tvd[x-1] + z_displacement)

        # Vertical section
        for x in range(round(eod / deltaz), len(md)):
            tvd.append(tvd[x-1] + deltaz)

    class WellDepths(object):
        def __init__(self):
            self.md = md
            self.tvd = tvd
            self.deltaz = deltaz
            self.zstep = zstep

    return WellDepths()


def load(md, tvd, deltaz):

    md_new = list(arange(0, max(md) + deltaz, deltaz))
    tvd_new = [0]
    for i in md_new[1:]:
        tvd_new.append(interp(i, md, tvd))
    zstep = len(md_new)

    class WellDepths(object):
        def __init__(self):
            self.md = md_new
            self.tvd = tvd_new
            self.deltaz = deltaz
            self.zstep = zstep

    return WellDepths()
