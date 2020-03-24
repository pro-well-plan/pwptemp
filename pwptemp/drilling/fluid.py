def initial_density(well, initcond):
    """
    Function to calculate the density profile for the first time step
    :param well: a well object created from the function set_well()
    :param initcond: a initial conditions object with the formation temperature profile
    :return: the density profile and the initial density at surface conditions
    """
    rhof_initial = well.rhof
    pressure = [well.rhof * 9.81 * i for i in well.tvd]
    rhof = [well.rhof * (1 + (x - 10 ** 5) / well.beta - well.alpha * (y - well.ts)) for x, y in
            zip(pressure, initcond.tdsio)]
    pressure = [x * 9.81 * y for x, y in zip(rhof, well.tvd)]
    rhof = [well.rhof * (1 + (x - 10 ** 5) / well.beta - well.alpha * (y - well.ts)) for x, y in
            zip(pressure, initcond.tdsio)]

    return rhof, rhof_initial


def calc_density(well, initcond, rhof_initial):
    """
    Function to calculate the density profile
    :param well: a well object created from the function set_well()
    :param initcond: a initial conditions object with the formation temperature profile
    :param rhof_initial: initial density at surface conditions
    :return: density profile
    """
    pressure_h = [x * 9.81 * y for x, y in zip(well.rhof, well.tvd)]
    pressure_f = [well.f_p * (well.md[-1] / well.ddi) * (1/2) * x * well.vp **2 for x in well.rhof]
    pressure = [x + y for x, y in zip(pressure_h, pressure_f)]
    rhof = [rhof_initial * (1 + (x - 10 ** 5) / well.beta - well.alpha * (y - well.ts)) for x, y in
            zip(pressure, initcond.tdsio)]

    return rhof
