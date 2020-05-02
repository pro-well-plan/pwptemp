def data(casings=[], d_openhole=0.216, units='metric'):
    from numpy import asarray
    dict_met = {'tin': 20.0, 'ts': 15.0, 'wd': 100.0,  'ddi': 4.0, 'ddo': 4.5, 'dri': 17.716, 'dro': 21.0, 'dfm': 80.0,
            'q': 794.933, 'lambdal': 0.635, 'lambdac': 43.3, 'lambdacem': 0.7, 'lambdad': 40.0, 'lambdafm': 2.249,
            'lambdar': 15.49, 'lambdaw': 0.6, 'cl': 3713.0, 'cc': 469.0, 'ccem': 2000.0, 'cd': 400.0, 'cr': 464.0,
            'cw': 4000.0, 'cfm': 800.0, 'rhof': 1.198, 'rhod': 7.8, 'rhoc': 7.8, 'rhor': 7.8, 'rhofm': 2.245,
            'rhow': 1.029, 'rhocem': 2.7, 'gt': 0.0238, 'wtg': -0.005, 'rpm': 100.0, 'tbit': 9, 'wob': 50, 'rop': 30.4,
            'an': 3100.0, 'bit_n': 1.0, 'dp_e': 0.0, 'thao_o': 1.82, 'beta': 44983 * 10 ** 5, 'alpha': 960 * 10 ** -6,
            'k': 0.3832, 'n': 0.7, 'visc': 0}

    dict_eng = {'tin': 68.0, 'ts': 59.0, 'wd': 328.0, 'ddi': 4.0, 'ddo': 4.5, 'dri': 17.716, 'dro': 21.0, 'dfm': 80.0,
                'q': 300, 'lambdal': 1.098, 'lambdac': 74.909, 'lambdacem': 1.21, 'lambdad': 69.2, 'lambdafm': 3.89,
                'lambdar': 26.8, 'lambdaw': 1.038, 'cl': 0.887, 'cc': 0.112, 'ccem': 0.478, 'cd': 0.096, 'cr': 0.1108,
                'cw': 0.955, 'cfm': 0.19, 'rhof': 9.997, 'rhod': 65.09, 'rhoc': 65.09, 'rhor': 65.09, 'rhofm': 18.73,
                'rhow': 8.587, 'rhocem': 22.5, 'gt': 0.013, 'wtg': -0.00274, 'rpm': 100.0, 'tbit': 6637, 'wob': 11240,
                'rop': 99.7, 'an': 3100.0, 'bit_n': 1.0, 'dp_e': 0.0, 'thao_o': 1.82, 'beta': 652423,
                'alpha': 5.33 * 10 ** -4, 'k': 0.3832, 'n': 0.7, 'visc': 0}

    if units == 'metric':
        dict = dict_met
    else:
        dict = dict_eng

    if len(casings) > 0:
        od = sorted([x['od'] * 0.0254 for x in casings])
        id = sorted([x['id'] * 0.0254 for x in casings])
        depth = sorted([x['depth'] for x in casings], reverse=True)
        dict['casings'] = [[od[x], id[x], depth[x]] for x in range(len(casings))]
        dict['casings'] = asarray(dict['casings'])
    else:
        dict['casings'] = [[(d_openhole + dict['dro'] * 0.0254), d_openhole, 0]]
        dict['casings'] = asarray(dict['casings'])

    return dict


