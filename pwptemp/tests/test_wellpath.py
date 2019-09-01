from unittest import TestCase
from pwptemp.WellPath import wellpath

class TestWellPath(TestCase):
    def test_wellpath(self):
        md, tvd, deltaz, zstep = wellpath(5000)
        self.assertIsInstance(md, range)
        self.assertIsInstance(tvd, list)
        self.assertEqual(len(md), len(tvd))
        self.assertEqual(deltaz, 50)
        self.assertEqual(zstep, len(md))
