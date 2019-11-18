from unittest import TestCase
import pwptemp


class TestWellPath(TestCase):
    def test_wellpath(self):
        depths = pwptemp.wellpath.get(100, 50)
        well = pwptemp.drill_op.input.set_well(pwptemp.drill_op.input.data(), depths)
        hc = pwptemp.drill_op.heatcoefficients.heat_coef(well, 1)
        for i in range(len(hc)):
            for j in range(len(hc[0])):
                for k in range(len(hc[0, 0])):
                    self.assertNotEqual(hc[i, j][k], 0)
