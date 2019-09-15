from numpy import interp

def get(mdt, deltaz):
    #WELLPROFILE for vertical well
    md = list(range(0, mdt + deltaz, deltaz))  # Measured Depth from RKB, m
    tvd = md   # True Vertical Depth from RKB, m
    zstep = len(md)  # Number of cells from RKB up to the bottom

    return md, tvd, deltaz, zstep


def load(md, tvd, deltaz):

    md_new = list(range(0, max(md) + deltaz, deltaz))
    tvd_new = [0]
    for i in md_new[1:]:
        tvd_new.append(interp(i, md, tvd))
    zstep = len(md_new)

    return md_new, tvd_new, deltaz, zstep