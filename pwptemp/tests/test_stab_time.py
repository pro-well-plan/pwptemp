from unittest import TestCase
from pwptemp.input import WellTemperature, temp_dict
from pwptemp.wellpath import wellpath
from pwptemp.main import stab_time


class TestLinearSystem(TestCase):
    def test_stab_time(self):
        well = WellTemperature(temp_dict)
        md, tvd, deltaz, zstep = wellpath(5000)
        finaltime, Tbot, Tout = stab_time(well, tvd, deltaz, zstep)
        self.assertEqual(finaltime, len(Tbot), len(Tout))
        self.assertIsInstance(finaltime, int)
        self.assertIsInstance(Tbot, list)
        self.assertIsInstance(Tout, list)