from unittest import TestCase
from pwptemp.heatcoefficients import heat_coef
from pwptemp.input import WellTemperature, temp_dict


class TestWellPath(TestCase):
    def test_wellpath(self):
        well = WellTemperature(temp_dict)
        c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5w, c5e, c5t, \
        c4z1, c4e1, c4w1, c4t1, c5z1, c5w1, c5e1, c5t1, c4z2, c4e2, c4w2, c4t2, c5z2, c5w2, c5e2, c5t2, c4z3, c4e3, \
        c4w3, c4t3, c5z3, c5w3, c5e3, c5t3, c4z4, c4e4, c4w4, c4t4, c5z4, c5w4, c5e4, c5t4, c4z5, c4e5, c4w5, c4t5, \
        c5z5, c5w5, c5e5, c5t5 = heat_coef(well.rhol, well.cl, well.vp, well.h1, well.r1, well.qp, well.lambdal,
                                           well.r2, well.h2, well.rhod, well.cd, well.va, well.r3, well.h3, well.qa,
                                           well.lambdar, well.lambdarw, well.lambdaw, well.cr, well.cw, well.rhor,
                                           well.rhow, well.r4, well.r5, well.rfm, well.lambdac, well.lambdacsr,
                                           well.lambdasr, well.lambdasrfm, well.cc, well.csr, well.rhoc, well.rhosr,
                                           well.lambdafm, well.cfm, well.rhofm, 50, 1, well.lambdasr2,
                                           well.lambdasr3, well.lambdacsr2, well.lambdacsr3, well.lambdasrfm2,
                                           well.lambdasrfm3, well.csr2, well.csr3)
        p = (c1z, c1e, c1, c1t, c2z, c2e, c2w, c2t, c3z, c3e, c3w, c3, c3t, c4z, c4e, c4w, c4t, c5z, c5w, c5e, c5t,
             c4z1, c4e1, c4w1, c4t1, c5z1, c5w1, c5e1, c5t1, c4z2, c4e2, c4w2, c4t2, c5z2, c5w2, c5e2, c5t2, c4z3, c4e3,
             c4w3, c4t3, c5z3, c5w3, c5e3, c5t3, c4z4, c4e4, c4w4, c4t4, c5z4, c5w4, c5e4, c5t4, c4z5, c4e5, c4w5, c4t5,
             c5z5, c5w5, c5e5, c5t5)
        for i in p:
            self.assertNotEqual(i, 0)
