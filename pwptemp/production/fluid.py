def initial_density(well, initcond, section='tubing'):
    """
    Function to calculate the density profile for the first time step
    :param section: 'tubing' or 'annular'
    :param well: a well object created from the function set_well()
    :param initcond: a initial conditions object with the formation temperature profile
    :return: the density profile and the initial density at surface conditions
    """

    if section == 'tubing':
        beta = well.beta
        alpha = well.alpha
        rho = well.rhof

    if section == 'annular':
        beta = well.beta_a
        alpha = well.alpha_a
        rho = well.rhof_a

    rhof_initial = rho
    pressure = [rho * 9.81 * i for i in well.tvd]
    rhof = [rhof_initial * (1 + (x - 10 ** 5) / beta - alpha * (y - well.ts)) for x, y in
            zip(pressure, initcond.tfto)]
    pressure = [x * 9.81 * y for x, y in zip(rhof, well.tvd)]

    rhof = [rhof_initial * (1 + (x - 10 ** 5) / beta - alpha * (y - well.ts)) for x, y in
            zip(pressure, initcond.tfto)]

    return rhof, rhof_initial


def calc_density(well, initcond, rhof_initial, section='tubing'):
    """
    Function to calculate the density profile
    :param section: 'tubing' or 'annular'
    :param well: a well object created from the function set_well()
    :param initcond: a initial conditions object with the formation temperature profile
    :param rhof_initial: initial density at surface conditions
    :param flow: boolean to define if the section is flowing
    :return: density profile
    """

    if section == 'tubing':
        beta = well.beta
        alpha = well.alpha
        flow = True
        temp = initcond.tfto
        rho = well.rhof
    if section == 'annular':
        beta = well.beta_a
        alpha = well.alpha_a
        flow = False
        temp = initcond.tao
        rho = well.rhof_a

    pressure_h = [x * 9.81 * y for x, y in zip(rho, well.tvd)]

    if flow:
        pressure_f = [x * (well.md[-1] / well.dti) * (1/2) * y * well.vp **2 for x, y in zip(well.f_p, rho)]
    else:
        pressure_f = [0] * len(well.md)

    pressure = [x + y for x, y in zip(pressure_h, pressure_f)]

    rhof = [rhof_initial * (1 + (x - 10 ** 5) / beta - alpha * (y - well.ts)) for x, y in
            zip(pressure, temp)]

    return rhof


def calc_vicosity(api, initcond):
    """
    Function to calculate the viscosity profile (Glaso, 1980)
    :param api: API gravity of the produced hydrocarbon
    :param initcond: a initial conditions object with the formation temperature profile
    :return: viscosity profile
    """

    from math import log10

    visc_t, visc_a = [], []
    for x, y in zip(initcond.tfto, initcond.tao):
        x = (x * 1.8) + 32      # converting °C to °F
        y = (y * 1.8) + 32      # converting °C to °F
        c = 3.141 * (10 ** 10) * (x ** (-3.444))
        d = (10.313 * log10(x)) - 36.447
        visc_t.append((c * log10(api) ** d)/1000)
        c = 3.141 * (10 ** 10) * (y ** (-3.444))
        d = (10.313 * log10(y)) - 36.447
        visc_a.append((c * log10(api) ** d)/1000)

    return visc_t, visc_a