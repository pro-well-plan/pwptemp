from statistics import mean


def temp_time(n):

    # Simulation main parameters
    time = n  # circulating time, h
    tcirc = time * 3600  # circulating time, s
    tstep = 1
    deltat = tcirc / tstep

    return tcirc,tstep,deltat


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

    Tbot = []
    Tout = []

    for n in range(finaltime):
        Tbot.append(Ta[[n][-1]])
        Tout.append(Ta[[n][0]])

    return finaltime, Tbot, Tout


