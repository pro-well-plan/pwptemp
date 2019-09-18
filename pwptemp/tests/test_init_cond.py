from unittest import TestCase
from pwptemp.initcond import init_cond
from pwptemp.wellpath import wellpath


class TestInitCond(TestCase):
    def test_init_cond(self):
        md, tvd, deltaz, zstep = wellpath(5000)
        a,b,c,d,e,f = init_cond(15, 2,-0.005,0.0238,100,tvd,50)
        self.assertIsInstance(a,list)
        self.assertIsInstance(b, list)
        self.assertIsInstance(c, list)
        self.assertIsInstance(d, list)
        self.assertIsInstance(e, list)
        self.assertIsInstance(f, list)


