from unittest import TestCase
import well_profile as wp

trajectory = wp.load('trajectory1.xlsx')


class TestLinearSystem(TestCase):

    def test_temp_calc_production(self):
        from pwptemp.production import input, initcond, heatcoefficients, linearsystem
        tdata = input.data()
        well = input.set_well(tdata, trajectory)
        ic = initcond.init_cond(well)
        tt = ic.tto
        tc = ic.tco
        well = well.define_viscosity(ic)
        well = well.define_density(ic, cond=0)
        hc = heatcoefficients.heat_coef(well, 1, tt, tc)
        tdist = linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tft), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tc), len(tdist.tsr))

    def test_temp_calc_injection(self):
        from pwptemp.injection import input, initcond, heatcoefficients, linearsystem
        tdata = input.data()
        well = input.set_well(tdata, trajectory)
        ic = initcond.init_cond(well)
        tt = ic.tto
        tc = ic.tco
        well = well.define_viscosity(ic)
        well = well.define_density(ic, cond=0)
        hc = heatcoefficients.heat_coef(well, 1, tt, tc)
        tdist = linearsystem.temp_calc(well, ic, hc)
        self.assertEqual(len(tdist.tft), len(tdist.ta), len(tdist.tr))
        self.assertEqual(len(tdist.tr), len(tdist.tc), len(tdist.tsr))
