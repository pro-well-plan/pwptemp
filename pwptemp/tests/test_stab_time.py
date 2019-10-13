from unittest import TestCase
import pwptemp


class TestMain(TestCase):
    def test_stab_time(self):
        tdata = pwptemp.input.tdict(50)
        depths = pwptemp.wellpath.get(3000, 50)
        well = pwptemp.input.set_well(tdata, depths)
        st = pwptemp.main.stab_time(well)
        self.assertEqual(st.finaltime, len(st.tbot), len(st.tout))
        self.assertIsInstance(st.finaltime, int)
        self.assertIsInstance(st.tbot, list)
        self.assertIsInstance(st.tout, list)