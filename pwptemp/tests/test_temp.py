from unittest import TestCase
import pwptemp.drilling as ptd
import pwptemp.production as ptp
import pwptemp.injection as pti


class TestHC(TestCase):
    def test_temp_drilling(self):
        t = ptd.temp(1)
        self.assertIsInstance(t.tdsi, list)
        self.assertIsInstance(t.tds, list)
        self.assertIsInstance(t.ta, list)
        self.assertIsInstance(t.tcsg, list)
        self.assertIsInstance(t.tsr, list)
        self.assertIsInstance(t.tfm, list)

    def test_temp_production(self):
        t = ptp.temp(1)
        self.assertIsInstance(t.tft, list)
        self.assertIsInstance(t.tt, list)
        self.assertIsInstance(t.ta, list)
        self.assertIsInstance(t.tc, list)
        self.assertIsInstance(t.tsr, list)
        self.assertIsInstance(t.tfm, list)

    def test_temp_injection(self):
        t = pti.temp(1)
        self.assertIsInstance(t.tft, list)
        self.assertIsInstance(t.tt, list)
        self.assertIsInstance(t.ta, list)
        self.assertIsInstance(t.tc, list)
        self.assertIsInstance(t.tsr, list)
        self.assertIsInstance(t.tfm, list)
