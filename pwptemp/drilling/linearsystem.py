def define_coef(coefficients, section):
    c1z = coefficients[section, 0][0]
    c1e = coefficients[section, 0][1]
    c1 = coefficients[section, 0][2]
    c1t = coefficients[section, 0][3]

    c2z = coefficients[section, 1][0]
    c2e = coefficients[section, 1][1]
    c2w = coefficients[section, 1][2]
    c2t = coefficients[section, 1][3]

    c3z = coefficients[section, 2][0]
    c3e = coefficients[section, 2][1]
    c3w = coefficients[section, 2][2]
    c3 = coefficients[section, 2][3]
    c3t = coefficients[section, 2][4]

    c4z = coefficients[section, 3][0]
    c4e = coefficients[section, 3][1]
    c4w = coefficients[section, 3][2]
    c4t = coefficients[section, 3][3]

    c5z = coefficients[section, 4][0]
    c5e = coefficients[section, 4][1]
    c5w = coefficients[section, 4][2]
    c5t = coefficients[section, 4][3]

    return c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t


def temp_calc(well, initcond, heatcoeff):
    from numpy import zeros, linalg

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

    section = 0
    limit = well.riser

    c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t = \
        define_coef(heatcoeff, section)

    for j in range(well.zstep):

        if j == limit:
            section += 1
            if section <= len(well.casings):
                limit = round(well.casings[-section, 2] / well.deltaz)
            c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t = \
                define_coef(heatcoeff, section)

        for i in range(xi):
            if i == 0:  # Inside Drill String
                if j == 1:
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * initcond.tdsio[j] + c1 + c1e * (initcond.tdso[j] - initcond.tdsio[j]) + c1z *
                             (initcond.tdsio[j - 1] - initcond.tdsio[j]) + c1z * (Tdsi[j - 1]))

                if 1 < j < well.zstep - 1:
                    N.append(-c1z)
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * initcond.tdsio[j] + c1 + c1e * (initcond.tdso[j] - initcond.tdsio[j]) + c1z *
                             (initcond.tdsio[j - 1] - initcond.tdsio[j]))

                if j == well.zstep - 1:
                    N.append(-c1z - c2z)
                    W.append(0)
                    C.append(3 * c1t + c1z + c2z + c3e)
                    E.append(-c3e)
                    B.append(c1t * initcond.tdsio[j] + c1 + c1z * (initcond.tdsio[j - 1] - initcond.tdsio[j]) + c1t *
                             initcond.tdso[j] + c1t * initcond.tao[j] + c3)

            if i == 1:  # Drill string wall

                if j == 0:
                    C.append(c2t + c2e + c2w + c2z)
                    E.append(-c2e)
                    S.append(-c2z)
                    B.append(c2t * initcond.tdso[j] + c2w * Tdsi[j] + c2e * (initcond.tao[j] - initcond.tdso[j]) + c2w *
                             (initcond.tdsio[j] - initcond.tdso[j]) + c2z * (initcond.tdso[j + 1] - initcond.tdso[j]))

                if 0 < j < well.zstep - 1:
                    N.append(-c2z)
                    W.append(-c2w)
                    C.append(c2t + c2e + c2w + 2 * c2z)
                    E.append(-c2e)
                    if j < well.zstep - 2:
                        S.append(-c2z)
                    B.append(c2t * initcond.tdso[j] + c2e * (initcond.tao[j] - initcond.tdso[j]) + c2w *
                             (initcond.tdsio[j] - initcond.tdso[j]) + c2z * (initcond.tdso[j + 1] - initcond.tdso[j]) +
                             c2z * (initcond.tdso[j - 1] - initcond.tdso[j]))

            if i == 2:  # Annular

                if j == 0:
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    S.append(-c3z)
                    B.append(c3t * initcond.tao[j] + c3 + c3e * (initcond.tcsgo[j] - initcond.tao[j]) + c3w *
                             (initcond.tdso[j] - initcond.tao[j]) + c3z * (initcond.tao[j + 1] - initcond.tao[j]))

                if 0 < j < well.zstep - 1:
                    N.append(0)
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    if j < well.zstep - 2:
                        S.append(-c3z)
                    B.append(c3t * initcond.tao[j] + c3 + c3e * (initcond.tcsgo[j] - initcond.tao[j]) + c3w *
                             (initcond.tdso[j] - initcond.tao[j]) + c3z * (initcond.tao[j + 1] - initcond.tao[j]))

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
    A = zeros((xi * well.zstep - 3, xi * well.zstep - 3))

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

    A[lenC - 1 - (xi - 3) - (xi - 1), lenC - 1 - (xi - 3)] = -c2z
    A[lenC - 1 - (xi - 3) - (xi - 2), lenC - 1 - (xi - 3)] = -c3z

    Temp = linalg.solve(A, B)

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

    csgs_reach = int(well.casings[0, 2] / well.deltaz)    # final depth still covered with casing(s)

    Toh = [None]*csgs_reach + Tcsg[csgs_reach:]
    for x in range(csgs_reach, well.zstep):
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
            self.csgs_reach = csgs_reach

    return TempCalc()
