from math import pi

temp_dict = {
  "tin": 20,
  "ts": 15,
  "wd": 0,
  "csgco": 0,
  "csgso": 0,
  "csgio": 0,
  "ddi": 0.101,
  "ddo": 0.114,
  "dcsg": 0.216,
  "dcsgo":  0.24,
  "dsr": 0.26,
  "dsro": 0.6,
  "dri": 0.45,
  "dro": 0.5334,
  "dfm": 2,
  "dcsgci": 0.63,
  "dcsgco": 0.66,
  "dcsgsi": 0.41,
  "dcsgso": 0.44,
  "tcsr3": 0,
  "tcem4": 0,
  "q": 47.696,
  "lambdal": 0.635,
  "lambdac": 43.3,
  "lambdacem": 0.7,
  "lambdad": 40,
  "lambdafm": 2.249,
  "lambdar": 15.49,
  "lambdarw": 5,
  "lambdaw": 0.6,
  "cl": 3713,
  "cc": 469,
  "ccem": 2000,
  "cd": 400,
  "cr": 464,
  "cw": 4000,
  "cfm": 800,
  "h1": 2000,
  "h2": 2000,
  "h3": 200,
  "h3r": 200,
  "rhol": 1198,
  "rhod": 7600,
  "rhoc": 7800,
  "rhor": 7800,
  "rhofm": 2245,
  "rhow": 1029,
  "rhocem": 2700,
  "gt": 0.0238,
  "wtg": -0.005,
  "rpm": 100,
  "t": 2,
  "tbit": 1.35,
  "wob": 22.41,
  "rop": 14.4,
  "an": 2,
  "mdt": 3000
}

class WellTemperature(object):
    def __init__(self, temp_dict):
        self.tin = temp_dict["tin"]  # Inlet Fluid temperature, °C
        self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
        self.wd = temp_dict["wd"]  # Water Depth, m
        deltaz = 50  # deltaz is always the same  # Length of each grid cell
        self.riser = round(self.wd / deltaz)  # number of grid cells for the riser
        self.csgc = round(temp_dict["csgco"] / deltaz)  # Shoe Depth of Conductor Casing, m
        self.csgs = round(temp_dict["csgso"] / deltaz)  # Shoe Depth of Surface Casing, m
        self.csgi = round(temp_dict["csgio"] / deltaz)  # Shoe Depth of Intermediate Casing, m
        # Wellbore Geometry
        self.ddi = temp_dict["ddi"]  # Drill String Inner  Diameter, m
        self.ddo = temp_dict["ddo"]  # Drill String Outer Diameter, m
        self.dcsg = temp_dict["dcsg"]  # Casing Inner Diameter, m
        self.dcsgo = temp_dict["dcsgo"]  # Casing Outer Diameter, m
        self.dsr = temp_dict["dsr"]  # Surrounding Space Inner Diameter, m
        self.dsro = temp_dict["dsro"]  # Surrounding Space Outer Diameter, m
        self.dri = temp_dict["dri"]  # Riser diameter Inner Diameter, m
        self.dro = temp_dict["dro"]  # Riser diameter Outer Diameter, m
        self.dfm = temp_dict["dfm"]  # Undisturbed Formation Diameter, m
        self.dcsgci = temp_dict["dcsgci"]   # Conductor casing inner diameter, m
        self.dcsgco = temp_dict["dcsgco"]   # Conductor casing outer diameter, m
        self.dcemo = self.dcsgco+0.03  # First Cement sheath outer diameter, m
        self.dcsgsi = temp_dict["dcsgsi"]   # Surface casing inner diameter, m
        self.dcsgso = temp_dict["dcsgso"]   # Surface casing outer diameter, m
        self.r1 = self.ddi / 2  # Drill String Inner  Radius, m
        self.r2 = self.ddo / 2  # Drill String Outer Radius, m
        self.r3 = self.dcsg / 2  # Casing Inner Radius, m
        self.r3r = self.dri / 2  # Riser Inner Radius, m
        self.r4r = self.dro / 2  # Riser Outer Radius, m
        self.r4 = self.dcsgo / 2  # Surrounding Space Inner Radius m
        self.r5 = self.dcemo / 2  # Surrounding Space Outer Radius, m
        self.rfm = self.dfm / 2  # Undisturbed Formation Radius, m
        self.tcsr = (self.dcsgco-self.dcsgci)/2 + (self.dcsgso-self.dcsgsi)/2
        self.tcem = (self.dcsgsi-self.dcsgo)/2 + (self.dcsgci-self.dcsgso)/2 + (self.dcemo-self.dcsgco)/2
        self.tcsr2 = (self.dcsgso-self.dcsgsi)/2
        self.tcem2 = (self.dcsgsi-self.dcsgo)/2 + (self.dcsgci-self.dcsgso)/2
        self.tcsr3 = temp_dict["tcsr3"]
        self.tcem3 = (self.dcsgsi - self.dcsgo) / 2
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
        self.lambdarw = temp_dict["lambdarw"]       # Comprehensive Riser - Seawater
        self.lambdaw = temp_dict["lambdaw"]     # Seawater
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
        self.gt = temp_dict["gt"] * deltaz  # Geothermal gradient, °C/m
        self.wtg = temp_dict["wtg"] * deltaz  # Seawater thermal gradient, °C/m
    # Operational Parameters    
        self.rpm = temp_dict["rpm"]    # Revolutions per minute
        self.t = temp_dict["t"]     # Torque on the drill string, kN*m
        self.tbit = temp_dict["tbit"]       # Torque on the bit, kN*m
        self.wob = temp_dict["wob"]     # Weight on bit, kN
        self.rop = temp_dict["rop"]     # Rate of Penetration, m/h
        self.an = temp_dict["an"]       # Area of the nozzles, m^2
        self.mdt = temp_dict["mdt"]     # Measured Depth of the Target, m
    # Heat Source Terms
        self.qp = 2*pi * (self.rpm/60) * self.t + 2 * 0.24 * self.rhol * (self.vp ** 2) * (self.mdt / (self.ddi*127.094*10**6)) * (1/0.24**.5)
        self.qa = 0.05*(self.wob*(self.rop/3600)+2*pi*(self.rpm/60)*self.tbit) + (self.rhol/2*9.81)*((self.q/3600)/(0.095*self.an)) \
                + (2*0.3832*self.mdt/((self.r3-self.r2)*(127.094*10**6)))*((2*(0.7+1)*self.va)/(0.7*pi*(self.r3+self.r2)
                * (self.r3-self.r2)**2))**0.7

