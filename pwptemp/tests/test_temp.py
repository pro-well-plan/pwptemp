from unittest import TestCase
import pwptemp as pt
import pwptemp.production as ptp
import pwptemp.injection as pti
import well_profile as wp

trajectory = wp.load('trajectory1.xlsx')


class TestHC(TestCase):
    def test_temp_drilling(self):
        t = pt.calc_temp(trajectory)
        tdsi = t.temperatures['in_pipe']
        tds = t.temperatures['pipe']
        ta = t.temperatures['annulus']
        tcsg = t.temperatures['casing']
        tr = t.temperatures['riser']
        tsr = t.temperatures['sr']
        tfm = t.temperatures['formation']
        self.assertIsInstance(tdsi, list)
        self.assertIsInstance(tds, list)
        self.assertIsInstance(ta, list)
        self.assertIsInstance(tcsg, list)
        self.assertIsInstance(tr, list)
        self.assertIsInstance(tsr, list)
        self.assertIsInstance(tfm, list)

    def test_temp_production(self):
        t = ptp.temp(trajectory, 2)
        self.assertIsInstance(t.tft, list)
        self.assertIsInstance(t.tt, list)
        self.assertIsInstance(t.ta, list)
        self.assertIsInstance(t.tc, list)
        self.assertIsInstance(t.tsr, list)
        self.assertIsInstance(t.tfm, list)

    def test_temp_injection(self):
        t = pti.temp(trajectory, 2)
        self.assertIsInstance(t.tft, list)
        self.assertIsInstance(t.tt, list)
        self.assertIsInstance(t.ta, list)
        self.assertIsInstance(t.tc, list)
        self.assertIsInstance(t.tsr, list)
        self.assertIsInstance(t.tfm, list)
