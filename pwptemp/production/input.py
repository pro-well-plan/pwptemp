def data(casings=[], d_openhole=0.216):
    from numpy import asarray
    dict = {'ts': 15.0, 'wd': 100.0,  'dti': 4.0, 'dto': 4.5, 'dri': 17.716, 'dro': 21.0, 'dfm': 80.0,
            'q': 300, 'lambdaf': 0.635, 'lambdac': 43.3, 'lambdacem': 0.7, 'lambdat': 40.0, 'lambdafm': 2.249,
            'lambdar': 15.49, 'lambdaw': 0.6, 'cf': 3713.0, 'cc': 469.0, 'ccem': 2000.0, 'ct': 400.0, 'cr': 464.0,
            'cw': 4000.0, 'cfm': 800.0, 'rhof': 1.198, 'rhof_a': 1.2, 'rhot': 7.6, 'rhoc': 7.8, 'rhor': 7.8,
            'rhofm': 2.245, 'rhow': 1.029, 'rhocem': 2.7, 'gt': 0.0238, 'wtg': -0.005, 'visc': 3,
            'beta': 44983 * 10 ** 5, 'alpha': 960 * 10 ** -6, 'beta_a': 44983 * 10 ** 5, 'alpha_a': 960 * 10 ** -6}

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


def set_well(temp_dict, depths):
    from math import pi, log

    class NewWell(object):
        def __init__(self):
            # DEPTH
            self.md = depths.md
            self.tvd = depths.tvd
            self.deltaz = depths.deltaz
            self.zstep = depths.zstep

            # TUBULAR
            self.casings = temp_dict["casings"]  # casings array
            self.riser = round(temp_dict["wd"] / self.deltaz)  # number of grid cells for the riser
            self.dti = temp_dict["dti"] * 0.0254  # Tubing Inner  Diameter, m
            self.dto = temp_dict["dto"] * 0.0254   # Tubing Outer Diameter, m
            self.dri = temp_dict["dri"] * 0.0254  # Riser diameter Inner Diameter, m
            self.dro = temp_dict["dro"] * 0.0254   # Riser diameter Outer Diameter, m

            # CONDITIONS
            self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
            self.wd = temp_dict["wd"]  # Water Depth, m
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
            self.rhof = temp_dict["rhof"] * 1000  # Fluid
            self.rhof_a = temp_dict["rhof_a"] * 1000  # Fluid
            self.rhot = temp_dict["rhot"] * 1000  # Tubing
            self.rhoc = temp_dict["rhoc"] * 1000  # Casing
            self.rhor = temp_dict["rhor"] * 1000  # Riser
            self.rhocem = temp_dict["rhocem"] * 1000  # Cement Sheath
            self.rhofm = temp_dict["rhofm"] * 1000  # Formation
            self.rhow = temp_dict["rhow"] * 1000  # Seawater
            self.visc = temp_dict["visc"] / 1000  # Fluid viscosity [Pas]

            # OPERATIONAL
            self.q = temp_dict["q"] * 0.06  # Flow rate, m^3/h
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600  # Fluid velocity through the tubing

            # HEAT COEFFICIENTS
            # Thermal conductivity
            self.lambdaf = temp_dict["lambdaf"]  # Fluid
            self.lambdac = temp_dict["lambdac"]  # Casing
            self.lambdacem = temp_dict["lambdacem"]  # Cement
            self.lambdat = temp_dict["lambdat"]  # Tubing wall
            self.lambdafm = temp_dict["lambdafm"]       # Formation
            self.lambdar = temp_dict["lambdar"]     # Riser
            self.lambdaw = temp_dict["lambdaw"]     # Seawater

            self.beta = temp_dict["beta"]       # Fluid Thermal Expansion Coefficient
            self.alpha = temp_dict['alpha']
            self.beta_a = temp_dict["beta_a"]  # Fluid Thermal Expansion Coefficient
            self.alpha_a = temp_dict['alpha_a']
            # Heat capacity
            self.cf = temp_dict["cf"]       # Fluid
            self.cc = temp_dict["cc"]    # Casing
            self.ccem = temp_dict["ccem"]     # Cement
            self.ct = temp_dict["ct"]     # Tubing
            self.cr = temp_dict["cr"]     # Riser
            self.cw = temp_dict["cw"]      # Seawater
            self.cfm = temp_dict["cfm"]       # Formation

            self.pr = self.visc * self.cf / self.lambdaf       # Prandtl number

            self.gt = temp_dict["gt"] * self.deltaz  # Geothermal gradient, °C/m
            self.wtg = temp_dict["wtg"] * self.deltaz  # Seawater thermal gradient, °C/m

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

        def define_density(self, ic, cond=0):
            from .fluid import initial_density, calc_density
            if cond == 0:
                self.rhof, self.rhof_initial = initial_density(self, ic)
                self.rhof_a, self.rhof_a_initial = initial_density(self, ic, section='annular')
            else:
                self.rhof = calc_density(self, ic, self.rhof_initial)
                self.rhof_a = calc_density(self, ic, self.rhof_initial, section='annular')
            self.re_p = [x * self.vp * 2 * self.r1 / self.visc for x in self.rhof]  # Reynolds number inside tubing
            self.f_p = [1.63 / log(6.9 / x) ** 2 for x in self.re_p]  # Friction factor inside tubing
            self.nu_dpi = [0.027 * (x ** (4 / 5)) * (self.pr ** (1 / 3)) * (1 ** 0.14) for x in self.re_p]
            # convective heat transfer coefficients, W/(m^2*°C)
            self.h1 = [self.lambdaf * x / self.dti for x in self.nu_dpi]  # Tubing inner wall
            return self

    return NewWell()
