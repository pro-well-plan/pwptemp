from unittest import TestCase
import pwptemp


class TestLinearSystem(TestCase):
    def test_temp_calc(self):
        tdata = pwptemp.drill_op.input.data()
        depths = pwptemp.wellpath.get(3000, 50)
        well = pwptemp.drill_op.input.set_well(tdata, depths)
        ic = pwptemp.drill_op.initcond.init_cond(well)
        hc = pwptemp.drill_op.heatcoefficients.heat_coef(well, 1)
        tdist = pwptemp.drill_op.linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tdsi), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tcsg), len(tdist.tsr))
