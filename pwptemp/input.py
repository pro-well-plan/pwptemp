from math import pi


def tdict():
    dict = {"tin": 20, "ts": 15, "wd": 0, "csg3": 0, "csg2": 0, "csg1": 0, "ddi": 0.101, "ddo": 0.114, "dcsg1i": 0.216,
            "dcsg1o": 0.24,  "dri": 0.45, "dro": 0.5334, "dfm": 2, "dcsg3i": 0.63, "dcsg3o": 0.66, "dcsg2i": 0.41,
            "dcsg2o": 0.44, "tcsr3": 0, "tcem4": 0, "q": 47.696, "lambdal": 0.635, "lambdac": 43.3, "lambdacem": 0.7,
            "lambdad": 40, "lambdafm": 2.249, "lambdar": 15.49, "lambdaw": 0.6, "cl": 3713, "cc": 469, "ccem": 2000,
            "cd": 400, "cr": 464, "cw": 4000, "cfm": 800, "h1": 1800, "h2": 2000, "h3": 200, "h3r": 200, "rhol": 1198,
            "rhod": 7600, "rhoc": 7800, "rhor": 7800, "rhofm": 2245, "rhow": 1029, "rhocem": 2700, "gt": 0.0238,
            "wtg": -0.005, "rpm": 100, "t": 2, "tbit": 1.35, "wob": 22.41, "rop": 14.4, "an": 2}

    return dict


