def temp_calc(Tin,Tdsio, Tdso, Tao, Tcsgo, Tsro,c1z,c1e,c1,c1t,c2z,c2e,c2w,c2t,c3z,c3e,c3w,c3,c3t,c4z,c4e,c4w,c4t,
            c5z,c5w,c5e,c5t,c4z1,c4e1,c4w1,c4t1,c5z1,c5w1,c5e1,c5t1,c4z2,c4e2,c4w2,c4t2,c5z2,c5w2,c5e2,c5t2,c4z3,
            c4e3,c4w3,c4t3,c5z3,c5w3,c5e3,c5t3,c4z4,c4e4,c4w4,c4t4,c5z4,c5w4,c5e4,c5t4,c4z5,c4e5,c4w5,c4t5,c5z5,
            c5w5,c5e5,c5t5,zstep,Riser,xi,csgc,csgs,csgi):

    import numpy as np

    Tdsi = [Tin]
    Tds = []
    Ta = []
    Tcsg = []
    Tsr = []

    # Creating vectors N,W,C,E,S,B
    N = []
    W = []
    C = []
    E = []
    S = []
    B = []

    # Casing:
    c4z = c4z1
    c4e = c4e1
    c4w = c4w1
    c4t = c4t1
    # Surrounding:
    c5z = c5z1
    c5w = c5w1
    c5e = c5e1
    c5t = c5t1

    for j in range(zstep):

        if j==Riser:
            # Casing:
            c4z = c4z2
            c4e = c4e2
            c4w = c4w2
            c4t = c4t2
            # Surrounding:
            c5z = c5z2
            c5w = c5w2
            c5e = c5e2
            c5t = c5t2

        if j==csgc:
            # Casing:
            c4z = c4z3
            c4e = c4e3
            c4w = c4w3
            c4t = c4t3
            # Surrounding:
            c5z = c5z3
            c5w = c5w3
            c5e = c5e3
            c5t = c5t3

        if j==csgs:
            # Casing:
            c4z = c4z4
            c4e = c4e4
            c4w = c4w4
            c4t = c4t4
            # Surrounding:
            c5z = c5z4
            c5w = c5w4
            c5e = c5e4
            c5t = c5t4

        if j==csgi:
            # Casing:
            c4z = c4z5
            c4e = c4e5
            c4w = c4w5
            c4t = c4t5
            # Surrounding:
            c5z = c5z5
            c5w = c5w5
            c5e = c5e5
            c5t = c5t5

        for i in range(xi):
            if i == 0:  # Inside Drill String
                if j == 1:
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(
                        c1t * Tdsio[j] + c1 + c1e * (Tdso[j] - Tdsio[j]) + c1z * (Tdsio[j - 1] - Tdsio[j]) + c1z * (Tdsi[j - 1]))

                if j > 1 and j < zstep - 1:
                    N.append(-c1z)
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * Tdsio[j] + c1 + c1e * (Tdso[j] - Tdsio[j]) + c1z * (Tdsio[j - 1] - Tdsio[j]))

                if j == zstep - 1:
                    N.append(-c1z - c2z)
                    W.append(0)
                    C.append(3 * c1t + c1z + c2z + c3e)
                    E.append(-c3e)
                    B.append(c1t * Tdsio[j] + c1 + c1z * (Tdsio[j - 1] - Tdsio[j]) + c1t * Tdso[j] + c1t * Tao[j])

            if i == 1:  # Drill string wall

                if j == 0:
                    C.append(c2t + c2e + c2w + c2z)
                    E.append(-c2e)
                    S.append(-c2z)
                    B.append(c2t * Tdso[j] + c2w * Tdsi[j] + c2e * (Tao[j] - Tdso[j]) + c2w * (Tdsio[j] - Tdso[j]) + c2z * (
                            Tdso[j + 1] - Tdso[j]))

                if j > 0 and j < zstep - 1:
                    N.append(-c2z)
                    W.append(-c2w)
                    C.append(c2t + c2e + c2w + 2 * c2z)
                    E.append(-c2e)
                    if j < zstep - 2:
                        S.append(-c2z)
                    B.append(c2t * Tdso[j] + c2e * (Tao[j] - Tdso[j]) + c2w * (Tdsio[j] - Tdso[j]) + c2z * (
                            Tdso[j + 1] - Tdso[j]) + c2z * (Tdso[j - 1] - Tdso[j]))

            if i == 2:  # Annular

                if j == 0:
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    S.append(-c3z)
                    B.append(
                        c3t * Tao[j] + c3 + c3e * (Tcsgo[j] - Tao[j]) + c3w * (Tdso[j] - Tao[j]) + c3z * (Tao[j + 1] - Tao[j]))

                if j > 0 and j < zstep - 1:
                    N.append(0)
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    if j < zstep - 2:
                        S.append(-c3z)
                    B.append(
                        c3t * Tao[j] + c3 + c3e * (Tcsgo[j] - Tao[j]) + c3w * (Tdso[j] - Tao[j]) + c3z * (Tao[j + 1] - Tao[j]))

            if i == 3:  # Casing

                if j == 0:
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(0)
                    S.append(-c4z)
                    B.append(
                        c4t * Tcsgo[j] + c4e * Tsro[j] + c4e * (Tsro[j] - Tcsgo[j]) + c4w * (Tao[j] - Tcsgo[j]) + c4z * (
                                Tcsgo[j + 1] - Tcsgo[j]))

                if j > 0 and j < zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + 2 * c4z)
                    E.append(0)
                    S.append(-c4z)
                    B.append(
                        c4t * Tcsgo[j] + c4e * Tsro[j] + c4e * (Tsro[j] - Tcsgo[j]) + c4w * (Tao[j] - Tcsgo[j]) + c4z * (
                                Tcsgo[j + 1] - Tcsgo[j])
                        + c4z * (Tcsgo[j - 1] - Tcsgo[j]))

                if j == zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(0)
                    B.append(
                        c4t * Tcsgo[j] + c4e * Tsro[j] + c4e * (Tsro[j] - Tcsgo[j]) + c4w * (Tao[j] - Tcsgo[j]) + c4z * (
                                Tcsgo[j - 1] - Tcsgo[j]))

            if i == 4:  # Formation

                if j == 0:
                    W.append(-c5w)
                    C.append(c5w + c5z + c5e + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (Tcsgo[j] - Tsro[j]) + c5z * (Tsro[j + 1] - Tsro[j]) + c5e * Tsro[j] + c5t * Tsro[j])

                if j > 0 and j < zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + 2 * c5z + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(
                        c5w * (Tcsgo[j] - Tsro[j]) + c5z * (Tsro[j + 1] - Tsro[j]) + c5z * (Tsro[j - 1] - Tsro[j]) + c5e *
                        Tsro[j] + c5t * Tsro[j])

                if j == zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + c5z + c5t)
                    B.append(c5w * (Tcsgo[j] - Tsro[j]) + c5z * (Tsro[j - 1] - Tsro[j]) + c5e * Tsro[j] + c5t * Tsro[j])

    #LINEARSYSTEM
    # Creating pentadiagonal matrix
    A = np.zeros((xi * zstep - 3, xi * zstep - 3))

    # Filling up Pentadiagonal Matrix A
    lenC = xi * zstep - 3
    lenN = lenC - xi
    lenW = lenC - 1
    lenE = lenC - 1
    lenS = lenC - xi

    for it in range(lenC):  # Inserting list C
        A[it, it] = C[it]
    for it in range(lenE):  # Inserting list E
        A[it, it + 1] = E[it]
    for it in range(lenW):  # Inserting list W
        A[it + 1, it] = W[it]
    for it in range(lenN):  # Inserting list N
        A[it + xi, it] = N[it]
    for it in range(lenS):  # Inserting list S
        A[it, it + xi] = S[it]

    A[lenC - 1 - (xi - 3) - (xi - 1), lenC - 1 - (xi - 3)] = -c2z
    A[lenC - 1 - (xi - 3) - (xi - 2), lenC - 1 - (xi - 3)] = -c3z

    Temp = np.linalg.solve(A, B)

    for x in range(zstep):
        if x < zstep - 1:
            Tds.append(Temp[5 * x])
        if x == zstep - 1:
            Tds.append(Temp[lenC - 1 - (xi - 3)])
    for x in range(zstep - 1):
        if x < zstep - 2:
            Tdsi.append(Temp[5 * x + 4])
        if x == zstep - 2:
            Tdsi.append(Temp[lenC - 1 - (xi - 3)])
    for x in range(zstep):
        if x < zstep - 1:
            Ta.append(Temp[5 * x + 1])
        if x == zstep - 1:
            Ta.append(Temp[lenC - 1 - (xi - 3)])
    for x in range(zstep):
        if x < zstep - 1:
            Tcsg.append(Temp[5 * x + 2])
        if x == zstep - 1:
            Tcsg.append(Temp[lenC - 2])
    for x in range(zstep):
        if x < zstep - 1:
            Tsr.append(Temp[5 * x + 3])
        if x == zstep - 1:
            Tsr.append(Temp[lenC - 1])

    Tr=Tcsg[:Riser]+[None]*(zstep-Riser)
    for x in range(Riser):
        Tcsg[x]=None

    return Tdsi,Ta,Tr,Tcsg,Tsr