def info(about='all'):
    print("Use the ID of a parameter to change the default value (e.g. tdict['tin']=30 to change the fluid inlet "
          "temperature from the default value to 30° Celsius)")
    print('Notice that the information is provided as follows:' + '\n' +
          'parameter ID: general description, units' + '\n')

    tubular_parameters = 'VALUES RELATED TO TUBULAR SIZES' + '\n' + \
                         'ddi: drill string inner diameter, in' + '\n' + \
                         'ddo: drill string outer diameter, in' + '\n' + \
                         'dri: riser inner diameter, in' + '\n' + \
                         'dro: riser outer diameter, in' + '\n'

    conditions_parameters = 'PARAMETERS RELATED TO SIMULATION CONDITIONS' + '\n' + \
                            'ts: surface temperature, °C' + '\n' + \
                            'wd: water depth, m' + '\n' + \
                            'dfm: undisturbed formation diameter, m' + '\n'

    heatcoeff_parameters = 'PARAMETERS RELATED TO HEAT COEFFICIENTS' + '\n' + \
                           'lambdal: fluid - thermal conductivity, W/(m*°C)' + '\n' + \
                           'lambdac: casing - thermal conductivity, W/(m*°C)' + '\n' + \
                           'lambdacem: cement - thermal conductivity, W/(m*°C)' + '\n' + \
                           'lambdad: drill pipe - thermal conductivity, W/(m*°C)' + '\n' + \
                           'lambdafm: formation - thermal conductivity, W/(m*°C)' + '\n' + \
                           'lambdar: riser - thermal conductivity, W/(m*°C)' + '\n' + \
                           'lambdaw: water - thermal conductivity, W/(m*°C)' + '\n' + \
                           'cl: fluid - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'cc: casing - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'ccem: cement - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'cd: drill pipe - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'cr: riser - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'cw: water - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'cfm: formation - specific heat capacity, J/(kg*°C)' + '\n' + \
                           'gt: geothermal gradient, °C/m' + '\n' + \
                           'wtg: seawater thermal gradient, °C/m' + '\n'

    densities_parameters = 'PARAMETERS RELATED TO DENSITIES' + '\n' + \
                           'rhof: fluid density, sg' + '\n' + \
                           'rhod: drill pipe density, sg' + '\n' + \
                           'rhoc: casing density, sg' + '\n' + \
                           'rhor: riser density, sg' + '\n' + \
                           'rhofm: formation density, sg' + '\n' + \
                           'rhow: seawater density, sg' + '\n' + \
                           'rhocem: cement density, sg' + '\n' + \
                           'beta: isothermal bulk modulus, Pa' + '\n' + \
                           'alpha: expansion coefficient, 1/°C' + '\n'

    viscosity_parameters = 'PARAMETERS RELATED TO MUD VISCOSITY' + '\n' + \
                           'thao_o: yield stress, Pa' + '\n' + \
                           'n: flow behavior index, dimensionless' + '\n' + \
                           'k: consistency index, Pa*s^n' + '\n' + \
                           'visc: fluid viscosity, cp' + '\n'

    operational_parameters = 'PARAMETERS RELATED TO THE OPERATION' + '\n' + \
                             'tin: fluid inlet temperature, °C' + '\n' + \
                             'q: flow rate, lpm' + '\n' + \
                             'rpm: revolutions per minute' + '\n' + \
                             'tbit: torque on the bit, kN*m' + '\n' + \
                             'wob: weight on bit, kN' + '\n' + \
                             'rop: rate of penetration, m/h' + '\n' + \
                             'an: area of the nozzles, in^2' + '\n' + \
                             'bit_n: drill bit efficiency' + '\n' + \
                             'dp_e: drill pipe eccentricity' + '\n'

    if about == 'casings':
        print(tubular_parameters)

    if about == 'conditions':
        print(conditions_parameters)

    if about == 'heatcoeff':
        print(heatcoeff_parameters)

    if about == 'densities':
        print(densities_parameters)

    if about == 'operational':
        print(operational_parameters)

    if about == 'viscosity':
        print(viscosity_parameters)

    if about == 'all':
        print(tubular_parameters + '\n' + conditions_parameters + '\n' + heatcoeff_parameters + '\n' +
              densities_parameters + '\n' + viscosity_parameters + '\n' + operational_parameters)


