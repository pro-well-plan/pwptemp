def heat_coef(rhol,cl,vp,h1,r1,qp,lambdal,r2,h2,rhod,cd,va,r3,h3,qa,lambdar,lambdarw,lambdaw,cr,cw,rhor,rhow,r4,r5,rfm,lambdac,lambdacsr,
              lambdasr,lambdasrfm,cc,csr,rhoc,rhosr,lambdafm,cfm,rhofm,deltaz,deltat,lambdasr2,lambdasr3,lambdacsr2,lambdacsr3,lambdasrfm2,
              lambdasrfm3,csr2,csr3):

    import math

    #HEATCOEFFICIENTS
    # Eq coefficients - Inside Drill String
    c1z = ((rhol * cl * vp) / deltaz) / 2    # Vertical component (North-South) for fluid inside drill string
    c1e = (2 * h1 / r1) / 2   # East component for fluid inside drill string
    c1 = qp / (math.pi * (r1 ** 2))   # Heat source term for fluid inside drill string
    c1t = rhol * cl / deltat    # Time component for fluid inside drill string

    # Eq coefficients - Drill String Wall
    c2z = (lambdal / (deltaz ** 2)) / 2     # Vertical component (North-South) for drill string wall
    c2e = (2 * r2 * h2 / ((r2 ** 2) - (r1 ** 2))) / 2   # East component for drill string wall
    c2w = (2 * r1 * h1 / ((r2 ** 2) - (r1 ** 2))) / 2   # West component for drill string wall
    c2t = rhod * cd / deltat    # Time component for drill string wall

    # Eq coefficients - Inside Annular
    c3z = (rhol * cl * va / deltaz) / 2     # Vertical component (North-South) for fluid inside annular
    c3e = (2 * r3 * h3 / ((r3 ** 2) - (r2 ** 2))) / 2   # East component for fluid inside annular
    c3w = (2 * r2 * h2 / ((r3 ** 2) - (r2 ** 2))) / 2   # West component for fluid inside annular
    c3 = qa / (math.pi * ((r3 ** 2) - (r2 ** 2)))   # Heat source term for fluid inside annular
    c3t = rhol * cl / deltat    # Time component for fluid inside annular

    # Casing
    c4z=[]    # Vertical component (North-South) for casing 
    c4e=[]    # East component for casing
    c4w=[]    # West component for casing
    c4t=[]    # Time component for casing

    # Surrounding Space
    c5z=[]    # Vertical component (North-South) for surrounding space
    c5w=[]    # West component for surrounding space
    c5e=[]    # East component for surrounding space
    c5t=[]    # Time component for surrounding space

    #j < Riser:   (This is the seawater/riser section)
    lambda4=lambdar  #Thermal conductivity of the casing (riser in this section) 
    lambda45=lambdarw   #Comprehensive Thermal conductivity of the casing (riser) and surrounding space (seawater)
    lambda5=lambdaw   #Thermal conductivity of the surrounding space (seawater)
    lambda56=lambdaw   #Comprehensive Thermal conductivity of the surrounding space (seawater) and formation (seawater)
    c4=cr   #Specific Heat Capacity of the casing (riser)
    c5=cw   #Specific Heat Capacity of the surrounding space (seawater)
    rho4=rhor   #Density of the casing (riser)
    rho5=rhow   #Density of the surrounding space (seawater)
    #Casing: (in this section casing=riser)
    c4z1=(lambda4 / (deltaz ** 2)) / 2
    c4e1=(2 * lambda45 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4w1=(2 * r3 * h3 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4t1=rho4 * c4 / deltat
    #Surrounding space: (in this section surrounding space is only seawater )
    c5z1=(lambda5 / (deltaz ** 2)) / 2
    c5w1=(2 * lambda56 / (r5 * (r5 - r4) * math.log(r5 / r4))) / 2
    c5e1=(2 * lambda56 / (r5 * (r5 - r4) * math.log(rfm / r5))) / 2
    c5t1=rho5 * c5 / deltat

    #Riser<=j<csgc:  (This section has intermediate casing + cement + surface casing + cement + conductor casing + cement )
    lambda4 = lambdac   #Thermal conductivity of the casing 
    lambda45=lambdacsr    #Comprehensive Thermal conductivity of the casing and surrounding space
    lambda5=lambdasr    #Thermal conductivity of the surrounding space (seawater)
    lambda56=lambdasrfm   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = cc   #Specific Heat Capacity of the casing
    c5 = csr    #Specific Heat Capacity of the surrounding space 
    rho4 = rhoc   #Density of the casing
    rho5 = rhosr    #Density of the surrounding space
    # Casing:
    c4z2=(lambda4 / (deltaz ** 2)) / 2
    c4e2=(2 * lambda45 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4w2=(2 * r3 * h3 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4t2=rho4 * c4 / deltat
    # Surrounding space:  (cement + surface casing + cement + conductor casing + cement )
    c5z2=(lambda5 / (deltaz ** 2)) / 2
    c5w2=(2 * lambda56 / (r5 * (r5 - r4) * math.log(r5 / r4))) / 2
    c5e2=(2 * lambda56 / (r5 * (r5 - r4) * math.log(rfm / r5))) / 2
    c5t2=rho5 * c5 / deltat

    #csgc<=j<csgs:  (This section has intermediate casing + cement + surface casing + cement + formation)
    lambda4 = lambdac   #Thermal conductivity of the casing 
    lambda45 = lambdacsr2    #Comprehensive Thermal conductivity of the casing and surrounding space
    lambda5 = lambdasr2    #Thermal conductivity of the surrounding space
    lambda56 = lambdasrfm2   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = cc   #Specific Heat Capacity of the casing
    c5 = csr2    #Specific Heat Capacity of the surrounding space
    rho4 = rhoc   #Density of the casing
    rho5 = rhosr-600    #Density of the surrounding space
    # Casing:
    c4z3=(lambda4 / (deltaz ** 2)) / 2
    c4e3=(2 * lambda45 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4w3=(2 * r3 * h3 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4t3=rho4 * c4 / deltat
    # Surrounding:   (cement + surface casing + cement + formation)
    c5z3=(lambda5 / (deltaz ** 2)) / 2
    c5w3=(2 * lambda56 / (r5 * (r5 - r4) * math.log(r5 / r4))) / 2
    c5e3=(2 * lambda56 / (r5 * (r5 - r4) * math.log(rfm / r5))) / 2
    c5t3=rho5 * c5 / deltat

    #csgs<=j<csgi:   (This section has intermediate casing + cement + formation)
    lambda4 = lambdac   #Thermal conductivity of the casing 
    lambda45 = lambdacsr3    #Comprehensive Thermal conductivity of the casing and surrounding space
    lambda5 = lambdasr3    #Thermal conductivity of the surrounding space
    lambda56 = lambdasrfm3   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = cc   #Specific Heat Capacity of the casing
    c5 = csr3    #Specific Heat Capacity of the surrounding space
    rho4 = rhoc   #Density of the casing
    rho5 = rhosr-1200   #Density of the surrounding space
    # Casing:
    c4z4=(lambda4 / (deltaz ** 2)) / 2
    c4e4=(2 * lambda45 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4w4=(2 * r3 * h3 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4t4=rho4 * c4 / deltat
    # Surrounding space:   (cement + formation)
    c5z4=(lambda5 / (deltaz ** 2)) / 2
    c5w4=(2 * lambda56 / (r5 * (r5 - r4) * math.log(r5 / r4))) / 2
    c5e4=(2 * lambda56 / (r5 * (r5 - r4) * math.log(rfm / r5))) / 2
    c5t4=rho5 * c5 / deltat

    #j >= csgi:    (This section is open hole)
    lambda4 = lambdafm    #Thermal conductivity of the casing (formation in this section) 
    lambda45 = lambdafm   #Comprehensive Thermal conductivity of the casing (formation) and surrounding space (formation)
    lambda5 = lambdafm    #Thermal conductivity of the surrounding space (formation)
    lambda56 = lambdafm   #Comprehensive Thermal conductivity of the surrounding space and formation
    c4 = cfm    #Specific Heat Capacity of the casing (formation)
    c5 = cfm    #Specific Heat Capacity of the surrounding space (formation)
    rho4 = rhofm    #Density of the casing (formation)
    rho5 = rhofm    #Density of the surrounding space (formation)
    # Casing:
    c4z5=(lambda4 / (deltaz ** 2)) / 2
    c4e5=(2 * lambda45 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4w5=(2 * lambda45 / ((r4 ** 2) - (r3 ** 2))) / 2
    c4t5=rho4 * c4 / deltat
    # Surrounding space:     (only formation)
    c5z5=(lambda5 / (deltaz ** 2)) / 2
    c5w5=(2 * lambda56 / (r5 * (r5 - r4) * math.log(r5 / r4))) / 2
    c5e5=(2 * lambda56 / (r5 * (r5 - r4) * math.log(rfm / r5))) / 2
    c5t5=rho5 * c5 / deltat

    return c1z,c1e,c1,c1t,c2z,c2e,c2w,c2t,c3z,c3e,c3w,c3,c3t,c4z,c4e,c4w,c4t,c5z,c5w,c5e,c5t,c4z1,c4e1, \
            c4w1,c4t1,c5z1,c5w1,c5e1,c5t1,c4z2,c4e2,c4w2,c4t2,c5z2,c5w2,c5e2,c5t2,c4z3,c4e3,c4w3,c4t3,c5z3, \
            c5w3,c5e3,c5t3,c4z4,c4e4,c4w4,c4t4,c5z4,c5w4,c5e4,c5t4,c4z5,c4e5,c4w5,c4t5,c5z5,c5w5,c5e5,c5t5
