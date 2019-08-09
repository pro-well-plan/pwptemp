def init_cond(Ts,riser,wtg,gt,zstep,tvd,deltaz):
    # Initial Conditions
    Tdsio = [Ts]
    Tdso = [Ts]
    Tao = [Ts]
    Tcsgo = [Ts]
    Tsro = [Ts]
    Tfm = [Ts]

    for j in range(1, zstep):

        if j <= riser:
            Tg = wtg
        else:
            Tg = gt

        deltaT = Tsro[j - 1] + Tg*(tvd[j]-tvd[j-1])/deltaz

        Tdsio.append(deltaT)
        Tdso.append(deltaT)
        Tao.append(deltaT)
        Tcsgo.append(deltaT)
        Tsro.append(deltaT)
        if j < zstep:
            Tfm.append(deltaT)
    return Tdsio, Tdso, Tao, Tcsgo, Tsro, Tfm