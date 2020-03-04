from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input, heatcoefficients


class TestWellPath(TestCase):
    def test_wellpath(self):
        depths = wellpath.get(100, 50)
        well = input.set_well(input.data(), depths)
        hc = heatcoefficients.heat_coef(well, 1)[0]
        for i in range(len(hc)):
            for j in range(len(hc[0])):
                for k in range(len(hc[0, 0])):
                    self.assertNotEqual(hc[i, j][k], 0)
