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
    c3t = hc_3[3][zstep]

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

    cbe = coefficients[5]
    cbt = coefficients[6]
    cbz = coefficients[7]

    return c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t, cbe, \
           cbt, cbz


def temp_calc(well, initcond, heatcoeff):
    """
    Build the penta-diagonal matrix and solve it to get the well temperature distribution.
    :param well: a well object created from the function set_well()
    :param initcond: object with initial temperature profiles
    :param heatcoeff: list with distribution of heat transfer coefficients
    :return: object with final well temperature distribution
    """

    from numpy import zeros, linalg

    Tft = [well.tin]
    Tt = []
    Ta = []
    tc = []
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
        c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3t, c4z, c4e, c4w, c4t, c5z, c5e, c5w, c5t, cbe, \
        cbt, cbz = define_coef(heatcoeff, j)
        for i in range(xi):

            if i == 0:  # Inside Tubing

                if j == 1:
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * initcond.tfto[j]    # Center(t=0)
                             + c1       # Heat Source
                             + c1e * (initcond.tto[j] - initcond.tfto[j])     # East(t=0)
                             + c1z * (initcond.tfto[j - 1] - initcond.tfto[j])
                             + c1z * well.tin)       # N/S(t=0)

                if 1 < j < well.zstep - 1:
                    N.append(-c1z)
                    W.append(0)
                    C.append(c1t + c1e + c1z)
                    E.append(-c1e)
                    S.append(0)
                    B.append(c1t * initcond.tfto[j]    # Center(t=0)
                             + c1       # Heat Source
                             + c1e * (initcond.tto[j] - initcond.tfto[j])     # East(t=0)
                             + c1z * (initcond.tfto[j - 1] - initcond.tfto[j]))       # N/S(t=0)

                if j == well.zstep - 1:
                    N.append(-c1z)
                    W.append(0)
                    C.append(cbt + c1z)
                    E.append(0)
                    B.append(cbt * initcond.tfto[j]    # Center(t=0)
                             + c1z * (initcond.tfto[j - 1] - initcond.tfto[j]))  # N/S(t=0)

            if i == 1:  # Tubing wall

                if j == 0:
                    C.append(c2t + c2e + c2w + c2z)
                    E.append(-c2e)
                    S.append(-c2z)
                    B.append(c2t * initcond.tto[j]
                             + c2e * (initcond.tao[j] - initcond.tto[j])
                             + c2w * (initcond.tfto[j] - initcond.tto[j])
                             + c2z * (initcond.tto[j + 1] - initcond.tto[j])
                             + c2w * well.tin)

                if 0 < j < well.zstep - 1:
                    N.append(-c2z)
                    W.append(-c2w)
                    C.append(c2t + c2e + c2w + 2 * c2z)
                    E.append(-c2e)
                    S.append(-c2z)
                    B.append(c2t * initcond.tto[j]
                             + c2e * (initcond.tao[j] - initcond.tto[j])
                             + c2w * (initcond.tfto[j] - initcond.tto[j])
                             + c2z * (initcond.tto[j + 1] - initcond.tto[j])
                             + c2z * (initcond.tto[j - 1] - initcond.tto[j]))

                if j == well.zstep - 1:
                    N.append(-c2z)
                    W.append(0)
                    C.append(c2t + c2z)
                    E.append(0)
                    B.append(c2t * initcond.tto[j]
                             + c2z * (initcond.tto[j - 1] - initcond.tto[j]))

            if i == 2:  # Annular

                if j == 0:
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + c3z)
                    E.append(-c3e)
                    S.append(-c3z)
                    B.append(c3t * initcond.tao[j]
                             + c3e * (initcond.tco[j] - initcond.tao[j])
                             + c3w * (initcond.tto[j] - initcond.tao[j])
                             + c3z * (initcond.tao[j + 1] - initcond.tao[j]))

                if 0 < j < well.zstep - 1:
                    N.append(-c3z)
                    W.append(-c3w)
                    C.append(c3t + c3e + c3w + 2 * c3z)
                    E.append(-c3e)
                    S.append(-c3z)
                    B.append(c3t * initcond.tao[j]
                             + c3e * (initcond.tco[j] - initcond.tao[j])
                             + c3w * (initcond.tto[j] - initcond.tao[j])
                             + c3z * (initcond.tao[j + 1] - initcond.tao[j])
                             + c3z * (initcond.tao[j - 1] - initcond.tao[j]))

                if j == well.zstep - 1:
                    N.append(-c3z)
                    W.append(0)
                    C.append(c3t + c3e + c3z)
                    E.append(-c3e)
                    B.append(c3t * initcond.tao[j]
                             + c3e * (initcond.tco[j] - initcond.tao[j])
                             + c3z * (initcond.tao[j - 1] - initcond.tao[j]))

            if i == 3:  # Casing

                if j == 0:
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(-c4e)
                    S.append(-c4z)
                    B.append(c4t * initcond.tco[j]   # Center(t=0)
                             + c4e * (initcond.tsro[j] - initcond.tco[j])  # East(t=0)
                             + c4w * (initcond.tao[j] - initcond.tco[j])  # West(t=0)
                             + c4z * (initcond.tco[j + 1] - initcond.tco[j]))   # N/S(t=0)

                if 0 < j < well.zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + 2 * c4z)
                    E.append(-c4e)
                    S.append(-c4z)
                    B.append(c4t * initcond.tco[j]    # Center(t=0)
                             + c4e * (initcond.tsro[j] - initcond.tco[j])     # East(t=0)
                             + c4w * (initcond.tao[j] - initcond.tco[j])      # West(t=0)
                             + c4z * (initcond.tco[j + 1] - 2 * initcond.tco[j] + initcond.tco[j - 1])) # N/S(t=0)

                if j == well.zstep - 1:
                    N.append(-c4z)
                    W.append(-c4w)
                    C.append(c4t + c4e + c4w + c4z)
                    E.append(-c4e)
                    B.append(c4t * initcond.tco[j]    # Center(t=0)
                             + c4e * (initcond.tsro[j] - initcond.tco[j])     # East(t=0)
                             + c4w * (initcond.tao[j] - initcond.tco[j])      # West(t=0)
                             + c4z * (initcond.tco[j - 1] - initcond.tco[j]))       # N/S(t=0))

            if i == 4:  # Surrounding Space

                if j == 0:
                    W.append(-c5w)
                    C.append(c5w + c5z + c5e + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (initcond.tco[j] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j + 1] - initcond.tsro[j])
                             + c5e * initcond.tsro[j])

                if 0 < j < well.zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + 2 * c5z + c5t)
                    E.append(0)
                    S.append(-c5z)
                    B.append(c5w * (initcond.tco[j] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j + 1] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j - 1] - initcond.tsro[j])
                             + c5e * initcond.tsro[j])

                if j == well.zstep - 1:
                    N.append(-c5z)
                    W.append(-c5w)
                    C.append(c5w + c5e + c5z + c5t)
                    B.append(c5w * (initcond.tco[j] - initcond.tsro[j])
                             + c5z * (initcond.tsro[j - 1] - initcond.tsro[j])
                             + c5t * initcond.tsro[j]
                             + c5e * initcond.tsro[j])

    #LINEARSYSTEM
    # Creating pentadiagonal matrix
    A = zeros((xi * well.zstep - 1, xi * well.zstep - 1))

    # Filling up Pentadiagonal Matrix A
    lenC = xi * well.zstep - 1
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

    Temp = linalg.solve(A, B)

    for x in range(well.zstep):
        Tt.append(Temp[5 * x])
        if x < well.zstep-1:
            Tft.append(Temp[5 * x + 4])
            Ta.append(Temp[5 * x + 1])
        if x == well.zstep - 1:
            Ta.append(Tft[-1])
        tc.append(Temp[5 * x + 2])
        Tsr.append(Temp[5 * x + 3])


    t3 = tc.copy()

    tr = tc[:well.riser] + [None] * (well.zstep - well.riser)
    for x in range(well.riser):
        tc[x] = None

    csgs_reach = int(well.casings[0, 2] / well.deltaz)  # final depth still covered with casing(s)

    Toh = [None] * csgs_reach + tc[csgs_reach:]
    for x in range(csgs_reach, well.zstep):
        tc[x] = None

    class TempCalc(object):
        def __init__(self):
            self.tft = Tft
            self.tt = Tt
            self.ta = Ta
            self.t3 = t3
            self.tc = tc
            self.tr = tr
            self.tsr = Tsr
            self.toh = Toh
            self.csgs_reach = csgs_reach

    return TempCalc()
