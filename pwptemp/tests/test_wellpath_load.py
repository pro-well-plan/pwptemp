from unittest import TestCase
from pwptemp.wellpath import get, load


class TestWellPath(TestCase):
    def test_load(self):
        mdo, tvdo, deltazo, zstepo = get(5000)
        md, tvd, deltaz, zstep = load(mdo, tvdo, deltazo)
        self.assertIsInstance(md, range)
        self.assertIsInstance(tvd, list)
        self.assertEqual(len(md), len(tvd))
        self.assertEqual(deltaz, 50)
        self.assertEqual(zstep, len(md))
