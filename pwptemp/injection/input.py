def data(casings=[], d_openhole=0.216, units='metric'):
    """
    Parameters involved within the operation calculations
    :param casings: list of dictionaries with casings characteristics (od, id and depth)
    :param d_openhole: diameter of open hole section, m
    :param units: system of units ('metric' or 'english')
    :return: a dictionary with default values for the required parameters
    """

    from numpy import asarray

    dict_met = {'ts': 15.0, 'wd': 100.0,  'dti': 4.0, 'dto': 4.5, 'dri': 17.716, 'dro': 21.0, 'dfm': 80.0,
                'q': 144, 'lambdaf': 0.635, 'lambdaf_a': 0.635, 'lambdac': 43.3, 'lambdacem': 0.7, 'lambdat': 40.0,
                'lambdafm': 2.249, 'lambdar': 15.49, 'lambdaw': 0.6, 'cf': 3713.0, 'cf_a': 3713.0, 'cc': 469.0,
                'ccem': 2000.0, 'ct': 400.0, 'cr': 464.0, 'cw': 4000.0, 'cfm': 800.0, 'rhof': 1.198, 'rhof_a': 1.2,
                'rhot': 7.6, 'rhoc': 7.8, 'rhor': 7.8, 'rhofm': 2.245, 'rhow': 1.029, 'rhocem': 2.7, 'gt': 0.0238,
                'wtg': -0.005, 'tin': 20, 'beta': 44983 * 10 ** 5, 'alpha': 960 * 10 ** -6,
                'beta_a': 44983 * 10 ** 5, 'alpha_a': 960 * 10 ** -6}

    dict_eng = {'ts': 59.0, 'wd': 328.0, 'dti': 4.0, 'dto': 4.5, 'dri': 17.716, 'dro': 21.0, 'dfm': 80.0,
                'q': 26.42, 'lambdaf': 1.098, 'lambdaf_a': 1.098, 'lambdac': 74.909, 'lambdacem': 1.21, 'lambdat': 69.2,
                'lambdafm': 3.89, 'lambdar': 26.8, 'lambdaw': 1.038, 'cf': 0.887, 'cf_a': 0.887, 'cc': 0.112,
                'ccem': 0.478, 'ct': 0.096, 'cr': 0.1108, 'cw': 0.955, 'cfm': 0.19, 'rhof': 9.997, 'rhof_a': 10,
                'rhot': 65.09, 'rhoc': 65.09, 'rhor': 65.09, 'rhofm': 18.73, 'rhow': 8.587, 'rhocem': 22.5,
                'gt': 0.00403, 'wtg': -8.47*10**-4, 'tin': 68, 'beta': 652423, 'alpha': 5.33 * 10 ** -4,
                'beta_a': 652423, 'alpha_a': 5.33 * 10 ** -4}

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
    """
    Retrieves information about the parameters (description and units)
    :param about: type of parameters
    :return: description and units of parameters
    """

    print("Use the ID of a parameter to change the default value (e.g. tdict['tin']=30 to change the fluid inlet "
          "temperature from the default value to 30° Celsius)")
    print('Notice that the information is provided as follows:' + '\n' +
          'parameter ID: general description, units' + '\n')

    tubular_parameters = 'VALUES RELATED TO TUBULAR SIZES' + '\n' + \
                         'dti: tubing inner diameter, in' + '\n' + \
                         'dto: tubing outer diameter, in' + '\n' + \
                         'dri: riser inner diameter, in' + '\n' + \
                         'dro: riser outer diameter, in' + '\n'

    conditions_parameters = 'PARAMETERS RELATED TO SIMULATION CONDITIONS' + '\n' + \
                            'ts: surface temperature, °C or °F' + '\n' + \
                            'wd: water depth, m or ft' + '\n' + \
                            'dfm: undisturbed formation diameter, m or ft' + '\n'

    heatcoeff_parameters = 'PARAMETERS RELATED TO HEAT COEFFICIENTS' + '\n' + \
                           'lambdaf: injection fluid - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdaf_a: annular fluid - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdac: casing - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdacem: cement - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdat: tubing - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdafm: formation - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdar: riser - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'lambdaw: water - thermal conductivity, W/(m*°C) or BTU/(h*ft*°F)' + '\n' + \
                           'cf: injection fluid - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'cf_a: annular fluid - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'cc: casing - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'ccem: cement - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'ct: tubing - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'cr: riser - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'cw: water - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'cfm: formation - specific heat capacity, J/(kg*°C) or BTU/(lb*°F)' + '\n' + \
                           'gt: geothermal gradient, °C/m or °F/ft' + '\n' + \
                           'wtg: seawater thermal gradient, °C/m or °F/ft' + '\n'

    densities_parameters = 'PARAMETERS RELATED TO DENSITIES' + '\n' + \
                           'rhof: fluid density, sg or ppg' + '\n' + \
                           'rhot: tubing density, sg or ppg' + '\n' + \
                           'rhoc: casing density, sg or ppg' + '\n' + \
                           'rhor: riser density, sg or ppg' + '\n' + \
                           'rhofm: formation density, sg or ppg' + '\n' + \
                           'rhow: seawater density, sg or ppg' + '\n' + \
                           'rhocem: cement density, sg or ppg' + '\n' + \
                           'beta: isothermal bulk modulus of injection fluid, Pa' + '\n' + \
                           'alpha: expansion coefficient of injection fluid, 1/°C' + '\n' + \
                           'beta_a: isothermal bulk modulus of fluid in annular, Pa or psi' + '\n' + \
                           'alpha_a: expansion coefficient of fluid in annular, 1/°C or 1/°F' + '\n'

    operational_parameters = 'PARAMETERS RELATED TO THE OPERATION' + '\n' + \
                             'tin: fluid inlet temperature, °C or °F' + '\n' + \
                             'q: flow rate, m^3/day or gpm' + '\n'

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

    if about == 'all':
        print(tubular_parameters + '\n' + conditions_parameters + '\n' + heatcoeff_parameters + '\n' +
              densities_parameters + '\n' + operational_parameters)


