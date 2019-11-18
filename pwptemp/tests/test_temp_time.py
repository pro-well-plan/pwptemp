from unittest import TestCase
import pwptemp


class TestMain(TestCase):
    def test_temp_time(self):
        tdata = pwptemp.drill_op.input.data()
        depths = pwptemp.wellpath.get(3000, 50)
        well = pwptemp.drill_op.input.set_well(tdata, depths)
        td = pwptemp.drill_op.main.temp_time(24, well)
        self.assertEqual(len(td.tdsi), len(td.ta), len(td.tr))
        self.assertEqual(len(td.tcsg), len(td.tsr), len(td.tfm))
        self.assertEqual(td.time, 24)
        self.assertIsInstance(td.tdsi, list)
        self.assertIsInstance(td.ta, list)
        self.assertIsInstance(td.tr, list)
        self.assertIsInstance(td.tcsg, list)
        self.assertIsInstance(td.tsr, list)
        self.assertIsInstance(td.tfm, list)
