
def heat_coef(well, deltat):

    import math

    #HEATCOEFFICIENTS
    # Eq coefficients - Inside Drill String
    c1z = ((well.rhol * well.cl * well.vp) / well.deltaz) / 2    # Vertical component (North-South) for fluid inside drill string
    c1e = (2 * well.h1 / well.r1) / 2   # East component for fluid inside drill string
    c1 = well.qp / (math.pi * (well.r1 ** 2))   # Heat source term for fluid inside drill string
    c1t = well.rhol * well.cl / deltat    # Time component for fluid inside drill string

    # Eq coefficients - Drill String Wall
    c2z = (well.lambdal / (well.deltaz ** 2)) / 2     # Vertical component (North-South) for drill string wall
    c2e = (2 * well.r2 * well.h2 / ((well.r2 ** 2) - (well.r1 ** 2))) / 2   # East component for drill string wall
    c2w = (2 * well.r1 * well.h1 / ((well.r2 ** 2) - (well.r1 ** 2))) / 2   # West component for drill string wall
    c2t = well.rhod * well.cd / deltat    # Time component for drill string wall

    # Eq coefficients - Inside Annular
    c3z = (well.rhol * well.cl * well.va / well.deltaz) / 2     # Vertical component (North-South) for fluid inside annular
    c3e = (2 * well.r3 * well.h3 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2   # East component for fluid inside annular
    c3w = (2 * well.r2 * well.h2 / ((well.r3 ** 2) - (well.r2 ** 2))) / 2   # West component for fluid inside annular
    c3 = well.qa / (math.pi * ((well.r3 ** 2) - (well.r2 ** 2)))   # Heat source term for fluid inside annular
    c3t = well.rhol * well.cl / deltat    # Time component for fluid inside annular

    # Casing
    c4z = []    # Vertical component (North-South) for casing
    c4e = []    # East component for casing
    c4w = []    # West component for casing
    c4t = []    # Time component for casing

    # Surrounding Space
    c5z = []    # Vertical component (North-South) for surrounding space
    c5w = []    # West component for surrounding space
    c5e = []    # East component for surrounding space
    c5t = []    # Time component for surrounding space

    #j < Riser:   (This is the seawater/riser section)
    lambda4 = well.lambdar  #Thermal conductivity of the casing (riser in this section)
    lambda45 = well.lambdarw   #Comprehensive Thermal conductivity of the casing (riser) and surrounding space (seawater)
    lambda5 = well.lambdaw   #Thermal conductivity of the surrounding space (seawater)
    lambda56 = well.lambdaw   #Comprehensive Thermal conductivity of the surrounding space (seawater) and formation (seawater)
    c4 = well.cr   #Specific Heat Capacity of the casing (riser)
    c5 = well.cw   #Specific Heat Capacity of the surrounding space (seawater)
    rho4 = well.rhor   #Density of the casing (riser)
    rho5 = well.rhow   #Density of the surrounding space (seawater)
    #Casing: (in this section casing=riser)
    c4z1 = (lambda4 / (well.deltaz ** 2)) / 2
    c4e1 = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4w1 = (2 * well.r3 * well.h3 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4t1 = rho4 * c4 / deltat
    #Surrounding space: (in this section surrounding space is only seawater )
    c5z1 = (lambda5 / (well.deltaz ** 2)) / 2
    c5w1 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.r5 / well.r4))) / 2
    c5e1 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.rfm / well.r5))) / 2
    c5t1 = rho5 * c5 / deltat

    #Riser<=j<csgc:  (This section has intermediate casing + cement + surface casing + cement + conductor casing + cement )
    lambda4 = well.lambdac   #Thermal conductivity of the casing
    lambda45 = well.lambdacsr    #Comprehensive Thermal conductivity of the casing and surrounding space
    lambda5 = well.lambdasr    #Thermal conductivity of the surrounding space (seawater)
    lambda56 = well.lambdasrfm   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = well.cc   #Specific Heat Capacity of the casing
    c5 = well.csr    #Specific Heat Capacity of the surrounding space
    rho4 = well.rhoc   #Density of the casing
    rho5 = well.rhosr    #Density of the surrounding space
    # Casing:
    c4z2 = (lambda4 / (well.deltaz ** 2)) / 2
    c4e2 = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4w2 = (2 * well.r3 * well.h3 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4t2 = rho4 * c4 / deltat
    # Surrounding space:  (cement + surface casing + cement + conductor casing + cement )
    c5z2 = (lambda5 / (well.deltaz ** 2)) / 2
    c5w2 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.r5 / well.r4))) / 2
    c5e2 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.rfm / well.r5))) / 2
    c5t2 = rho5 * c5 / deltat

    #csgc<=j<csgs:  (This section has intermediate casing + cement + surface casing + cement + formation)
    lambda4 = well.lambdac   #Thermal conductivity of the casing
    lambda45 = well.lambdacsr2    #Comprehensive Thermal conductivity of the casing and surrounding space
    lambda5 = well.lambdasr2    #Thermal conductivity of the surrounding space
    lambda56 = well.lambdasrfm2   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = well.cc   #Specific Heat Capacity of the casing
    c5 = well.csr2    #Specific Heat Capacity of the surrounding space
    rho4 = well.rhoc   #Density of the casing
    rho5 = well.rhosr2    #Density of the surrounding space
    # Casing:
    c4z3 = (lambda4 / (well.deltaz ** 2)) / 2
    c4e3 = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4w3 = (2 * well.r3 * well.h3 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4t3 = rho4 * c4 / deltat
    # Surrounding:   (cement + surface casing + cement + formation)
    c5z3 = (lambda5 / (well.deltaz ** 2)) / 2
    c5w3 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.r5 / well.r4))) / 2
    c5e3 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.rfm / well.r5))) / 2
    c5t3 = rho5 * c5 / deltat

    #csgs<=j<csgi:   (This section has intermediate casing + cement + formation)
    lambda4 = well.lambdac   #Thermal conductivity of the casing
    lambda45 = well.lambdacsr3    #Comprehensive Thermal conductivity of the casing and surrounding space
    lambda5 = well.lambdasr3    #Thermal conductivity of the surrounding space
    lambda56 = well.lambdasrfm3   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = well.cc   #Specific Heat Capacity of the casing
    c5 = well.csr3    #Specific Heat Capacity of the surrounding space
    rho4 = well.rhoc   #Density of the casing
    rho5 = well.rhosr3   #Density of the surrounding space
    # Casing:
    c4z4 = (lambda4 / (well.deltaz ** 2)) / 2
    c4e4 = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4w4 = (2 * well.r3 * well.h3 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4t4 = rho4 * c4 / deltat
    # Surrounding space:   (cement + formation)
    c5z4 = (lambda5 / (well.deltaz ** 2)) / 2
    c5w4 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.r5 / well.r4))) / 2
    c5e4 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.rfm / well.r5))) / 2
    c5t4 = rho5 * c5 / deltat

    #j >= csgi:    (This section is open hole)
    lambda4 = well.lambdafm    #Thermal conductivity of the casing (formation in this section)
    lambda45 = well.lambdafm   #Comprehensive Thermal conductivity of the casing (formation) and surrounding space (formation)
    lambda5 = well.lambdafm    #Thermal conductivity of the surrounding space (formation)
    lambda56 = well.lambdafm   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = well.cfm    #Specific Heat Capacity of the casing (formation)
    c5 = well.cfm    #Specific Heat Capacity of the surrounding space (formation)
    rho4 = well.rhofm    #Density of the casing (formation)
    rho5 = well.rhofm    #Density of the surrounding space (formation)
    # Casing:
    c4z5 = (lambda4 / (well.deltaz ** 2)) / 2
    c4e5 = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4w5 = (2 * lambda45 / ((well.r4 ** 2) - (well.r3 ** 2))) / 2
    c4t5 = rho4 * c4 / deltat
    # Surrounding space:     (only formation)
    c5z5 = (lambda5 / (well.deltaz ** 2)) / 2
    c5w5 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.r5 / well.r4))) / 2
    c5e5 = (2 * lambda56 / (well.r5 * (well.r5 - well.r4) * math.log(well.rfm / well.r5))) / 2
    c5t5 = rho5 * c5 / deltat

    class HeatCoeff(object):
        def __init__(self):
            self.c1z = c1z
            self.c1e = c1e
            self.c1 = c1
            self.c1t = c1t
            self.c2z = c2z
            self.c2e = c2e
            self.c2w = c2w
            self.c2t = c2t
            self.c3z = c3z
            self.c3e = c3e
            self.c3w = c3w
            self.c3 = c3
            self.c3t = c3t
            self.c4z = c4z
            self.c4e = c4e
            self.c4w = c4w
            self.c4t = c4t
            self.c5z = c5z
            self.c5w = c5w
            self.c5e = c5e
            self.c5t = c5t
            self.c4z1 = c4z1
            self.c4e1 = c4e1
            self.c4w1 = c4w1
            self.c4t1 = c4t1
            self.c5z1 = c5z1
            self.c5w1 = c5w1
            self.c5e1 = c5e1
            self.c5t1 = c5t1
            self.c4z2 = c4z2
            self.c4e2 = c4e2
            self.c4w2 = c4w2
            self.c4t2 = c4t2
            self.c5z2 = c5z2
            self.c5w2 = c5w2
            self.c5e2 = c5e2
            self.c5t2 = c5t2
            self.c4z3 = c4z3
            self.c4e3 = c4e3
            self.c4w3 = c4w3
            self.c4t3 = c4t3
            self.c5z3 = c5z3
            self.c5w3 = c5w3
            self.c5e3 = c5e3
            self.c5t3 = c5t3
            self.c4z4 = c4z4
            self.c4e4 = c4e4
            self.c4w4 = c4w4
            self.c4t4 = c4t4
            self.c5z4 = c5z4
            self.c5w4 = c5w4
            self.c5e4 = c5e4
            self.c5t4 = c5t4
            self.c4z5 = c4z5
            self.c4e5 = c4e5
            self.c4w5 = c4w5
            self.c4t5 = c4t5
            self.c5z5 = c5z5
            self.c5w5 = c5w5
            self.c5e5 = c5e5
            self.c5t5 = c5t5

    return HeatCoeff()
