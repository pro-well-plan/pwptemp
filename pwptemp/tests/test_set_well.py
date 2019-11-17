from unittest import TestCase
import pwptemp


class TestSetWell(TestCase):
    def test_set_well(self):
        # with casings
        casings = [{'od': 0.24, 'id': 0.216, 'depth': 25}, {'od': 0.66, 'id': 0.63, 'depth': 10}]
        tdata = pwptemp.input.data(casings)
        depths = pwptemp.wellpath.get(100, 10)
        well = pwptemp.input.set_well(tdata, depths)
        self.assertEqual(len(well.casings[0]), len(well.casings[1]))
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertIsInstance(value, float)

        # without casings
        tdata = pwptemp.input.data()
        depths = pwptemp.wellpath.get(100, 10)
        well = pwptemp.input.set_well(tdata, depths)
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertIsInstance(value, float)

