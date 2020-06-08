def define_coef(coefficients, zstep):
    """
    Retrieves respective heat transfer coefficients for certain depth point.
    :param coefficients: list with distribution of heat transfer coefficients
    :param zstep: depth step
    :return: values of heat coefficients for each section at the same depth
    """

    hc_1 = coefficients[0]
    c1z = hc_1[0][zstep]
    c1e = hc_1[1][zstep]
    c1 = hc_1[2][zstep]
    c1t = hc_1[3][zstep]

    hc_2 = coefficients[1]
    c2z = hc_2[0][zstep]
    c2e = hc_2[1][zstep]
    c2w = hc_2[2][zstep]
    c2t = hc_2[3][zstep]

    hc_3 = coefficients[2]
    c3z = hc_3[0][zstep]
    c3e = hc_3[1][zstep]
    c3w = hc_3[2][zstep]
    c3 = hc_3[3][zstep]
    c3t = hc_3[4][zstep]

    hc_4 = coefficients[3]
    c4z = hc_4[0][zstep]
    c4e = hc_4[1][zstep]
    c4w = hc_4[2][zstep]
    c4t = hc_4[3][zstep]

    hc_5 = coefficients[4]
    c5z = hc_5[0][zstep]
    c5e = hc_5[1][zstep]
    c5w = hc_5[2][zstep]
    c5t = hc_5[3][zstep]

    cb = coefficients[5]
    cbe = coefficients[6]
    cbt = coefficients[7]
    cbz = coefficients[8]

    return c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t, cb, \
           cbe, cbt, cbz


