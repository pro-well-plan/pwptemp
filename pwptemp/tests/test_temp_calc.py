from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input, initcond, heatcoefficients, linearsystem


class TestLinearSystem(TestCase):
    def test_temp_calc(self):
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
        hc = heatcoefficients.heat_coef(well, 1)
        tdist = linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tdsi), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tcsg), len(tdist.tsr))
