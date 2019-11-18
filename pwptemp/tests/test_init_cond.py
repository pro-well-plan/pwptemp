from unittest import TestCase
import pwptemp


class TestInitCond(TestCase):
    def test_init_cond(self):
        tdata = pwptemp.drill_op.input.data()
        depths = pwptemp.wellpath.get(100, 10)
        well = pwptemp.drill_op.input.set_well(tdata, depths)
        ic = pwptemp.drill_op.initcond.init_cond(well)
        a = ic.tdsio
        b = ic.tdso
        c = ic.tao
        d = ic.tcsgo
        e = ic.tsro
        f = ic.tfm
        self.assertIsInstance(a, list)
        self.assertIsInstance(b, list)
        self.assertIsInstance(c, list)
        self.assertIsInstance(d, list)
        self.assertIsInstance(e, list)
        self.assertIsInstance(f, list)


