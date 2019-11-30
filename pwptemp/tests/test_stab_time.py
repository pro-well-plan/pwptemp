from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input, main


class TestMain(TestCase):
    def test_stab_time(self):
        tdata = input.data()
        depths = wellpath.get(3000, 50)
        well = input.set_well(tdata, depths)
        st = main.stab_time(well)
        self.assertEqual(st.finaltime, len(st.tbot), len(st.tout))
        self.assertIsInstance(st.finaltime, int)
        self.assertIsInstance(st.tbot, list)
        self.assertIsInstance(st.tout, list)