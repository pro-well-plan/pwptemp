from unittest import TestCase
import pwptemp.drilling as ptd
import pwptemp.production as ptp
import pwptemp.injection as pti


class TestMain(TestCase):
    def test_temp_behavior(self):
        t = 2

        # For Drilling
        st = ptd.temp(t, log=True).behavior()
        self.assertEqual(len(st.tbot), len(st.tout))
        self.assertIsInstance(st.finaltime, type(t))
        self.assertIsInstance(st.tbot, list)
        self.assertIsInstance(st.tout, list)

        # For Production
        st = ptp.temp(t, log=True).behavior()
        self.assertIsInstance(st.finaltime, type(t))
        self.assertIsInstance(st.tout, list)

        # For Injection
        st = pti.temp(t, log=True).behavior()
        self.assertIsInstance(st.finaltime, type(t))
        self.assertIsInstance(st.tbot, list)
