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
        total = eff.flow + eff.hs + eff.fm
        self.assertEqual(round(total), 100)
        self.assertIsInstance(eff.flow, float)
        self.assertIsInstance(eff.hs, float)
        self.assertIsInstance(eff.fm, float)
