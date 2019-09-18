from unittest import TestCase
from pwptemp.initcond import init_cond
from pwptemp.wellpath import wellpath
from pwptemp.linearsystem import temp_calc


class TestLinearSystem(TestCase):
    def test_temp_calc(self):
        tvd = wellpath(5000)[1]
        a, b, c, d, e, f = init_cond(15, 2, -0.005, 0.0238, 100, tvd, 50)
        tdsi, ta, tr, tcsg, tsr = temp_calc(15, a, b, c, d, e, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 100, 0, 500, 1000, 1500)
        self.assertEqual(len(tdsi), len(ta), len(tr))
        self.assertEqual(len(tr), len(tcsg), len(tsr))
