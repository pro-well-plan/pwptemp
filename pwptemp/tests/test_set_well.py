from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input


class TestSetWell(TestCase):
    def test_set_well(self):
        # with casings
        casings = [{'od': 9.5, 'id': 8.5, 'depth': 25.0}, {'od': 20.0, 'id': 18.0, 'depth': 10.0}]
        tdata = input.data(casings)
        depths = wellpath.get(100, 10)
        well = input.set_well(tdata, depths)
        self.assertEqual(len(well.casings[0]), len(well.casings[1]))
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertEqual(value/value, 1)

        # without casings
        tdata = input.data()
        depths = wellpath.get(100, 10)
        well = input.set_well(tdata, depths)
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertEqual(value/value, 1)

