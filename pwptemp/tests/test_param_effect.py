from unittest import TestCase
import pwptemp


class TestAnalysis(TestCase):
    def test_temp_time(self):
        tdata = pwptemp.drill_op.input.data()
        depths = pwptemp.wellpath.get(3000, 50)
        well = pwptemp.drill_op.input.set_well(tdata, depths)
        td = pwptemp.drill_op.main.temp_time(24, well)
        eff = pwptemp.drill_op.analysis.param_effect(td, well)
        total = eff.flow + eff.hs + eff.fm
        self.assertEqual(round(total), 100)
        self.assertIsInstance(eff.flow, float)
        self.assertIsInstance(eff.hs, float)
        self.assertIsInstance(eff.fm, float)
