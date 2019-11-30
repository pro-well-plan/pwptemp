from unittest import TestCase
from pwptemp import wellpath


class TestWellPath(TestCase):
    def test_load(self):
        D = wellpath.get(3000, 50)
        data = [D.md, D.tvd]
        newD = wellpath.load(data, deltaz=D.deltaz)
        self.assertIsInstance(newD.md, list)
        self.assertIsInstance(newD.tvd, list)
        self.assertEqual(len(newD.md), len(newD.tvd))
        self.assertEqual(newD.deltaz, 50)
        self.assertEqual(newD.zstep, len(newD.md))
