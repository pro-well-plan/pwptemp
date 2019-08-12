def wellpath(mdt):
    #WELLPATH
    md=range(mdt)  # Measured Depth from RKB, m
    tvd=[]   # True Vertical Depth from RKB, m

    for z in md:
        tvd.append(z)

    deltaz = 50  # Length of each grid cell, m
    zstep = round(mdt/deltaz)  # Number of cells from RKB up to the bottom

    tvd=tvd[0::deltaz]
    md=md[0::deltaz]

    csgco=500    # Shoe Depth of Conductor Casing, m
    csgc=round(csgco/deltaz)
    csgso=2000   # Shoe Depth of Surface Casing, m
    csgs=round(csgso/deltaz)
    csgio=4000   # Shoe Depth of Intermediate Casing, m
    csgi=round(csgio/deltaz)

    return md,tvd,deltaz,zstep,csgc,csgs,csgi