def set_well(temp_dict, depths, units='metric'):
    """
    Define properly the parameters and respective values within an object well.
    :param temp_dict: dictionary with inputs and default values.
    :param depths: wellpath object
    :param units: system of units ('metric' or 'english')
    :return: a well object with conditions and parameters defined
    """

    from math import pi, log

    class NewWell(object):
        def __init__(self):
            # DEPTH
            self.md = depths.md
            self.tvd = depths.tvd
            self.deltaz = self.md[-1] - self.md[-2]
            self.zstep = depths.cells_no
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
                d_conv = 0.0254  # from in to m
            else:
                d_conv = 0.0254  # from in to m
            self.casings = temp_dict["casings"]  # casings array
            self.dti = temp_dict["dti"] * d_conv  # Tubing Inner  Diameter, m
            self.dto = temp_dict["dto"] * d_conv   # Tubing Outer Diameter, m
            self.dri = temp_dict["dri"] * d_conv  # Riser diameter Inner Diameter, m
            self.dro = temp_dict["dro"] * d_conv   # Riser diameter Outer Diameter, m

            # CONDITIONS
            if units == 'metric':
                depth_conv = 1  # from m to m
                self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
            else:
                depth_conv = 1 / 3.28  # from ft to m
                self.ts = (temp_dict["ts"] - 32) * (5 / 9)  # Surface Temperature (RKB), from °F to °C
            self.wd = temp_dict["wd"] * depth_conv  # Water Depth, m
            self.riser = round(self.wd / self.deltaz)  # number of grid cells for the riser
            self.dsr = self.casings[0, 0]  # Surrounding Space Inner Diameter, m
            self.dsro = sorted([self.dro + 0.03, self.casings[-1, 0] + 0.03])[-1]  # Surrounding Space Outer Diameter, m
            self.dfm = temp_dict["dfm"]  # Undisturbed Formation Diameter, m

            # RADIUS (CALCULATED)
            self.r1 = self.dti / 2  # Tubing Inner  Radius, m
            self.r2 = self.dto / 2  # Tubing Outer Radius, m
            self.r3 = self.casings[0, 1] / 2  # Casing Inner Radius, m
            self.r3r = self.dri / 2  # Riser Inner Radius, m
            self.r4r = self.dro / 2  # Riser Outer Radius, m
            self.r4 = self.casings[0, 0] / 2  # Surrounding Space Inner Radius m
            self.r5 = self.dsro / 2  # Surrounding Space Outer Radius, m
            self.rfm = self.dfm / 2  # Undisturbed Formation Radius, m

            # DENSITIES kg/m3
            if units == 'metric':
                dens_conv = 1000  # from sg to kg/m3
            else:
                dens_conv = 119.83  # from ppg to kg/m3
            self.rhof = temp_dict["rhof"] * dens_conv  # Fluid
            self.rhof_a = temp_dict["rhof_a"] * dens_conv  # Fluid
            self.rhot = temp_dict["rhot"] * dens_conv  # Tubing
            self.rhoc = temp_dict["rhoc"] * dens_conv  # Casing
            self.rhor = temp_dict["rhor"] * dens_conv  # Riser
            self.rhocem = temp_dict["rhocem"] * dens_conv  # Cement Sheath
            self.rhofm = temp_dict["rhofm"] * dens_conv  # Formation
            self.rhow = temp_dict["rhow"] * dens_conv  # Seawater

            # OPERATIONAL
            if units == 'metric':
                self.tin = temp_dict["tin"]  # Inlet Fluid temperature, °C
                q_conv = 0.04167     # from m^3/day to m^3/h
            else:
                self.tin = (temp_dict["tin"] - 32) * (5/9)  # Inlet Fluid temperature, from °F to °C
                q_conv = 0.2271   # from gpm to m^3/h
            self.q = temp_dict["q"] * q_conv  # Flow rate, m^3/h
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600  # Fluid velocity through the tubing

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
                gt_conv = 3.28*1.8     # from °F/ft to °C/m
                beta_conv = 6894.76  # from psi to Pa
                alpha_conv = 1.8  # from 1/°F to 1/°C

            # Thermal conductivity  W/(m*°C)
            self.lambdaf = temp_dict["lambdaf"] * lambda_conv  # Injection Fluid
            self.lambdaf_a = temp_dict["lambdaf_a"] * lambda_conv  # Annular Fluid
            self.lambdac = temp_dict["lambdac"] * lambda_conv  # Casing
            self.lambdacem = temp_dict["lambdacem"] * lambda_conv  # Cement
            self.lambdat = temp_dict["lambdat"] * lambda_conv  # Tubing wall
            self.lambdafm = temp_dict["lambdafm"] * lambda_conv  # Formation
            self.lambdar = temp_dict["lambdar"] * lambda_conv  # Riser
            self.lambdaw = temp_dict["lambdaw"] * lambda_conv  # Seawater

            self.beta = temp_dict["beta"] * beta_conv  # isothermal bulk modulus in tubing, Pa
            self.alpha = temp_dict['alpha'] * alpha_conv  # Fluid Thermal Expansion Coefficient in tubing, 1/°C
            self.beta_a = temp_dict["beta_a"] * beta_conv  # isothermal bulk modulus in annular, Pa
            self.alpha_a = temp_dict['alpha_a'] * alpha_conv  # Fluid Thermal Expansion Coefficient in annular, 1/°C

            # Specific heat capacity, J/(kg*°C)
            self.cf = temp_dict["cf"] * c_conv  # Injection Fluid
            self.cf_a = temp_dict["cf"] * c_conv  # Annular Fluid
            self.cc = temp_dict["cc"] * c_conv  # Casing
            self.ccem = temp_dict["ccem"] * c_conv  # Cement
            self.ct = temp_dict["ct"] * c_conv  # Tubing
            self.cr = temp_dict["cr"] * c_conv  # Riser
            self.cw = temp_dict["cw"] * c_conv  # Seawater
            self.cfm = temp_dict["cfm"] * c_conv  # Formation

            self.gt = temp_dict["gt"] * gt_conv * self.deltaz  # Geothermal gradient, °C/m
            self.wtg = temp_dict["wtg"] * gt_conv * self.deltaz  # Seawater thermal gradient, °C/m

            # Raise Errors:

            if self.casings[-1, 0] > self.dsro:
                raise ValueError('Last casing outer diameter must be smaller than the surrounding space diameter.')

            if self.casings[0, 2] > self.md[-1]:
                raise ValueError('MD must be higher than the first casing depth.')

            if self.casings[0, 1] < self.dto:
                raise ValueError('Tubing outer diameter must be smaller than the first casing inner diameter.')

            if self.wd > 0 and self.dro > self.dsro:
                raise ValueError('Riser diameter must be smaller than the surrounding space diameter.')

            if self.dsro > self.dfm:
                raise ValueError('Surrounding space diameter must be smaller than the undisturbed formation diameter.')

        def wellpath(self):
            """
            :return: wellpath object
            """
            return depths

        def define_density(self, ic, cond=0):
            """
            Calculate the density profile
            :param ic: current temperature distribution
            :param cond: '0' to calculate the initial profile
            :return: density profile and derived calculations
            """

            from .fluid import initial_density, calc_density

            if cond == 0:
                self.rhof, self.rhof_initial = initial_density(self, ic)
                self.rhof_a, self.rhof_a_initial = initial_density(self, ic, section='annular')
            else:
                self.rhof = calc_density(self, ic, self.rhof_initial)
                self.rhof_a = calc_density(self, ic, self.rhof_initial, section='annular')
            # Reynolds number inside tubing
            self.re_p = [x * self.vp * 2 * self.r1 / y for x, y in zip(self.rhof, self.visc_t)]
            self.f_p = []  # Friction factor inside tubing
            self.nu_dpi = []
            for x in range(len(self.md)):
                if self.re_p[x] < 2300:
                    self.f_p.append(64 / self.re_p[x])
                    self.nu_dpi.append(4.36)
                else:
                    self.f_p.append(1.63 / log(6.9 / self.re_p[x]) ** 2)
                    self.nu_dpi.append(
                        (self.f_p[x] / 8) * (self.re_p[x] - 1000) *
                        self.pr_t[x] / (1 + (12.7 * (self.f_p[x] / 8) ** 0.5) *
                        (self.pr_t[x] ** (2 / 3) - 1)))
            # convective heat transfer coefficients, W/(m^2*°C)
            self.h1 = [self.lambdaf * x / self.dti for x in self.nu_dpi]  # Tubing inner wall

            return self

        def define_viscosity(self, ic, a=1.856 * 10 ** -11, b=4209, c=0.04527, d=-3.376 * 10 ** -5):
            """
            Calculate the viscosity profile
            :param ic: current temperature distribution
            :param a: constant
            :param b: constant
            :param c: constant
            :param d: constant
            :return: viscosity profile and derived calculations
            """

            from .fluid import calc_vicosity
            self.visc_t, self.visc_a = calc_vicosity(ic, a, b, c, d)

            self.pr_t = [x * self.cf / self.lambdaf for x in self.visc_t]  # Prandtl number - inside tubing
            self.pr_a = [x * self.cf / self.lambdaf for x in self.visc_a]  # Prandtl number - annulus

            return self

    return NewWell()

