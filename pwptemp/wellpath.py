from numpy import interp


def get(mdt, deltaz):
    #WELLPROFILE for vertical well
    md = list(range(0, mdt + deltaz, deltaz))  # Measured Depth from RKB, m
    tvd = md   # True Vertical Depth from RKB, m
    zstep = len(md)  # Number of cells from RKB up to the bottom

    class WellDepths(object):
        def __init__(self):
            self.md = md
            self.tvd = tvd
            self.deltaz = deltaz
            self.zstep = zstep

    return WellDepths()


def load(md, tvd, deltaz):

    md_new = list(range(0, max(md) + deltaz, deltaz))
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
