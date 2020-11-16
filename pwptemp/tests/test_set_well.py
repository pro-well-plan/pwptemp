from unittest import TestCase
import well_profile as wp

trajectory = wp.load('trajectory1.xlsx')


class TestSetWell(TestCase):
    def test_set_well_drilling(self):
        # with casings
        from pwptemp import well_system, inputs
        casings = [{'od': 9.5, 'id': 8.5, 'depth': 25.0}, {'od': 20.0, 'id': 18.0, 'depth': 10.0}]
        tdata = inputs.inputs_dict(casings)
        well = well_system.set_well(tdata, trajectory)
        self.assertEqual(len(well.casings[0]), len(well.casings[1]))
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            if value is None:
                value = 0
            if value is float:
                self.assertEqual(value - value, 0)

        # without casings
        tdata = inputs.inputs_dict()
        well = well_system.set_well(tdata, trajectory)
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            if value is None:
                value = 0
            if value is float:
                self.assertEqual(value - value, 0)

    def test_set_well_production(self):
        from pwptemp.production import input
        # with casings
        casings = [{'od': 9.5, 'id': 8.5, 'depth': 25.0}, {'od': 20.0, 'id': 18.0, 'depth': 10.0}]
        tdata = input.data(casings)
        well = input.set_well(tdata, trajectory)
        self.assertEqual(len(well.casings[0]), len(well.casings[1]))
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertEqual(value - value, 0)

        # without casings
        tdata = input.data()
        well = input.set_well(tdata, trajectory)
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertEqual(value - value, 0)

    def test_set_well_injection(self):
        from pwptemp.injection import input
        # with casings
        casings = [{'od': 9.5, 'id': 8.5, 'depth': 25.0}, {'od': 20.0, 'id': 18.0, 'depth': 10.0}]
        tdata = input.data(casings)
        well = input.set_well(tdata, trajectory)
        self.assertEqual(len(well.casings[0]), len(well.casings[1]))
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertEqual(value - value, 0)

        # without casings
        tdata = input.data()
        well = input.set_well(tdata, trajectory)
        self.assertEqual(len(well.md), well.zstep)
        del tdata['casings']
        for x, value in tdata.items():
            self.assertEqual(value - value, 0)
