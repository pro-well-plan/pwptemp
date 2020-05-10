from unittest import TestCase
from pwptemp import wellpath


class TestLinearSystem(TestCase):
    def test_temp_calc_drilling(self):
        from pwptemp.drilling import input, initcond, heatcoefficients, linearsystem
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
        well = well.define_density(ic, cond=0)
        hc = heatcoefficients.heat_coef(well, 1)
        tdist = linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tdsi), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tcsg), len(tdist.tsr))

    def test_temp_calc_production(self):
        from pwptemp.production import input, initcond, heatcoefficients, linearsystem
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
        tt = ic.tto
        tc = ic.tco
        well = well.define_density(ic, cond=0)
        hc = heatcoefficients.heat_coef(well, 1, tt, tc)
        tdist = linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tft), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tc), len(tdist.tsr))

    def test_temp_calc_injection(self):
        from pwptemp.injection import input, initcond, heatcoefficients, linearsystem
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
        tt = ic.tto
        tc = ic.tco
        well = well.define_density(ic, cond=0)
        hc = heatcoefficients.heat_coef(well, 1, tt, tc)
        tdist = linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tft), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tc), len(tdist.tsr))
