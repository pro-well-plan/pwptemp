import numpy as np


def temp_calc(well, initcond, heatcoeff):

    Tdsi = [well.tin]
    Tds = []
    Ta = []
    Tcsg = []
    Tsr = []
    xi = 5

    # Creating vectors N,W,C,E,S,B
    N = []
    W = []
    C = []
    E = []
    S = []
    B = []

    # Casing:
    c4z = heatcoeff.c4z1
    c4e = heatcoeff.c4e1
    c4w = heatcoeff.c4w1
    c4t = heatcoeff.c4t1
    # Surrounding:
    c5z = heatcoeff.c5z1
    c5w = heatcoeff.c5w1
    c5e = heatcoeff.c5e1
    c5t = heatcoeff.c5t1

    for j in range(well.zstep):

        if j == well.riser:
            # Casing:
            c4z = heatcoeff.c4z2
            c4e = heatcoeff.c4e2
            c4w = heatcoeff.c4w2
            c4t = heatcoeff.c4t2
            # Surrounding:
            c5z = heatcoeff.c5z2
            c5w = heatcoeff.c5w2
            c5e = heatcoeff.c5e2
            c5t = heatcoeff.c5t2

        if j == well.csg3:
            # Casing:
            c4z = heatcoeff.c4z3
            c4e = heatcoeff.c4e3
            c4w = heatcoeff.c4w3
            c4t = heatcoeff.c4t3
            # Surrounding:
            c5z = heatcoeff.c5z3
            c5w = heatcoeff.c5w3
            c5e = heatcoeff.c5e3
            c5t = heatcoeff.c5t3

        if j == well.csg2:
            # Casing:
            c4z = heatcoeff.c4z4
            c4e = heatcoeff.c4e4
            c4w = heatcoeff.c4w4
            c4t = heatcoeff.c4t4
            # Surrounding:
            c5z = heatcoeff.c5z4
            c5w = heatcoeff.c5w4
            c5e = heatcoeff.c5e4
            c5t = heatcoeff.c5t4

        if j == well.csg1:
            # Casing:
            c4z = heatcoeff.c4z5
            c4e = heatcoeff.c4e5
            c4w = heatcoeff.c4w5
            c4t = heatcoeff.c4t5
            # Surrounding:
            c5z = heatcoeff.c5z5
            c5w = heatcoeff.c5w5
            c5e = heatcoeff.c5e5
            c5t = heatcoeff.c5t5

        for i in range(xi):
            if i == 0:  # Inside Drill String
                if j == 1:
                    W.append(0)
                    C.append(heatcoeff.c1t + heatcoeff.c1e + heatcoeff.c1z)
                    E.append(-heatcoeff.c1e)
                    S.append(0)
                    B.append(heatcoeff.c1t * initcond.tdsio[j] + heatcoeff.c1 + heatcoeff.c1e * (initcond.tdso[j] -
                                initcond.tdsio[j]) + heatcoeff.c1z * (initcond.tdsio[j - 1] - initcond.tdsio[j]) +
                                heatcoeff.c1z * (Tdsi[j - 1]))

                if j > 1 and j < well.zstep - 1:
                    N.append(-heatcoeff.c1z)
                    W.append(0)
                    C.append(heatcoeff.c1t + heatcoeff.c1e + heatcoeff.c1z)
                    E.append(-heatcoeff.c1e)
                    S.append(0)
                    B.append(heatcoeff.c1t * initcond.tdsio[j] + heatcoeff.c1 + heatcoeff.c1e * (initcond.tdso[j] -
                                initcond.tdsio[j]) + heatcoeff.c1z * (initcond.tdsio[j - 1] - initcond.tdsio[j]))

                if j == well.zstep - 1:
                    N.append(-heatcoeff.c1z - heatcoeff.c2z)
                    W.append(0)
                    C.append(3 * heatcoeff.c1t + heatcoeff.c1z + heatcoeff.c2z + heatcoeff.c3e)
                    E.append(-heatcoeff.c3e)
                    B.append(heatcoeff.c1t * initcond.tdsio[j] + heatcoeff.c1 + heatcoeff.c1z * (initcond.tdsio[j - 1] -
                                initcond.tdsio[j]) + heatcoeff.c1t * initcond.tdso[j] + heatcoeff.c1t * initcond.tao[j]
                                + heatcoeff.c3)

            if i == 1:  # Drill string wall

                if j == 0:
                    C.append(heatcoeff.c2t + heatcoeff.c2e + heatcoeff.c2w + heatcoeff.c2z)
                    E.append(-heatcoeff.c2e)
                    S.append(-heatcoeff.c2z)
                    B.append(heatcoeff.c2t * initcond.tdso[j] + heatcoeff.c2w * Tdsi[j] + heatcoeff.c2e *
                                (initcond.tao[j] - initcond.tdso[j]) + heatcoeff.c2w * (initcond.tdsio[j] -
                                initcond.tdso[j]) + heatcoeff.c2z * (initcond.tdso[j + 1] - initcond.tdso[j]))

                if 0 < j < well.zstep - 1:
                    N.append(-heatcoeff.c2z)
                    W.append(-heatcoeff.c2w)
                    C.append(heatcoeff.c2t + heatcoeff.c2e + heatcoeff.c2w + 2 * heatcoeff.c2z)
                    E.append(-heatcoeff.c2e)
                    if j < well.zstep - 2:
                        S.append(-heatcoeff.c2z)
                    B.append(heatcoeff.c2t * initcond.tdso[j] + heatcoeff.c2e * (initcond.tao[j] - initcond.tdso[j]) +
                                heatcoeff.c2w * (initcond.tdsio[j] - initcond.tdso[j]) + heatcoeff.c2z *
                                (initcond.tdso[j + 1] - initcond.tdso[j]) + heatcoeff.c2z * (initcond.tdso[j - 1] -
                                initcond.tdso[j]))

            if i == 2:  # Annular

                if j == 0:
                    W.append(-heatcoeff.c3w)
                    C.append(heatcoeff.c3t + heatcoeff.c3e + heatcoeff.c3w + heatcoeff.c3z)
                    E.append(-heatcoeff.c3e)
                    S.append(-heatcoeff.c3z)
                    B.append(heatcoeff.c3t * initcond.tao[j] + heatcoeff.c3 + heatcoeff.c3e * (initcond.tcsgo[j] -
                                initcond.tao[j]) + heatcoeff.c3w * (initcond.tdso[j] - initcond.tao[j]) + heatcoeff.c3z
                                * (initcond.tao[j + 1] - initcond.tao[j]))

                if j > 0 and j < well.zstep - 1:
                    N.append(0)
                    W.append(-heatcoeff.c3w)
                    C.append(heatcoeff.c3t + heatcoeff.c3e + heatcoeff.c3w + heatcoeff.c3z)
                    E.append(-heatcoeff.c3e)
                    if j < well.zstep - 2:
                        S.append(-heatcoeff.c3z)
                    B.append(heatcoeff.c3t * initcond.tao[j] + heatcoeff.c3 + heatcoeff.c3e * (initcond.tcsgo[j] -
                                initcond.tao[j]) + heatcoeff.c3w * (initcond.tdso[j] - initcond.tao[j]) + heatcoeff.c3z
                                * (initcond.tao[j + 1] - initcond.tao[j]))

            if i == 3:  # Casing

                if j == 0:
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(0)
                    S.append(-c4z)
                    B.append(c4t * initcond.tcsgo[j] + c4e * initcond.tsro[j] + c4e * (initcond.tsro[j] -
                                initcond.tcsgo[j]) + c4w * (initcond.tao[j] - initcond.tcsgo[j]) + c4z *
                                (initcond.tcsgo[j + 1] - initcond.tcsgo[j]))

                if 0 < j < well.zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + 2 * c4z)
                    E.append(0)
                    S.append(-c4z)
                    B.append(c4t * initcond.tcsgo[j] + c4e * initcond.tsro[j] + c4e * (initcond.tsro[j] -
                                initcond.tcsgo[j]) + c4w * (initcond.tao[j] - initcond.tcsgo[j]) + c4z *
                                (initcond.tcsgo[j + 1] - initcond.tcsgo[j]) + c4z * (initcond.tcsgo[j - 1] -
                                initcond.tcsgo[j]))

                if j == well.zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(0)
                    B.append(c4t * initcond.tcsgo[j] + c4e * initcond.tsro[j] + c4e * (initcond.tsro[j] -
                                initcond.tcsgo[j]) + c4w * (initcond.tao[j] - initcond.tcsgo[j]) + c4z *
                                (initcond.tcsgo[j - 1] - initcond.tcsgo[j]))

            if i == 4:  # Formation

                if j == 0:
                    W.append(-c5w)
                    C.append(c5w + c5z + c5e + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (initcond.tcsgo[j] - initcond.tsro[j]) + c5z * (initcond.tsro[j + 1] -
                                initcond.tsro[j]) + c5e * initcond.tsro[j] + c5t * initcond.tsro[j])

                if 0 < j < well.zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + 2 * c5z + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (initcond.tcsgo[j] - initcond.tsro[j]) + c5z * (initcond.tsro[j + 1] -
                                initcond.tsro[j]) + c5z * (initcond.tsro[j - 1] - initcond.tsro[j]) + c5e *
                                initcond.tsro[j] + c5t * initcond.tsro[j])

                if j == well.zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + c5z + c5t)
                    B.append(c5w * (initcond.tcsgo[j] - initcond.tsro[j]) + c5z * (initcond.tsro[j - 1] -
                                initcond.tsro[j]) + c5e * initcond.tsro[j] + c5t * initcond.tsro[j])

    #LINEARSYSTEM
    # Creating pentadiagonal matrix
    A = np.zeros((xi * well.zstep - 3, xi * well.zstep - 3))

    # Filling up Pentadiagonal Matrix A
    lenC = xi * well.zstep - 3
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

    A[lenC - 1 - (xi - 3) - (xi - 1), lenC - 1 - (xi - 3)] = -heatcoeff.c2z
    A[lenC - 1 - (xi - 3) - (xi - 2), lenC - 1 - (xi - 3)] = -heatcoeff.c3z

    Temp = np.linalg.solve(A, B)

    for x in range(well.zstep):
        if x < well.zstep - 1:
            Tds.append(Temp[5 * x])
        if x == well.zstep - 1:
            Tds.append(Temp[lenC - 1 - (xi - 3)])
    for x in range(well.zstep - 1):
        if x < well.zstep - 2:
            Tdsi.append(Temp[5 * x + 4])
        if x == well.zstep - 2:
            Tdsi.append(Temp[lenC - 1 - (xi - 3)])
    for x in range(well.zstep):
        if x < well.zstep - 1:
            Ta.append(Temp[5 * x + 1])
        if x == well.zstep - 1:
            Ta.append(Temp[lenC - 1 - (xi - 3)])
    for x in range(well.zstep):
        if x < well.zstep - 1:
            Tcsg.append(Temp[5 * x + 2])
        if x == well.zstep - 1:
            Tcsg.append(Temp[lenC - 2])
    for x in range(well.zstep):
        if x < well.zstep - 1:
            Tsr.append(Temp[5 * x + 3])
        if x == well.zstep - 1:
            Tsr.append(Temp[lenC - 1])

    Tr = Tcsg[:well.riser]+[None]*(well.zstep-well.riser)
    for x in range(well.riser):
        Tcsg[x] = None
    Toh = [None]*well.csg1 + Tcsg[well.csg1:]
    for x in range(well.csg1, well.zstep):
        Tcsg[x] = None

    class TempCalc(object):
        def __init__(self):
            self.tdsi = Tdsi
            self.tds = Tds
            self.ta = Ta
            self.tr = Tr
            self.tcsg = Tcsg
            self.toh = Toh
            self.tsr = Tsr

    return TempCalc()
