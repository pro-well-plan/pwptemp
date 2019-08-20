from math import pi

class WellTemperature(object):
    def __init__(self):
        self.tin = 30  # Inlet Fluid temperature, °C
        self.ts = 15  # Surface Temperature (RKB), °C
        self.xi = 5  # number of radial sections (Inside DS, DS wall, Annular, Csg and Surrounding Space)
        self.wd = 100  # Water Depth, m
        deltaz=50  # deltaz is always the same  # Length of each grid cell
        self.riser = round(self.wd / deltaz)  # number of grid cells for the riser
        # Wellbore Geometry
        self.ddi = 0.101  # Drill String Inner  Diameter, m
        self.ddo = 0.114  # Drill String Outer Diameter, m
        self.dcsg = 0.216  # Casing Inner Diameter, m
        self.dcsgo = 0.24  # Casing Outer Diameter, m
        self.dsr = 0.26  # Surrounding Space Inner Diameter, m
        self.dsro = 0.6  # Surrounding Space Outer Diameter, m
        self.dri = 0.45  # Riser diameter Inner Diameter, m
        self.dro = 0.5334  # Riser diameter Outer Diameter, m
        self.dfm = 2  # Undisturbed Formation Diameter, m
        self.dcsgci = 0.63   # Conductor casing inner diameter, m
        self.dcsgco = 0.66   # Conductor casing outer diameter, m
        self.dcemo = self.dcsgco+0.03  # First Cement sheath outer diameter, m
        self.dcsgsi = 0.41   # Surface casing inner diameter, m
        self.dcsgso = 0.44   # Surface casing outer diameter, m
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
        self.tcsr3 = 0
        self.tcem3 = (self.dcsgsi - self.dcsgo) / 2
        self.tcem4 = 0
    # Flow Rate
        self.q = 47.696     # Flow rate, m^3/h
        self.va = (self.q / (pi * ((self.r3 ** 2) - (self.r2 ** 2)))) / 3600        # Fluid velocity through the annular
        self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600       # Fluid velocity through the drill pipe
    # Heat Coefficients
    # Thermal Conductivity, W/(m*°C)
        self.lambdal = 0.635     # Fluid
        self.lambdac = 43.3    # Casing
        self.lambdacem = 0.7     #Cement
        self.lambdad = 40     # Drill Pipe
        self.lambdasr = (self.lambdac*(self.tcsr) + self.lambdacem*(self.tcem))/(self.r5-self.r4)       # Surrounding space
        self.lambdasr2 = (self.lambdac*(self.tcsr2) + self.lambdacem*(self.tcem2))/(self.r5 - self.r4)     # Surrounding space
        self.lambdasr3 = (self.lambdac*(self.tcsr3) + self.lambdacem*(self.tcem3))/(self.r5 - self.r4)  # Surrounding space
        self.lambdacsr = (self.lambdac * (self.r4 - self.r3) + self.lambdasr * (self.r5 - self.r4)) / (
                    self.r5 - self.r3)  # Comprehensive Casing - Surrounding space
        self.lambdacsr2 = (self.lambdac * (self.r4 - self.r3) + self.lambdasr2 * (self.r5 - self.r4)) / (
                    self.r5 - self.r3)  # Comprehensive Casing - Surrounding space
        self.lambdacsr3 = (self.lambdac * (self.r4 - self.r3) + self.lambdasr3 * (self.r5 - self.r4)) / (
                    self.r5 - self.r3)  # Comprehensive Casing - Surrounding space
        self.lambdafm = 2.249       # Formation
        self.lambdasrfm = (self.lambdac * (self.r5 - self.r4) + self.lambdasr * (self.rfm - self.r5)) / (
                    self.rfm - self.r4)  # Comprehensive Surrounding space - Formation
        self.lambdasrfm2 = (self.lambdac * (self.r5 - self.r4) + self.lambdasr2 * (self.rfm - self.r5)) / (
                    self.rfm - self.r4)  # Comprehensive Surrounding space - Formation
        self.lambdasrfm3 = (self.lambdac * (self.r5 - self.r4) + self.lambdasr3 * (self.rfm - self.r5)) / (
                    self.rfm - self.r4)  # Comprehensive Surrounding space - Formation
        self.lambdar = 15.49     # Riser
        self.lambdarw = 5       # Comprehensive Riser - Seawater
        self.lambdaw = 0.6     # Seawater
    # Specific Heat Capacity, J/(kg*°C)
        self.cl = 3713       # Fluid
        self.cc = 469    # Casing
        self.ccem = 2000     # Cement
        self.cd = 400     # Drill Pipe
        self.cr = 464     # Riser
        self.cw = 4000       # Seawater
        self.csr = (self.cc*(self.tcsr) + self.ccem*(self.tcem))/(self.r5-self.r4)       # Surrounding space
        self.csr2 = (self.cc * (self.tcsr2) + self.ccem * (self.tcem2)) / (self.r5 - self.r4)  # Surrounding space
        self.csr3 = (self.cc * (self.tcsr3) + self.ccem * (self.tcem3)) / (self.r5 - self.r4)  # Surrounding space
        self.cfm = 1500       # Formation
    # Convective Heat Transfer Coefficient, W/(m^2*°C)
        self.h1 = 2000       # Drill Pipe inner wall
        self.h2 = 2000       # Drill Pipe outer wall
        self.h3 = 200       # Casing inner wall
        self.h3r = 200    # Riser inner wall
    # Densities, kg/m3
        self.rhol = 1198       # Fluid
        self.rhod = 8000       # Drill Pipe
        self.rhoc = 9000       # Casing
        self.rhor = 9000       # Riser
        self.rhofm = 2645     # Formation
        self.rhow = 1029       # Seawater
        self.rhosr = 4000     # Surrounding Space
    # Thermal Gradients
        self.gt = 0.0238 * deltaz  # Geothermal gradient, °C/m
        self.wtg = -0.005 * deltaz  # Seawater thermal gradient, °C/m
    # Operational Parameters    
        self.rpm = 100    # Revolutions per minute
        self.t = 2     # Torque on the drill string, kN*m
        self.tbit = 1.35       # Torque on the bit, kN*m
        self.wob = 22.41     # Weight on bit, kN
        self.rop = 14.4     # Rate of Penetration, m/h
        self.an = 2       # Area of the nozzles, m^2
        self.mdt = 5000     # Measured Depth of the Target, m
    # Heat Source Terms
        self.qp = 2*pi * (self.rpm/60) * self.t * 2 * 0.24 * self.rhol * (self.vp ** 2) * (self.mdt / (self.ddi*127.094*10**6)) * (1/0.24**.5)
        self.qa = 0.05*(self.wob*(self.rop/3600)+2*pi*(self.rpm/60)*self.tbit) + (self.rhol/2*9.81)*((self.q/3600)/(0.095*self.an)) \
                + (2*0.3832*self.mdt/((self.r3-self.r2)*(127.094*10**6)))*((2*(0.7+1)*self.va)/(0.7*pi*(self.r3+self.r2)
                * (self.r3-self.r2)**2))**0.7

