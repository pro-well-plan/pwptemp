from unittest import TestCase
from pwptemp import wellpath


class TestInitCond(TestCase):
    def test_init_cond_drilling(self):
        from pwptemp.drilling import input, initcond
        tdata = input.data()
        depths = wellpath.get(100, 10)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
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

    def test_init_cond_production(self):
        from pwptemp.production import input, initcond
        tdata = input.data()
        depths = wellpath.get(100, 10)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
        a = ic.tfto
        b = ic.tto
        c = ic.tao
        d = ic.tco
        e = ic.tsro
        f = ic.tfm
        self.assertIsInstance(a, list)
        self.assertIsInstance(b, list)
        self.assertIsInstance(c, list)
        self.assertIsInstance(d, list)
        self.assertIsInstance(e, list)
        self.assertIsInstance(f, list)

    def test_init_cond_injection(self):
        from pwptemp.injection import input, initcond
        tdata = input.data()
        depths = wellpath.get(100, 10)
        well = input.set_well(tdata, depths)
        ic = initcond.init_cond(well)
        a = ic.tfto
        b = ic.tto
        c = ic.tao
        d = ic.tco
        e = ic.tsro
        f = ic.tfm
        self.assertIsInstance(a, list)
        self.assertIsInstance(b, list)
        self.assertIsInstance(c, list)
        self.assertIsInstance(d, list)
        self.assertIsInstance(e, list)
        self.assertIsInstance(f, list)


