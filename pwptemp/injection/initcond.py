def init_cond(well):
    """
    Generates the temperature profiles at time 0, before starting the operation.
    :param well: a well object created from the function set_well()
    :return: object with initial temperature profiles
    """

    # Initial Conditions
    Tfto = [well.ts]   # Temperature of the fluid inside the tubing at RKB
    Tto = [well.ts]    # Temperature of the tubing at RKB, t=0
    Tao = [well.ts]      # Temperature of the fluid inside the annulus at RKB, t=0
    Tco = [well.ts]    # Temperature of the casing at RKB, t=0
    Tsro = [well.ts]    # Temperature of the surrounding space at RKB, t=0
    Tfm = [well.ts]      # Temperature of the formation at RKB

    for j in range(1, well.zstep):

        if j <= well.riser:
            Tg = well.wtg    # Water Thermal Gradient for the Riser section
        else:
            Tg = well.gt      # Geothermal Gradient below the Riser section

        deltaT = Tsro[j - 1] + Tg*(well.tvd[j]-well.tvd[j-1])/well.deltaz

        # Generating the Temperature Profile at t=0
        Tfto.append(deltaT)
        Tto.append(deltaT)
        Tao.append(deltaT)
        Tco.append(deltaT)
        Tsro.append(deltaT)
        Tfm.append(deltaT)

    class InitCond(object):
        def __init__(self):
            self.tfto = Tfto
            self.tto = Tto
            self.tao = Tao
            self.tco = Tco
            self.tsro = Tsro
            self.tfm = Tfm

    return InitCond()
