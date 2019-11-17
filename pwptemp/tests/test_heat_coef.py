from unittest import TestCase
import pwptemp


class TestWellPath(TestCase):
    def test_wellpath(self):
        depths = pwptemp.wellpath.get(100, 50)
        well = pwptemp.input.set_well(pwptemp.input.data(), depths)
        hc = pwptemp.heatcoefficients.heat_coef(well, 1)
        for i in range(len(hc)):
            for j in range(len(hc[0])):
                for k in range(len(hc[0, 0])):
                    self.assertNotEqual(hc[i, j][k], 0)
