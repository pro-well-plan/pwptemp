from math import pi


def tdict():
    dict = {"tin": 20, "ts": 15, "wd": 0, "csg3": 0, "csg2": 0, "csg1": 0, "ddi": 0.101, "ddo": 0.114, "dcsg1i": 0.216,
            "dcsg1o": 0.24, "dsr": 0.26, "dsro": 0.6, "dri": 0.45, "dro": 0.5334, "dfm": 2, "dcsg3i": 0.63,
            "dcsg3o": 0.66, "dcsg2i": 0.41, "dcsg2o": 0.44, "tcsr3": 0, "tcem4": 0, "q": 47.696, "lambdal": 0.635,
            "lambdac": 43.3, "lambdacem": 0.7, "lambdad": 40, "lambdafm": 2.249, "lambdar": 15.49, "lambdaw": 0.6,
            "cl": 3713, "cc": 469, "ccem": 2000, "cd": 400, "cr": 464, "cw": 4000, "cfm": 800, "h1": 1800,
            "h2": 2000, "h3": 200, "h3r": 200, "rhol": 1198, "rhod": 7600, "rhoc": 7800, "rhor": 7800, "rhofm": 2245,
            "rhow": 1029, "rhocem": 2700, "gt": 0.0238, "wtg": -0.005, "rpm": 100, "t": 2, "tbit": 1.35, "wob": 22.41,
            "rop": 14.4, "an": 2}

    return dict


def info(about='all'):
    print("Use the ID of a parameter to change the default value (e.g. tdict['tin']=30 to change the fluid inlet "
          "temperature from the default value to 30° Celsius)" + '\n')

    casings_parameters = 'PARAMETERS RELATED TO CASINGS/RISER' + '\n' + \
                         'csg1: shoe depth of the first casing from the well to the formation, m' + '\n' + \
                         'csg2: shoe depth of the second casing from the well to the formation, m' + '\n' + \
                         'csg3: shoe depth of the third casing from the well to the formation, m' + '\n' + \
                         'ddi: drill string inner diameter, m' + '\n' + \
                         'ddo: drill string outer diameter, m' + '\n' + \
                         'dcsg1i: inner diameter of the first casing from the well to the formation, m' + '\n' + \
                         'dcsg1o: outer diameter of the first casing from the well to the formation, m' + '\n' + \
                         'dcsg2i: inner diameter of the second casing from the well to the formation, m' + '\n' + \
                         'dcsg2o: outer diameter of the second casing from the well to the formation, m' + '\n' + \
                         'dcsg3i: inner diameter of the third casing from the well to the formation, m' + '\n' + \
                         'dcsg3o: outer diameter of the third casing from the well to the formation, m' + '\n' + \
                         'dri: riser inner diameter, m' + '\n' + \
                         'dro: riser outer diameter, m' + '\n'

    conditions_parameters = 'PARAMETERS RELATED TO SIMULATION CONDITIONS' + '\n' + \
                            'ts: surface temperature, °C' + '\n' + \
                            'wd: water depth, m' + '\n' + \
                            'dsr: surrounding space inner diameter, m' + '\n' + \
                            'dsro: surrounding space outer diameter, m' + '\n' + \
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
                           'h1: drill pipe inner - convective heat transfer coefficient, W/(m^2*°C)' + '\n' + \
                           'h2: drill pipe outer - convective heat transfer coefficient, W/(m^2*°C)' + '\n' + \
                           'h3: casing inner - convective heat transfer coefficient, W/(m^2*°C)' + '\n' + \
                           'h3r: riser inner - convective heat transfer coefficient, W/(m^2*°C)' + '\n' + \
                           'gt: geothermal gradient, °C/m' + '\n' + \
                           'wtg: seawater thermal gradient, °C/m' + '\n'

    densities_parameters = 'PARAMETERS RELATED TO DENSITIES' + '\n' + \
                           'rhol: fluid density, kg/m3' + '\n' + \
                           'rhod: drill pipe density, kg/m3' + '\n' + \
                           'rhoc: casing density, kg/m3' + '\n' + \
                           'rhor: riser density, kg/m3' + '\n' + \
                           'rhofm: formation density, kg/m3' + '\n' + \
                           'rhow: seawater density, kg/m3' + '\n' + \
                           'rhocem: cement density, kg/m3' + '\n'

    operational_parameters = 'PARAMETERS RELATED TO THE OPERATION' + '\n' + \
                             'tin: fluid inlet temperature, °C' + '\n' + \
                             'q: flow rate, m3/h' + '\n' + \
                             'rpm: revolutions per minute' + '\n' + \
                             't: torque on the drill string, kN*m' + '\n' + \
                             'tbit: torque on the bit, kN*m' + '\n' + \
                             'wob: reight on bit, kN' + '\n' + \
                             'rop: rate of penetration, m/h' + '\n' + \
                             'an: area of the nozzles, m2' + '\n'

    if about == 'casings':
        print(casings_parameters)

    if about == 'conditions':
        print(conditions_parameters)

    if about == 'heatcoeff':
        print(heatcoeff_parameters)

    if about == 'densities':
        print(densities_parameters)

    if about == 'operational':
        print(operational_parameters)

    if about == 'all':
        print(casings_parameters + '\n' + conditions_parameters + '\n' + heatcoeff_parameters + '\n' +
              densities_parameters + '\n' + operational_parameters)


