from unittest import TestCase
import pwptemp


class TestWellPath(TestCase):
    def test_get(self):
        D = pwptemp.wellpath.get(3000, 50)
        self.assertIsInstance(D.md, list)
        self.assertIsInstance(D.tvd, list)
        self.assertEqual(len(D.md), len(D.tvd))
        self.assertEqual(D.deltaz, 50)
        self.assertEqual(D.zstep, len(D.md))
