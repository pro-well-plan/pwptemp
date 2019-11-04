from unittest import TestCase
import pwptemp


class TestWellPath(TestCase):
    def test_wellpath(self):
        depths = pwptemp.wellpath.get(100, 50)
        well = pwptemp.input.set_well(pwptemp.input.tdict(), depths)
        hc = pwptemp.heatcoefficients.heat_coef(well, 1)
        p = (hc.c1z, hc.c1e, hc.c1, hc.c1t, hc.c2z, hc.c2e, hc.c2w, hc.c2t, hc.c3z, hc.c3e, hc.c3w, hc.c3, hc.c3t,
             hc.c4z, hc.c4e, hc.c4w, hc.c4t, hc.c5z, hc.c5w, hc.c5e, hc.c5t, hc.c4z1, hc.c4e1, hc.c4w1, hc.c4t1,
             hc.c5z1, hc.c5w1, hc.c5e1, hc.c5t1, hc.c4z2, hc.c4e2, hc.c4w2, hc.c4t2, hc.c5z2, hc.c5w2, hc.c5e2,
             hc.c5t2, hc.c4z3, hc.c4e3, hc.c4w3, hc.c4t3, hc.c5z3, hc.c5w3, hc.c5e3, hc.c5t3, hc.c4z4, hc.c4e4, hc.c4w4,
             hc.c4t4, hc.c5z4, hc.c5w4, hc.c5e4, hc.c5t4, hc.c4z5, hc.c4e5, hc.c4w5, hc.c4t5, hc.c5z5, hc.c5w5, hc.c5e5,
             hc.c5t5)
        for i in p:
            self.assertNotEqual(i, 0)