def set_well(temp_dict, depths):
    class NewWell(object):
        def __init__(self):
            self.md = depths.md
            self.tvd = depths.tvd
            self.deltaz = depths.deltaz
            self.zstep = depths.zstep
            self.tin = temp_dict["tin"]  # Inlet Fluid temperature, °C
            self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
            self.wd = temp_dict["wd"]  # Water Depth, m
            self.riser = round(self.wd / self.deltaz)  # number of grid cells for the riser
            self.csg3 = round(temp_dict["csg3"] / self.deltaz)  # Shoe Depth of Conductor Casing, m
            self.csg2 = round(temp_dict["csg2"] / self.deltaz)  # Shoe Depth of Surface Casing, m
            self.csg1 = round(temp_dict["csg1"] / self.deltaz)  # Shoe Depth of Intermediate Casing, m
            # Wellbore Geometry
            self.ddi = temp_dict["ddi"]  # Drill String Inner  Diameter, m
            self.ddo = temp_dict["ddo"]  # Drill String Outer Diameter, m
            self.dcsg1i = temp_dict["dcsg1i"]  # Casing Inner Diameter, m
            self.dcsg1o = temp_dict["dcsg1o"]  # Casing Outer Diameter, m
            self.dsr = temp_dict["dsr"]  # Surrounding Space Inner Diameter, m
            self.dsro = temp_dict["dsro"]  # Surrounding Space Outer Diameter, m
            self.dri = temp_dict["dri"]  # Riser diameter Inner Diameter, m
            self.dro = temp_dict["dro"]  # Riser diameter Outer Diameter, m
            self.dfm = temp_dict["dfm"]  # Undisturbed Formation Diameter, m
            self.dcsg3i = temp_dict["dcsg3i"]   # Conductor casing inner diameter, m
            self.dcsg3o = temp_dict["dcsg3o"]   # Conductor casing outer diameter, m
            self.dcemo = self.dcsg3o+0.03  # First Cement sheath outer diameter, m
            self.dcsg2i = temp_dict["dcsg2i"]   # Surface casing inner diameter, m
            self.dcsg2o = temp_dict["dcsg2o"]   # Surface casing outer diameter, m
            self.r1 = self.ddi / 2  # Drill String Inner  Radius, m
            self.r2 = self.ddo / 2  # Drill String Outer Radius, m
            self.r3 = self.dcsg1i / 2  # Casing Inner Radius, m
            self.r3r = self.dri / 2  # Riser Inner Radius, m
            self.r4r = self.dro / 2  # Riser Outer Radius, m
            self.r4 = self.dcsg1o / 2  # Surrounding Space Inner Radius m
            self.r5 = self.dcemo / 2  # Surrounding Space Outer Radius, m
            self.rfm = self.dfm / 2  # Undisturbed Formation Radius, m
            self.tcsr = (self.dcsg3o-self.dcsg3i)/2 + (self.dcsg2o-self.dcsg2i)/2
            self.tcem = (self.dcsg2i-self.dcsg1o)/2 + (self.dcsg3i-self.dcsg2o)/2 + (self.dcemo-self.dcsg3o)/2
            self.tcsr2 = (self.dcsg2o-self.dcsg2i)/2
            self.tcem2 = (self.dcsg2i-self.dcsg1o)/2 + (self.dcsg2i-self.dcsg2o)/2
            self.tcsr3 = temp_dict["tcsr3"]
            self.tcem3 = (self.dcsg2i - self.dcsg1o) / 2
            self.tcem4 = temp_dict["tcem4"]
        # Flow Rate
            self.q = temp_dict["q"]     # Flow rate, m^3/h
            self.va = (self.q / (pi * ((self.r3 ** 2) - (self.r2 ** 2)))) / 3600        # Fluid velocity through the annular
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600       # Fluid velocity through the drill pipe
        # Heat Coefficients
        # Thermal Conductivity, W/(m*°C)
            self.lambdal = temp_dict["lambdal"]     # Fluid
            self.lambdac = temp_dict["lambdac"]    # Casing
            self.lambdacem = temp_dict["lambdacem"]     #Cement
            self.lambdad = temp_dict["lambdad"]     # Drill Pipe
            self.lambdasr = (self.lambdac*(self.tcsr) + self.lambdacem*(self.tcem))/(self.r5-self.r4)       # Surrounding space
            self.lambdasr2 = (self.lambdac*(self.tcsr2) + self.lambdacem*(self.tcem2))/(self.r5 - self.r4)     # Surrounding space
            self.lambdasr3 = (self.lambdac*(self.tcsr3) + self.lambdacem*(self.tcem3))/(self.r5 - self.r4)  # Surrounding space
            self.lambdacsr = (self.lambdac * (self.r4 - self.r3) + self.lambdasr * (self.r5 - self.r4)) / (
                        self.r5 - self.r3)  # Comprehensive Casing - Surrounding space
            self.lambdacsr2 = (self.lambdac * (self.r4 - self.r3) + self.lambdasr2 * (self.r5 - self.r4)) / (
                        self.r5 - self.r3)  # Comprehensive Casing - Surrounding space
            self.lambdacsr3 = (self.lambdac * (self.r4 - self.r3) + self.lambdasr3 * (self.r5 - self.r4)) / (
                        self.r5 - self.r3)  # Comprehensive Casing - Surrounding space
            self.lambdafm = temp_dict["lambdafm"]       # Formation
            self.lambdasrfm = (self.lambdac * (self.r5 - self.r4) + self.lambdasr * (self.rfm - self.r5)) / (
                        self.rfm - self.r4)  # Comprehensive Surrounding space - Formation
            self.lambdasrfm2 = (self.lambdac * (self.r5 - self.r4) + self.lambdasr2 * (self.rfm - self.r5)) / (
                        self.rfm - self.r4)  # Comprehensive Surrounding space - Formation
            self.lambdasrfm3 = (self.lambdac * (self.r5 - self.r4) + self.lambdasr3 * (self.rfm - self.r5)) / (
                        self.rfm - self.r4)  # Comprehensive Surrounding space - Formation
            self.lambdar = temp_dict["lambdar"]     # Riser
            self.lambdaw = temp_dict["lambdaw"]     # Seawater
            self.lambdarw = (self.lambdar * (self.r4r - self.r3r) + self.lambdaw * (self.r5 - self.r4r)) / (
                        self.r5 - self.r3r)       # Comprehensive Riser - Seawater
        # Specific Heat Capacity, J/(kg*°C)
            self.cl = temp_dict["cl"]       # Fluid
            self.cc = temp_dict["cc"]    # Casing
            self.ccem = temp_dict["ccem"]     # Cement
            self.cd = temp_dict["cd"]     # Drill Pipe
            self.cr = temp_dict["cr"]     # Riser
            self.cw = temp_dict["cw"]      # Seawater
            self.csr = (self.cc*(self.tcsr) + self.ccem*(self.tcem))/(self.r5-self.r4)       # Surrounding space
            self.csr2 = (self.cc * (self.tcsr2) + self.ccem * (self.tcem2)) / (self.r5 - self.r4)  # Surrounding space
            self.csr3 = (self.cc * (self.tcsr3) + self.ccem * (self.tcem3)) / (self.r5 - self.r4)  # Surrounding space
            self.cfm = temp_dict["cfm"]       # Formation
        # Convective Heat Transfer Coefficient, W/(m^2*°C)
            self.h1 = temp_dict["h1"]       # Drill Pipe inner wall
            self.h2 = temp_dict["h2"]       # Drill Pipe outer wall
            self.h3 = temp_dict["h3"]       # Casing inner wall
            self.h3r = temp_dict["h3r"]    # Riser inner wall
        # Densities, kg/m3
            self.rhol = temp_dict["rhol"]       # Fluid
            self.rhod = temp_dict["rhod"]       # Drill Pipe
            self.rhoc = temp_dict["rhoc"]       # Casing
            self.rhocem = temp_dict["rhocem"]
            self.rhor = temp_dict["rhor"]       # Riser
            self.rhofm = temp_dict["rhofm"]     # Formation
            self.rhow = temp_dict["rhow"]       # Seawater
            xcsr = self.tcsr / (self.r5 - self.r4)
            xcem = self.tcem / (self.r5 - self.r4)
            xfm = 1 - xcsr - xcem
            self.rhosr = xcsr*self.rhoc + xcem*self.rhocem + xfm*self.rhofm  # Surrounding Space
            xcsr = self.tcsr2 / (self.r5 - self.r4)
            xcem = self.tcem2 / (self.r5 - self.r4)
            xfm = 1 - xcsr - xcem
            self.rhosr2 = xcsr*self.rhoc + xcem*self.rhocem + xfm*self.rhofm  # Surrounding Space
            xcsr = self.tcsr3 / (self.r5 - self.r4)
            xcem = self.tcem3 / (self.r5 - self.r4)
            xfm = 1 - xcsr - xcem
            self.rhosr3 = xcsr*self.rhoc + xcem*self.rhocem + xfm*self.rhofm  # Surrounding Space
        # Thermal Gradients
            self.gt = temp_dict["gt"] * self.deltaz  # Geothermal gradient, °C/m
            self.wtg = temp_dict["wtg"] * self.deltaz  # Seawater thermal gradient, °C/m
        # Operational Parameters
            self.rpm = temp_dict["rpm"]    # Revolutions per minute
            self.t = temp_dict["t"]     # Torque on the drill string, kN*m
            self.tbit = temp_dict["tbit"]       # Torque on the bit, kN*m
            self.wob = temp_dict["wob"]     # Weight on bit, kN
            self.rop = temp_dict["rop"]     # Rate of Penetration, m/h
            self.an = temp_dict["an"]       # Area of the nozzles, m^2
            self.mdt = depths.md[-1]     # Measured Depth of the Target, m
        # Heat Source Terms
            self.qp = 2*pi * (self.rpm/60) * self.t + 2 * 0.24 * self.rhol * (self.vp ** 2) * (self.mdt / (self.ddi*127.094*10**6)) * (1/0.24**.5)
            self.qa = 0.05*(self.wob*(self.rop/3600)+2*pi*(self.rpm/60)*self.tbit) + (self.rhol/2*9.81)*((self.q/3600)/(0.095*self.an)) \
                    + (2*0.3832*self.mdt/((self.r3-self.r2)*(127.094*10**6)))*((2*(0.7+1)*self.va)/(0.7*pi*(self.r3+self.r2)
                    * (self.r3-self.r2)**2))**0.7

    return NewWell()
