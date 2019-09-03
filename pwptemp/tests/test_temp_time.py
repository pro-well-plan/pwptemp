from unittest import TestCase
from pwptemp.Input import WellTemperature, temp_dict
from pwptemp.WellPath import wellpath
from pwptemp.Main import temp_time


class TestLinearSystem(TestCase):
    def test_temp_time(self):
        well = WellTemperature(temp_dict)
        md, tvd, deltaz, zstep = wellpath(5000)
        tdsi, ta, tr, tcsg, tsr, tfm, time = temp_time(5, well, tvd, deltaz, zstep)
        self.assertEqual(len(tdsi), len(ta), len(tr))
        self.assertEqual(len(tcsg), len(tsr), len(tfm))
        self.assertEqual(time, 5)
        self.assertIsInstance(tdsi, list)
        self.assertIsInstance(ta, list)
        self.assertIsInstance(tr, list)
        self.assertIsInstance(tcsg, list)
        self.assertIsInstance(tsr, list)
        self.assertIsInstance(tfm, list)
