def init_cond(well):
    """
    Generates the temperature profiles at time 0, before starting the operation.
    :param well: a well object created from the function set_well()
    :return: object with initial temperature profiles
    """

    # Initial Conditions
    Tdsio = [well.ts]   # Temperature of the fluid inside the drill string at RKB
    Tdso = [well.ts]    # Temperature of the drill string wall at RKB, t=0
    Tao = [well.ts]      # Temperature of the fluid inside the annulus at RKB, t=0
    Tcsgo = [well.ts]    # Temperature of the casing at RKB, t=0
    Tsro = [well.ts]    # Temperature of the surrounding space at RKB, t=0
    Tfm = [well.ts]      # Temperature of the formation at RKB

    for j in range(1, well.zstep):

        if j <= well.riser:
            Tg = well.wtg    # Water Thermal Gradient for the Riser section
        else:
            Tg = well.gt      # Geothermal Gradient below the Riser section

        deltaT = Tsro[j - 1] + Tg*(well.tvd[j]-well.tvd[j-1])/well.deltaz

        # Generating the Temperature Profile at t=0
        Tdsio.append(deltaT)
        Tdso.append(deltaT)
        Tao.append(deltaT)
        Tcsgo.append(deltaT)
        Tsro.append(deltaT)
        Tfm.append(deltaT)

    class InitCond(object):
        def __init__(self):
            self.tdsio = Tdsio
            self.tdso = Tdso
            self.tao = Tao
            self.tcsgo = Tcsgo
            self.tsro = Tsro
            self.tfm = Tfm

    return InitCond()
