from unittest import TestCase
import pwptemp


class TestWellPath(TestCase):
    def test_get(self):
        D = pwptemp.wellpath.get(3000, 50)  # for Vertical well
        self.assertIsInstance(D.md, list)
        self.assertIsInstance(D.tvd, list)
        self.assertEqual(len(D.md), len(D.tvd))
        self.assertEqual(D.deltaz, 50)
        self.assertEqual(D.zstep, len(D.md))
        D = pwptemp.wellpath.get(3000, 50, profile='J', kop=1000, eob=1800)  # for J-type well
        self.assertIsInstance(D.md, list)
        self.assertIsInstance(D.tvd, list)
        self.assertEqual(len(D.md), len(D.tvd))
        self.assertEqual(D.deltaz, 50)
        self.assertEqual(D.zstep, len(D.md))
        D = pwptemp.wellpath.get(3000, 50, profile='S', kop=1000, eob=1800, sod=2300, eod=2700)  # for S-type well
        self.assertIsInstance(D.md, list)
        self.assertIsInstance(D.tvd, list)
        self.assertEqual(len(D.md), len(D.tvd))
        self.assertEqual(D.deltaz, 50)
        self.assertEqual(D.zstep, len(D.md))
        D = pwptemp.wellpath.get(3000, 50, profile='H1', kop=1000, eob=1800)  # for H1-type well
        self.assertIsInstance(D.md, list)
        self.assertIsInstance(D.tvd, list)
        self.assertEqual(len(D.md), len(D.tvd))
        self.assertEqual(D.deltaz, 50)
        self.assertEqual(D.zstep, len(D.md))
        D = pwptemp.wellpath.get(3000, 50, profile='H1', kop=1000, eob=1800, kop2=2300, eob2=2700)  # for H2-type well
        self.assertIsInstance(D.md, list)
        self.assertIsInstance(D.tvd, list)
        self.assertEqual(len(D.md), len(D.tvd))
        self.assertEqual(D.deltaz, 50)
        self.assertEqual(D.zstep, len(D.md))
