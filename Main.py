import matplotlib.pyplot as plt
import json
import cProfile
from Input import WellTemperature
from WellPath import wellpath
pr = cProfile.Profile()
pr.enable()

with open('temp_dict.json') as f:
    tempdict = json.load(f)

mywell=WellTemperature(tempdict)

md,tvd,deltaz,zstep,csgc,csgs,csgi=wellpath(mywell.mdt)

# Initial Conditions
from InitCond import init_cond
Tdsio, Tdso, Tao, Tcsgo, Tsro, Tfm=init_cond(mywell.ts,mywell.riser,mywell.wtg,mywell.gt,zstep,tvd,deltaz)

Ta=[]

def temp_time(n):
    # Simulation main parameters
    Time = n # circulating time, h
    tcirc = Time * 3600  # circulating time, s
    tstep = 1
    deltat = tcirc / tstep

    from HeatCoefficients import heat_coef
    c1z,c1e,c1,c1t,c2z,c2e,c2w,c2t,c3z,c3e,c3w,c3,c3t,c4z,c4e,c4w,c4t,c5z,c5w,c5e,c5t,c4z1,c4e1, \
    c4w1,c4t1,c5z1,c5w1,c5e1,c5t1,c4z2,c4e2,c4w2,c4t2,c5z2,c5w2,c5e2,c5t2,c4z3,c4e3,c4w3,c4t3,c5z3, \
    c5w3,c5e3,c5t3,c4z4,c4e4,c4w4,c4t4,c5z4,c5w4,c5e4,c5t4,c4z5,c4e5,c4w5,c4t5,c5z5,c5w5,c5e5,c5t5= \
    heat_coef(mywell.rhol,mywell.cl,mywell.vp,mywell.h1,mywell.r1,mywell.qp,mywell.lambdal,mywell.r2,
    mywell.h2,mywell.rhod,mywell.cd,mywell.va,mywell.r3,mywell.h3,mywell.qa,mywell.lambdar,mywell.lambdarw,
    mywell.lambdaw,mywell.cr,mywell.cw,mywell.rhor,mywell.rhow,mywell.r4,mywell.r5,mywell.rfm,mywell.lambdac,
    mywell.lambdacsr,mywell.lambdasr,mywell.lambdasrfm,mywell.cc,mywell.csr,mywell.rhoc,mywell.rhosr,
    mywell.lambdafm,mywell.cfm,mywell.rhofm,deltaz,deltat)

    from LinearSystem import temp_calc
    Tdsiv,Tav,Trv,Tcsgv,Tsrv=temp_calc(mywell.tin,Tdsio,Tdso, Tao, Tcsgo, Tsro,c1z,c1e,c1,c1t,c2z,c2e,c2w,c2t,c3z,c3e,c3w,c3,
    c3t,c4z,c4e,c4w,c4t,c5z,c5w,c5e,c5t,c4z1,c4e1,c4w1,c4t1,c5z1,c5w1,c5e1,c5t1,c4z2,c4e2,c4w2,c4t2,c5z2,c5w2,c5e2,
    c5t2,c4z3,c4e3,c4w3,c4t3,c5z3,c5w3,c5e3,c5t3,c4z4,c4e4,c4w4,c4t4,c5z4,c5w4,c5e4,c5t4,c4z5,c4e5,c4w5,c4t5,c5z5,
    c5w5,c5e5,c5t5,zstep,mywell.riser,mywell.xi,csgc,csgs,csgi)

    return Tdsiv,Tav,Trv,Tcsgv,Tsrv

for n in range(1,3):
    Ta.append(temp_time(n)[1])

from statistics import mean

valor = mean(Ta[0]) - mean(Ta[1])
finaltime=2
while abs(valor) >= 0.01:
    Ta.append(temp_time(finaltime+1)[1])
    valor = mean(Ta[finaltime]) - mean(Ta[finaltime-1])
    finaltime=finaltime+1
Tdsi=temp_time(finaltime)[0]
Tr=temp_time(finaltime)[2]
Tcsg=temp_time(finaltime)[3]
Tsr=temp_time(finaltime)[4]

Tbot=[]
Tout=[]
for n in range(finaltime):
    Tbot.append(Ta[n][-1])
    Tout.append(Ta[n][0])

pr.disable()
pr.print_stats(sort="tottime")

from Graph import temp_plot
temp_plot(finaltime,Tbot,Tout,Tfm,Tdsi,md,Ta,Tr,Tcsg,Tsr,mywell.riser)

print("It's stable at %i hours" % finaltime)

print(mywell.tcsr,mywell.tcem)


