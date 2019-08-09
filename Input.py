from math import pi
from WellPath import wellpath

class WellTemperature(object):
    def __init__(self, temp_dict):
        self.tin = temp_dict["tin"]  # Inlet Fluid temperature, °C
        self.ts = temp_dict["ts"]  # Surface Temperature (RKB), °C
        self.xi = 5  # number of radial sections (Inside DS, DS wall, Annular, Csg and Surrounding Space)
        self.wd = temp_dict["wd"]  # Water Depth, m
        deltaz=wellpath(1)[2]  # deltaz is always the same  # Length of each grid cell
        self.riser = round(self.wd / deltaz)  # number of grid cells for the riser
        # Wellbore Geometry
        self.ddi = temp_dict["ddi"]  # Drill String Inner  Diameter, m
        self.ddo = temp_dict["ddo"]  # Drill String Outer Diameter, m
        self.dcsg = temp_dict["dcsg"]  # Casing Inner Diameter, m
        self.dsr = temp_dict["dsr"]  # Surrounding Space Inner Diameter, m
        self.dsro = temp_dict["dsro"]  # Surrounding Space Outer Diameter, m
        self.dri = temp_dict["dri"]  # Riser diameter Inner Diameter, m
        self.dro = temp_dict["dro"]  # Riser diameter Outer Diameter, m
        self.dfm = temp_dict["dfm"]  # Undisturbed Formation Diameter, m
        self.r1 = self.ddi / 2  # Drill String Inner  Radius, m
        self.r2 = self.ddo / 2  # Drill String Outer Radius, m
        self.r3 = self.dcsg / 2  # Casing Inner Radius, m
        self.r3r = self.dri / 2  # Riser Inner Radius, m
        self.r4r = self.dro / 2  # Riser Outer Radius, m
        self.r4 = self.dsr / 2  # Surrounding Space Inner Radius m
        self.r5 = self.dsro / 2  # Surrounding Space Outer Radius, m
        self.rfm = self.dfm / 2  # Undisturbed Formation Radius, m
    # Flow Rate
        self.q = temp_dict["q"]
        self.va = (self.q / (pi * ((self.r3 ** 2) - (self.r2 ** 2)))) / 3600
        self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600
    # Heat Coefficients
    # Thermal Conductivity
        self.lambdal = temp_dict["lambdal"]
        self.lambdac = temp_dict["lambdac"]
        self.lambdad = temp_dict["lambdad"]
        self.lambdacsr = temp_dict["lambdacsr"]
        self.lambdasr = temp_dict["lambdasr"]
        self.lambdafm = temp_dict["lambdafm"]
        self.lambdasrfm = temp_dict["lambdasrfm"]
        self.lambdar = temp_dict["lambdar"]
        self.lambdarw = temp_dict["lambdarw"]
        self.lambdaw = temp_dict["lambdaw"]
    # Specific Heat Capacity
        self.cl = temp_dict["cl"]
        self.cc = temp_dict["cc"]
        self.cd = temp_dict["cd"]
        self.cr = temp_dict["cr"]
        self.cw = temp_dict["cw"]
        self.csr = temp_dict["csr"]
        self.cfm = temp_dict["cfm"]
    # Convective Heat Transfer Coefficient
        self.h1 = temp_dict["h1"]
        self.h2 = temp_dict["h2"]
        self.h3 = temp_dict["h3"]
        self.h3r = temp_dict["h3r"]
    # Densities
        self.rhol = temp_dict["rhol"]
        self.rhod = temp_dict["rhod"]
        self.rhoc = temp_dict["rhoc"]
        self.rhor = temp_dict["rhor"]
        self.rhofm = temp_dict["rhofm"]
        self.rhow = temp_dict["rhow"]
        self.rhosr = temp_dict["rhosr"]
    # Thermal Gradients
        self.gt = temp_dict["gt"] * deltaz  # Geothermal gradient, °C/m
        self.wtg = temp_dict["wtg"] * deltaz  # Seawater thermal gradient, °C/m
        self.rpm = temp_dict["RPM"]
        self.t = temp_dict["T"]
        self.tbit = temp_dict["Tbit"]
        self.wob = temp_dict["WOB"]
        self.rop = temp_dict["ROP"]
        self.an = temp_dict["An"]
        self.mdt = temp_dict["mdt"]
        # Heat Source Terms
        self.qp = 2*pi * (self.rpm/60) * self.t * 2 * 0.24 * self.rhol * (self.vp ** 2) * (self.mdt / (self.ddi*127.094*10**6)) * (1/0.24**.5)
        self.qa = 0.05*(self.wob*self.rop+2*pi*(self.rpm/60)*self.tbit) + (self.rhol/2*9.81)*((self.q/3600)/(0.095*self.an)) \
                + (2*0.3832*self.mdt/((self.r3-self.r2)*(127.094*10**6)))*((2*(0.7+1)*self.va)/(0.7*pi*(self.r3+self.r2)
                * (self.r3-self.r2)**2))**0.7

