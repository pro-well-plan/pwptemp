from unittest import TestCase
from pwptemp.WellPath import get


class TestWellPath(TestCase):
    def test_get(self):
        md, tvd, deltaz, zstep = get(5000)
        self.assertIsInstance(md, range)
        self.assertIsInstance(tvd, list)
        self.assertEqual(len(md), len(tvd))
        self.assertEqual(deltaz, 50)
        self.assertEqual(zstep, len(md))
