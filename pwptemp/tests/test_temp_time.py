from unittest import TestCase
import well_profile as wp

trajectory = wp.load('trajectory1.xlsx')


class TestMain(TestCase):
    def test_temp_time_drilling(self):
        from pwptemp.drilling import input, main
        tdata = input.data()
        well = input.set_well(tdata, trajectory)
        td = main.temp_time(2, well)
        self.assertEqual(len(td.tdsi), len(td.ta), len(td.tr))
        self.assertEqual(len(td.tcsg), len(td.tsr), len(td.tfm))
        self.assertEqual(td.time, 2)
        self.assertIsInstance(td.tdsi, list)
        self.assertIsInstance(td.ta, list)
        self.assertIsInstance(td.tr, list)
        self.assertIsInstance(td.tcsg, list)
        self.assertIsInstance(td.tsr, list)
        self.assertIsInstance(td.tfm, list)

    def test_temp_time_injection(self):
        from pwptemp.injection import input, main
        tdata = input.data()
        well = input.set_well(tdata, trajectory)
        td = main.temp_time(2, well)
        self.assertEqual(len(td.tft), len(td.ta), len(td.tr))
        self.assertEqual(len(td.tc), len(td.tsr), len(td.tfm))
        self.assertEqual(td.time, 2)
        self.assertIsInstance(td.tft, list)
        self.assertIsInstance(td.ta, list)
        self.assertIsInstance(td.tr, list)
        self.assertIsInstance(td.tc, list)
        self.assertIsInstance(td.tsr, list)
        self.assertIsInstance(td.tfm, list)
