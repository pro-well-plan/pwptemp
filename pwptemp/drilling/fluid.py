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
    pressure_f = [x * (well.md[-1] / well.ddi) * (1/2) * y * well.vp **2 for x, y in zip(well.f_p, well.rhof)]
    pressure = [x + y for x, y in zip(pressure_h, pressure_f)]
    rhof = [rhof_initial * (1 + (x - 10 ** 5) / well.beta - well.alpha * (y - well.ts)) for x, y in
            zip(pressure, initcond.tdsio)]

    return rhof


def calc_vicosity(well, visc_eq, initcond, a=-3.2 * 10 ** -3, b=5.8 * 10 ** -5):
    """
    Function to calculate the viscosity profile (Huang et al., 2020)
    :param well: a well object created from the function set_well()
    :param visc_eq: boolean to use the same viscosity in the pipe and annular
    :param initcond: a initial conditions object with the formation temperature profile
    :param a: constant (specific for the fluid)
    :param b: constant (specific for the fluid)
    :return: viscosity profile
    """

    from math import pi, exp

    q = well.q
    n = well.n
    r1 = well.r1
    r2 = well.r2
    r3 = well.r3
    k = well.k
    thao_o = well.thao_o

    thao_w = ((q / (pi * n * (r3 - r2) ** 2 * (1 / (2 * (2 * n + 1) * k ** (1 / n))) *
                         (r3 + r2))) + (thao_o * (2 * n + 1) / (n + 1)) ** (1 / n)) ** n
    shear_rate = ((thao_w - thao_o) / k) ** (1 / n)
    visc_annulus = (thao_o / shear_rate) + k * shear_rate ** (n - 1)  # Fluid viscosity [Pas]

    if visc_eq:
        visc_pipe = visc_annulus
    else:
        from sympy import symbols, solve
        x = symbols('x')
        expr = q - (pi * n * r1**3 * (1 /(3*n + 1)) * (x/k)**(1/n) * (1 - (3*n + 1) * (thao_o) / (n*(2*n + 1) * x)))
        sol = solve(expr)
        thao_w_p = sol[0]
        shear_rate_p = ((thao_w_p - thao_o) / k) ** (1 / n)
        visc_pipe = float((thao_o / shear_rate_p) + k * shear_rate_p ** (n - 1))

    P = 1000 # constant pressure at 1000 psi
    visc_p = [visc_pipe * exp((a * x) + (b * P)) for x in initcond.tdsio]
    visc_a = [visc_annulus * exp((a * x) + (b * P)) for x in initcond.tao]

    return visc_p, visc_a
