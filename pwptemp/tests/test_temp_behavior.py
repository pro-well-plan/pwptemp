from unittest import TestCase
from pwptemp import wellpath
from pwptemp.drilling import input, main


class TestMain(TestCase):
    def test_temp_behavior(self):
        tdata = input.data()
        depths = wellpath.get(100)
        well = input.set_well(tdata, depths)
        st = main.temp_time(2, well, log=True).behavior()

        self.assertEqual(st.finaltime, len(st.tbot), len(st.tout))
        self.assertIsInstance(st.finaltime, int)
        self.assertIsInstance(st.tbot, list)
        self.assertIsInstance(st.tout, list)