def temp_calc(well, initcond, heatcoeff):
    """
    Build the penta-diagonal matrix and solve it to get the well temperature distribution.
    :param well: a well object created from the function set_well()
    :param initcond: object with initial temperature profiles
    :param heatcoeff: list with distribution of heat transfer coefficients
    :return: object with final well temperature distribution
    """

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

    for j in range(well.zstep):
        c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t, cb, \
        cbe, cbt, cbz = define_coef(heatcoeff, j)

        for i in range(xi):
            if i == 0:  # Inside Drill String
                if j == 1:
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * initcond.tdsio[j]    # Center(t=0)
                             + c1   # Heat Source
                             + c1e * (initcond.tdso[j] - initcond.tdsio[j])     # East(t=0)
                             + c1z * (initcond.tdsio[j - 1] - initcond.tdsio[j])       # N/S(t=0)
                             + c1z * (Tdsi[j - 1]))     # Tin

                if 1 < j < well.zstep - 1:
                    N.append(-c1z)
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * initcond.tdsio[j]    # Center(t=0)
                             + c1       # Heat Source
                             + c1e * (initcond.tdso[j] - initcond.tdsio[j])     # East(t=0)
                             + c1z * (initcond.tdsio[j - 1] - initcond.tdsio[j]))       # N/S(t=0)

                if j == well.zstep - 1:     # Cell where fluid flows out of the tubing and then go to annular
                    N.append(-cbz)
                    W.append(0)
                    C.append(cbt + cbz + cbe)     # Note that c1t = c3t since it's the same fluid
                    E.append(-cbe)
                    B.append(cbt * initcond.tdsio[j]    # Center(t=0)
                             + cb       # Heat Source
                             + cbe * (initcond.tdso[j] - initcond.tdsio[j])     # East(t=0)
                             + cbz * (initcond.tdsio[j - 1] - initcond.tdsio[j]))       # N/S(t=0)

            if i == 1:  # Drill string wall

                if j == 0:
                    C.append(c2t + c2e + c2w + c2z)
                    E.append(-c2e)
                    S.append(-c2z)
                    B.append(c2t * initcond.tdso[j]
                             + c2w * Tdsi[j]
                             + c2e * (initcond.tao[j] - initcond.tdso[j])
                             + c2w * (initcond.tdsio[j] - initcond.tdso[j])
                             + c2z * (initcond.tdso[j + 1] - initcond.tdso[j]))

                if 0 < j < well.zstep - 1:
                    N.append(-c2z)
                    W.append(-c2w)
                    C.append(c2t + c2e + c2w + 2 * c2z)
                    E.append(-c2e)
                    if j < well.zstep - 2:
                        S.append(-c2z)
                    B.append(c2t * initcond.tdso[j]
                             + c2e * (initcond.tao[j] - initcond.tdso[j])
                             + c2w * (initcond.tdsio[j] - initcond.tdso[j])
                             + c2z * (initcond.tdso[j + 1] - initcond.tdso[j])
                             + c2z * (initcond.tdso[j - 1] - initcond.tdso[j]))

            if i == 2:  # Annular

                if j == 0:
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    S.append(-c3z)
                    B.append(c3t * initcond.tao[j]
                             + c3
                             + c3e * (initcond.tcsgo[j] - initcond.tao[j])
                             + c3w * (initcond.tdso[j] - initcond.tao[j])
                             + c3z * (initcond.tao[j + 1] - initcond.tao[j]))

                if 0 < j < well.zstep - 1:
                    N.append(0)
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    if j < well.zstep - 2:
                        S.append(-c3z)
                    B.append(c3t * initcond.tao[j]
                             + c3
                             + c3e * (initcond.tcsgo[j] - initcond.tao[j])
                             + c3w * (initcond.tdso[j] - initcond.tao[j])
                             + c3z * (initcond.tao[j + 1] - initcond.tao[j]))

            if i == 3:  # Casing

                if j == 0:
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(- c4e)
                    S.append(-c4z)
                    B.append(c4t * initcond.tcsgo[j]   # Center(t=0)
                             + c4e * (initcond.tsro[j] - initcond.tcsgo[j])  # East(t=0)
                             + c4w * (initcond.tao[j] - initcond.tcsgo[j])  # West(t=0)
                             + c4z * (initcond.tcsgo[j + 1] - initcond.tcsgo[j]))   # N/S(t=0)

                if 0 < j < well.zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + 2 * c4z)
                    E.append(- c4e)
                    S.append(-c4z)
                    B.append(c4t * initcond.tcsgo[j]    # Center(t=0)
                             + c4e * (initcond.tsro[j] - initcond.tcsgo[j])     # East(t=0)
                             + c4w * (initcond.tao[j] - initcond.tcsgo[j])      # West(t=0)
                             + c4z * (initcond.tcsgo[j + 1] - 2 * initcond.tcsgo[j] + initcond.tcsgo[j - 1])) # N/S(t=0)

                if j == well.zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(- c4e)
                    B.append(c4t * initcond.tcsgo[j]    # Center(t=0)
                             + c4e * (initcond.tsro[j] - initcond.tcsgo[j])     # East(t=0)
                             + c4w * (initcond.tao[j] - initcond.tcsgo[j])      # West(t=0)
                             + c4z * (initcond.tcsgo[j - 1] - initcond.tcsgo[j]))       # N/S(t=0)

            if i == 4:  # Surrounding Space

                if j == 0:
                    W.append(-c5w)
                    C.append(c5w + c5z + c5e + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (initcond.tcsgo[j] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j + 1] - initcond.tsro[j])
                             + c5e * initcond.tsro[j]
                             + c5t * initcond.tsro[j])

                if 0 < j < well.zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + 2 * c5z + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (initcond.tcsgo[j] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j + 1] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j - 1] - initcond.tsro[j])
                             + c5e * initcond.tsro[j] +
                             c5t * initcond.tsro[j])

                if j == well.zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + c5z + c5t)
                    B.append(c5w * (initcond.tcsgo[j] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j - 1] - initcond.tsro[j])
                             + c5e * initcond.tsro[j]
                             + c5t * initcond.tsro[j])

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

    t3 = Tcsg.copy()

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
            self.t3 = t3
            self.tcsg = Tcsg
            self.toh = Toh
            self.tsr = Tsr
            self.csgs_reach = csgs_reach

    return TempCalc()
