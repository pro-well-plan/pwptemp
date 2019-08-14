from statistics import mean
from Main import temp_time

def stab_time():
    Ta = []
    for n in range(1,3):
        Ta.append(temp_time(n)[1])

    valor = mean(Ta[0]) - mean(Ta[1])
    finaltime = 2

    while abs(valor) >= 0.01:
        Ta.append(temp_time(finaltime+1)[1])
        valor = mean(Ta[finaltime]) - mean(Ta[finaltime-1])
        finaltime = finaltime+1
    Tdsi = temp_time(finaltime+1)[0]
    Tr = temp_time(finaltime+1)[2]
    Tcsg = temp_time(finaltime+1)[3]
    Tsr = temp_time(finaltime+1)[4]

    Tbot = []
    Tout = []

    for n in range(finaltime):
        Tbot.append(Ta[n][-1])
        Tout.append(Ta[n][0])

    return finaltime,Tbot,Tout

