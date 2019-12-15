from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input, main, analysis


class TestAnalysis(TestCase):
    def test_temp_time(self):
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        td = main.temp_time(24, well)
        eff = analysis.param_effect(td, well)
        final = round(eff.cc + eff.hs + eff.t1, 1)
        self.assertEqual(final, round(eff.t2, 1))
        self.assertIsInstance(eff.cc, float)
        self.assertIsInstance(eff.hs, float)
