from unittest import TestCase
import pwptemp


class TestWellPath(TestCase):
    def test_load(self):
        D = pwptemp.wellpath.get(3000, 50)
        data = [D.md, D.tvd]
        newD = pwptemp.wellpath.load(data, deltaz=D.deltaz, mode=1)
        self.assertIsInstance(newD.md, list)
        self.assertIsInstance(newD.tvd, list)
        self.assertEqual(len(newD.md), len(newD.tvd))
        self.assertEqual(newD.deltaz, 50)
        self.assertEqual(newD.zstep, len(newD.md))