def set_well(temp_dict, depths, visc_eq=True, units='metric'):
    from math import pi, log

    class NewWell(object):
        def __init__(self):
            # DEPTH
            self.md = depths.md
            self.tvd = depths.tvd
            self.deltaz = depths.deltaz
            self.zstep = depths.zstep
            self.sections = depths.sections
            self.north = depths.north
            self.east = depths.east
            self.inclination = depths.inclination
            self.dogleg = depths.dogleg
            self.azimuth = depths.azimuth
            if units != 'metric':
                self.md = [i / 3.28 for i in self.md]
                self.tvd = [i / 3.28 for i in self.tvd]
                self.deltaz = self.deltaz / 3.28
                self.north = [i / 3.28 for i in self.north]
                self.east = [i / 3.28 for i in self.east]

            # TUBULAR
            if units == 'metric':
                conv = 0.0254   # from in to m
            else:
                conv = 0.0254   # from in to m
            self.casings = temp_dict["casings"]  # casings array
            self.riser = round(temp_dict["wd"] / self.deltaz)  # number of grid cells for the riser
            self.ddi = temp_dict["ddi"] * conv  # Drill String Inner  Diameter, m
            self.ddo = temp_dict["ddo"] * conv   # Drill String Outer Diameter, m
            self.dri = temp_dict["dri"] * conv  # Riser diameter Inner Diameter, m
            self.dro = temp_dict["dro"] * conv   # Riser diameter Outer Diameter, m

            # CONDITIONS
            if units == 'metric':
                conv = 1     # from m to m
                self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
            else:
                conv = 1/3.28   # from ft to m
                self.ts = (temp_dict["ts"] - 32) * (5/9)  # Surface Temperature (RKB), from °F to °C
            self.wd = temp_dict["wd"] * conv  # Water Depth, m
            self.dsr = self.casings[0, 0]  # Surrounding Space Inner Diameter, m
            self.dsro = sorted([self.dro + 0.03, self.casings[-1, 0] + 0.03])[-1]  # Surrounding Space Outer Diameter, m
            self.dfm = temp_dict["dfm"]  # Undisturbed Formation Diameter, m

            # RADIUS (CALCULATED)
            self.r1 = self.ddi / 2  # Drill String Inner  Radius, m
            self.r2 = self.ddo / 2  # Drill String Outer Radius, m
            self.r3 = self.casings[0, 1] / 2  # Casing Inner Radius, m
            self.r3r = self.dri / 2  # Riser Inner Radius, m
            self.r4r = self.dro / 2  # Riser Outer Radius, m
            self.r4 = self.casings[0, 0] / 2  # Surrounding Space Inner Radius m
            self.r5 = self.dsro / 2  # Surrounding Space Outer Radius, m
            self.rfm = self.dfm / 2  # Undisturbed Formation Radius, m

            # DENSITIES kg/m3
            if units == 'metric':
                conv = 1000     # from sg to kg/m3
            else:
                conv = 119.83   # from ppg to kg/m3
            self.rhof = temp_dict["rhof"] * conv  # Fluid
            self.rhod = temp_dict["rhod"] * conv  # Drill Pipe
            self.rhoc = temp_dict["rhoc"] * conv  # Casing
            self.rhor = temp_dict["rhor"] * conv  # Riser
            self.rhocem = temp_dict["rhocem"] * conv  # Cement Sheath
            self.rhofm = temp_dict["rhofm"] * conv  # Formation
            self.rhow = temp_dict["rhow"] * conv  # Seawater

            # OPERATIONAL
            if units == 'metric':
                self.tin = temp_dict["tin"]  # Inlet Fluid temperature, °C
                q_conv = 0.06     # from lpm to m^3/h
                an_conv = 1 / 1500  # from in^2 to m^2
                wob_conv = 1   # from kN to kN
                tbit_conv = 1  # from kN*m to kN*m
                rop_conv = 1    # from m/h to m/h
            else:
                self.tin = (temp_dict["tin"] - 32) * (5/9)  # Inlet Fluid temperature, from °F to °C
                q_conv = 0.2271   # from gpm to m^3/h
                an_conv = 1 / 1500  # from in^2 to m^2
                wob_conv = 4.4482 / 1000  # from lbf to kN
                tbit_conv = 1.356 / 1000  # from lbf*ft to kN*m
                rop_conv = 1/3.28  # from ft/h to m/h

            self.q = temp_dict["q"] * q_conv  # Flow rate, m^3/h
            self.va = (self.q / (pi * ((self.r3 ** 2) - (self.r2 ** 2)))) / 3600  # Fluid velocity through the annular
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600  # Fluid velocity through the drill pipe
            self.rpm = temp_dict["rpm"]  # Revolutions per minute
            self.tbit = temp_dict["tbit"] * tbit_conv  # Torque on the bit, kN*m
            self.wob = temp_dict["wob"] * wob_conv  # Weight on bit, kN
            self.rop = temp_dict["rop"] * rop_conv  # Rate of Penetration, m/h
            self.an = temp_dict["an"] * an_conv   # Area of the nozzles, m^2
            self.bit_n = temp_dict["bit_n"]  # drill bit efficiency
            self.dp_e = temp_dict["dp_e"]  # drill pipe eccentricity

            self.thao_o = temp_dict["thao_o"]
            self.k = temp_dict["k"]
            self.n = temp_dict["n"]

            if temp_dict["visc"] == 0:
                n = self.n
                thao_w = ((self.q / (pi * n * (self.r3 - self.r2) ** 2 * (1 / (2 * (2 * n + 1) * self.k ** (1 / n))) *
                          (self.r3 + self.r2))) + (self.thao_o * (2 * n + 1) / (n + 1)) ** (1 / n)) ** n
                shear_rate = ((thao_w - self.thao_o) / self.k) ** (1/n)
                self.visc_a = (self.thao_o / shear_rate) + self.k * shear_rate ** (n - 1)  # Fluid viscosity [Pas]

                if visc_eq:
                    self.visc_p = self.visc_a
                else:
                    from sympy import symbols, solve
                    x = symbols('x')
                    expr = self.q - (pi * n * self.r1 ** 3 * (1 / (3 * n + 1)) * (x / self.k) ** (1 / n) * (1 -
                            (3 * n + 1) * (self.thao_o) / (n * (2 * n + 1) * x)))
                    sol = solve(expr)
                    thao_w_p = sol[0]
                    shear_rate_p = ((thao_w_p - self.thao_o) / self.k) ** (1 / n)
                    self.visc_p = float((self.thao_o / shear_rate_p) + self.k * shear_rate_p ** (n - 1))

            else:
                self.visc_p = self.visc_a = temp_dict["visc"] / 1000

            # HEAT COEFFICIENTS
            if units == 'metric':
                lambda_conv = 1     # from W/(m*°C) to W/(m*°C)
                c_conv = 1  # from J/(kg*°C) to J/(kg*°C)
                gt_conv = 1     # from °C/m to °C/m
                beta_conv = 1   # from Pa to Pa
                alpha_conv = 1  # from 1/°F to 1/°C
            else:
                lambda_conv = 1/1.73     # from BTU/(h*ft*°F) to W/(m*°C)
                c_conv = 4187.53  # from BTU/(lb*°F) to J/(kg*°C)
                gt_conv = 3.28/1.8     # from °F/ft to °C/m
                beta_conv = 6894.76  # from psi to Pa
                alpha_conv = 1.8  # from 1/°F to 1/°C
            self.lambdal = temp_dict["lambdal"] * lambda_conv  # Fluid
            self.lambdac = temp_dict["lambdac"] * lambda_conv   # Casing
            self.lambdacem = temp_dict["lambdacem"] * lambda_conv   # Cement
            self.lambdad = temp_dict["lambdad"] * lambda_conv   # Drill Pipe
            self.lambdafm = temp_dict["lambdafm"] * lambda_conv        # Formation
            self.lambdar = temp_dict["lambdar"] * lambda_conv      # Riser
            self.lambdaw = temp_dict["lambdaw"] * lambda_conv      # Seawater
            self.beta = temp_dict["beta"] * beta_conv  # isothermal bulk modulus, Pa
            self.alpha = temp_dict['alpha'] * alpha_conv     # Fluid Thermal Expansion Coefficient, 1/°C
            self.cl = temp_dict["cl"] * c_conv       # Fluid
            self.cc = temp_dict["cc"] * c_conv     # Casing
            self.ccem = temp_dict["ccem"] * c_conv      # Cement
            self.cd = temp_dict["cd"] * c_conv      # Drill Pipe
            self.cr = temp_dict["cr"] * c_conv      # Riser
            self.cw = temp_dict["cw"] * c_conv       # Seawater
            self.cfm = temp_dict["cfm"] * c_conv        # Formation
            self.pr_p = self.visc_p * self.cl / self.lambdal       # Prandtl number
            self.pr_a = self.visc_a * self.cl / self.lambdal  # Prandtl number
            self.gt = temp_dict["gt"] * gt_conv * self.deltaz  # Geothermal gradient, from °C/m to °C/cell
            self.wtg = temp_dict["wtg"] * gt_conv * self.deltaz  # Seawater thermal gradient, from °C/m to °C/cell


            # Raise Errors:
            if self.casings[-1, 0] > self.dsro:
                raise ValueError('Last casing outer diameter must be smaller than the surrounding space diameter.')

            if self.casings[0, 2] > self.md[-1]:
                raise ValueError('MD must be higher than the first casing depth.')

            if self.casings[0, 1] < self.ddo:
                raise ValueError('Drill Pipe outer diameter must be smaller than the first casing inner diameter.')

            if self.wd > 0 and self.dro > self.dsro:
                raise ValueError('Riser diameter must be smaller than the surrounding space diameter.')

            if self.dsro > self.dfm:
                raise ValueError('Surrounding space diameter must be smaller than the undisturbed formation diameter.')

        def plot_torque_drag(self, plot='torque'):
            from .plot import plot_torque_drag
            plot_torque_drag(self, plot)

        def wellpath(self):
            return depths

        def define_density(self, ic, cond=0):
            from .fluid import initial_density, calc_density
            from .torque_drag import calc_torque_drag
            if cond == 0:
                self.rhof, self.rhof_initial = initial_density(self, ic)
            else:
                self.rhof = calc_density(self, ic, self.rhof_initial)
            self.drag, self.torque = calc_torque_drag(self)  # Torque/Forces, kN*m / kN
            self.re_p = [x * self.vp * 2 * self.r1 / self.visc_p for x in self.rhof]  # Reynolds number inside drill pipe
            self.re_a = [x * self.va * 2 * (self.r3 - self.r2) / self.visc_a for x in
                         self.rhof]  # Reynolds number - annular
            self.f_p = [1.63 / log(6.9 / x) ** 2 for x in self.re_p]  # Friction factor inside drill pipe
            self.nu_dpi = [0.027 * (x ** (4 / 5)) * (self.pr_p ** (1 / 3)) * (1 ** 0.14) for x in self.re_p]
            self.nu_dpo = [0.027 * (x ** (4 / 5)) * (self.pr_a ** (1 / 3)) * (1 ** 0.14) for x in self.re_a]
            self.h1 = [self.lambdal * x / self.ddi for x in self.nu_dpi]  # Drill Pipe inner wall
            self.h2 = [self.lambdal * x / self.ddo for x in self.nu_dpo]  # Drill Pipe outer wall
            self.nu_a = [1.86 * ((x * self.pr_a) ** (1 / 3)) * ((2 * (self.r3 - self.r2) / self.md[-1]) ** (1 / 3))
                         * (1 ** (1 / 4)) for x in self.re_a]
            # convective heat transfer coefficients, W/(m^2*°C)
            self.h3 = [self.lambdal * x / (2 * self.r3) for x in self.nu_a]  # Casing inner wall
            self.h3r = [self.lambdal * x / (2 * self.r3r) for x in self.nu_a]  # Riser inner wall
            return self

    return NewWell()
