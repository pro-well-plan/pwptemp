from unittest import TestCase
from pwptemp.InitCond import init_cond
from pwptemp.WellPath import wellpath
from pwptemp.LinearSystem import temp_calc

class TestWellPath(TestCase):
    def test_wellpath(self):
        md, tvd, deltaz, zstep = wellpath(5000)
        a, b, c, d, e, f = init_cond(15, 2, -0.005, 0.0238, 100, tvd, 50)
        Tdsi, Ta, Tr, Tcsg, Tsr = temp_calc(15, a, b, c, d, e, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 100, 0, 500, 1000, 1500)
        self.assertEqual(len(Tdsi), len(Ta))