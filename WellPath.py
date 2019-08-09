def wellpath(mdt):
    #WELLPATH
    md=range(mdt)
    tvd=[]

    for z in md:
        tvd.append(z)

    deltaz = 50
    zstep = round(mdt/deltaz)

    tvd=tvd[0::deltaz]
    md=md[0::deltaz]

    csgco=500
    csgc=round(csgco/deltaz)
    csgso=2000
    csgs=round(csgso/deltaz)
    csgio=4000
    csgi=round(csgio/deltaz)

    return md,tvd,deltaz,zstep,csgc,csgs,csgi