def info(about='all'):
    print("Use the ID of a parameter to change the default value (e.g. tdict['tin']=30 to change the fluid inlet "
          "temperature from the default value to 30° Celsius)")
    print('Notice that the information is provided as follows:' + '\n' +
          'parameter ID: general description, units' + '\n')

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
            #DEPTH
            self.md = depths.md
            self.tvd = depths.tvd
            self.deltaz = depths.deltaz
            self.zstep = depths.zstep

            #TUBULAR
            self.csg1 = round(temp_dict["csg1"] / self.deltaz)  # number of grid cells for the casing 1
            self.csg2 = round(temp_dict["csg2"] / self.deltaz)  # # number of grid cells for the casing 2
            self.csg3 = round(temp_dict["csg3"] / self.deltaz)  # # number of grid cells for the casing 3
            self.riser = round(temp_dict["wd"] / self.deltaz)  # number of grid cells for the riser
            self.ddi = temp_dict["ddi"]  # Drill String Inner  Diameter, m
            self.ddo = temp_dict["ddo"]  # Drill String Outer Diameter, m
            self.dcsg1i = temp_dict["dcsg1i"]  # Casing Inner Diameter, m
            self.dcsg1o = temp_dict["dcsg1o"]  # Casing Outer Diameter, m
            self.dcsg2i = temp_dict["dcsg2i"]   # Surface casing inner diameter, m
            self.dcsg2o = temp_dict["dcsg2o"]   # Surface casing outer diameter, m
            self.dcsg3i = temp_dict["dcsg3i"]   # Conductor casing inner diameter, m
            self.dcsg3o = temp_dict["dcsg3o"]   # Conductor casing outer diameter, m
            self.dri = temp_dict["dri"]  # Riser diameter Inner Diameter, m
            self.dro = temp_dict["dro"]  # Riser diameter Outer Diameter, m

            #CONDITIONS
            self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
            self.wd = temp_dict["wd"]  # Water Depth, m
            self.dsr = temp_dict["dcsg1o"]  # Surrounding Space Inner Diameter, m
            self.dsro = temp_dict["dcsg3o"]+0.03  # Surrounding Space Outer Diameter, m
            self.dfm = temp_dict["dfm"]  # Undisturbed Formation Diameter, m

            #RADIUS (CALCULATED)
            self.r1 = self.ddi / 2  # Drill String Inner  Radius, m
            self.r2 = self.ddo / 2  # Drill String Outer Radius, m
            self.r3 = self.dcsg1i / 2  # Casing Inner Radius, m
            self.r3r = self.dri / 2  # Riser Inner Radius, m
            self.r4r = self.dro / 2  # Riser Outer Radius, m
            self.r4 = self.dcsg1o / 2  # Surrounding Space Inner Radius m
            self.r5 = self.dsro / 2  # Surrounding Space Outer Radius, m
            self.rfm = self.dfm / 2  # Undisturbed Formation Radius, m

            #HEAT COEFFICIENTS
            self.lambdal = temp_dict["lambdal"]  # Fluid
            self.lambdac = temp_dict["lambdac"]  # Casing
            self.lambdacem = temp_dict["lambdacem"]  # Cement
            self.lambdad = temp_dict["lambdad"]  # Drill Pipe
            self.lambdafm = temp_dict["lambdafm"]       # Formation
            self.lambdar = temp_dict["lambdar"]     # Riser
            self.lambdaw = temp_dict["lambdaw"]     # Seawater
            self.cl = temp_dict["cl"]       # Fluid
            self.cc = temp_dict["cc"]    # Casing
            self.ccem = temp_dict["ccem"]     # Cement
            self.cd = temp_dict["cd"]     # Drill Pipe
            self.cr = temp_dict["cr"]     # Riser
            self.cw = temp_dict["cw"]      # Seawater
            self.cfm = temp_dict["cfm"]       # Formation
            self.h1 = temp_dict["h1"]       # Drill Pipe inner wall
            self.h2 = temp_dict["h2"]       # Drill Pipe outer wall
            self.h3 = temp_dict["h3"]       # Casing inner wall
            self.h3r = temp_dict["h3r"]    # Riser inner wall
            self.gt = temp_dict["gt"] * self.deltaz  # Geothermal gradient, °C/m
            self.wtg = temp_dict["wtg"] * self.deltaz  # Seawater thermal gradient, °C/m

            #DENSITIES
            self.rhol = temp_dict["rhol"]  # Fluid
            self.rhod = temp_dict["rhod"]  # Drill Pipe
            self.rhoc = temp_dict["rhoc"]  # Casing
            self.rhor = temp_dict["rhor"]  # Riser
            self.rhocem = temp_dict["rhocem"]
            self.rhofm = temp_dict["rhofm"]     # Formation
            self.rhow = temp_dict["rhow"]       # Seawater

            #OPERATIONAL
            self.tin = temp_dict["tin"]  # Inlet Fluid temperature, °C
            self.q = temp_dict["q"]     # Flow rate, m^3/h
            self.va = (self.q / (pi * ((self.r3 ** 2) - (self.r2 ** 2)))) / 3600   # Fluid velocity through the annular
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600    # Fluid velocity through the drill pipe
            self.rpm = temp_dict["rpm"]    # Revolutions per minute
            self.t = temp_dict["t"]     # Torque on the drill string, kN*m
            self.tbit = temp_dict["tbit"]       # Torque on the bit, kN*m
            self.wob = temp_dict["wob"]     # Weight on bit, kN
            self.rop = temp_dict["rop"]     # Rate of Penetration, m/h
            self.an = temp_dict["an"]       # Area of the nozzles, m^2


            # Raise Errors:
            if self.dcsg1i > self.dcsg1o or self.dcsg2i > self.dcsg2o or self.dcsg3i > self.dcsg3o or \
                    self.dri > self.dro or self.dsr > self.dsro or self.ddi > self.ddo:
                raise ValueError('Inner diameters must be smaller than outer diameters.')

            if self.csg1 < self.csg2 or self.csg2 < self.csg3:
                raise ValueError('Shoe depths of casings are wrong. They should be csg1 > csg2 > csg3.')

            if self.ddo > self.dcsg1i:
                raise ValueError('Drill string diameter must be smaller than the casing 1 diameter.')

            if self.dcsg1o > self.dcsg2i:
                raise ValueError('Casing 1 diameter must be smaller than the casing 2 diameter.')

            if self.dcsg2o > self.dcsg3i:
                raise ValueError('Casing 2 diameter must be smaller than the casing 3 diameter.')

            if self.dcsg3o > self.dsro:
                raise ValueError('Casing 3 diameter must be smaller than the surrounding space diameter.')

            if self.dro > self.dsro:
                raise ValueError('Riser diameter must be smaller than the surrounding space diameter.')

            if self.dsro > self.dfm:
                raise ValueError('Surrounding space diameter must be smaller than the undisturbed formation diameter.')

    return NewWell()
