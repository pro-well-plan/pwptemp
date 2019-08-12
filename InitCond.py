def init_cond(Ts,riser,wtg,gt,zstep,tvd,deltaz):
    # Initial Conditions
    Tdsio = [Ts]   # Temperature of the fluid inside the drill string at RKB
    Tdso = [Ts]    # Temperature of the drill string wall at RKB, t=0
    Tao = [Ts]      # Temperature of the fluid inside the annulus at RKB, t=0
    Tcsgo = [Ts]    # Temperature of the casing at RKB, t=0   
    Tsro = [Ts]    # Temperature of the surrounding space at RKB, t=0
    Tfm = [Ts]      # Temperature of the formation at RKB

    for j in range(1, zstep):

        if j <= riser:
            Tg = wtg    # Water Thermal Gradient for the Riser section
        else:
            Tg = gt      # Geothermal Gradient below the Riser section

        deltaT = Tsro[j - 1] + Tg*(tvd[j]-tvd[j-1])/deltaz
        # Generating the Temperature Profile at t=0
        Tdsio.append(deltaT)
        Tdso.append(deltaT)
        Tao.append(deltaT)
        Tcsgo.append(deltaT)
        Tsro.append(deltaT)
        Tfm.append(deltaT)
    return Tdsio, Tdso, Tao, Tcsgo, Tsro, Tfm
