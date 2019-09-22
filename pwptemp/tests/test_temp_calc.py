from unittest import TestCase
import pwptemp


class TestLinearSystem(TestCase):
    def test_temp_calc(self):
        tdata = pwptemp.input.tdict(50)
        depths = pwptemp.wellpath.get(3000, 50)
        well = pwptemp.input.set_well(tdata, depths)
        ic = pwptemp.initcond.init_cond(well)
        hc = pwptemp.heatcoefficients.heat_coef(well, 1)
        tdist = pwptemp.linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tdsi), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tcsg), len(tdist.tsr))
