from unittest import TestCase
from pwptemp import wellpath


class TestHC(TestCase):
    def test_heat_coef_drilling(self):
        from pwptemp.drilling import input, heatcoefficients, initcond
        depths = wellpath.get(100, 50)
        well = input.set_well(input.data(), depths)
        ic = initcond.init_cond(well)
        well = well.define_viscosity(ic)
        well = well.define_density(ic)
        hc = heatcoefficients.heat_coef(well, 1)
        self.assertEqual(len(hc), 9)
        self.assertEqual(len(hc[0]), 4)     # len of hc_1
        self.assertEqual(len(hc[0][0]), depths.zstep)   # len of c1z
        self.assertEqual(len(hc[0][1]), depths.zstep)   # len of c1e
        self.assertEqual(len(hc[0][2]), depths.zstep)   # len of c1
        self.assertEqual(len(hc[0][3]), depths.zstep)   # len of c1t
        self.assertEqual(len(hc[1]), 4)  # len of hc_2
        self.assertEqual(len(hc[1][0]), depths.zstep)  # len of c2z
        self.assertEqual(len(hc[1][1]), depths.zstep)  # len of c2e
        self.assertEqual(len(hc[1][2]), depths.zstep)  # len of c2w
        self.assertEqual(len(hc[1][3]), depths.zstep)  # len of c2t
        self.assertEqual(len(hc[2]), 5)  # len of hc_3
        self.assertEqual(len(hc[2][0]), depths.zstep)  # len of c3z
        self.assertEqual(len(hc[2][1]), depths.zstep)  # len of c3e
        self.assertEqual(len(hc[2][2]), depths.zstep)  # len of c3w
        self.assertEqual(len(hc[2][3]), depths.zstep)  # len of c3
        self.assertEqual(len(hc[2][4]), depths.zstep)  # len of c3t
        self.assertEqual(len(hc[3]), 4)  # len of hc_4
        self.assertEqual(len(hc[3][0]), depths.zstep)  # len of c4z
        self.assertEqual(len(hc[3][1]), depths.zstep)  # len of c4e
        self.assertEqual(len(hc[3][2]), depths.zstep)  # len of c4w
        self.assertEqual(len(hc[3][3]), depths.zstep)  # len of c4t
        self.assertEqual(len(hc[4]), 4)  # len of hc_5
        self.assertEqual(len(hc[4][0]), depths.zstep)  # len of c5z
        self.assertEqual(len(hc[4][1]), depths.zstep)  # len of c5e
        self.assertEqual(len(hc[4][2]), depths.zstep)  # len of c5w
        self.assertEqual(len(hc[4][3]), depths.zstep)  # len of c5t

    def test_heat_coef_production(self):
        from pwptemp.production import input, heatcoefficients, initcond
        depths = wellpath.get(100, 50)
        well = input.set_well(input.data(), depths)
        ic = initcond.init_cond(well)
        well = well.define_viscosity(ic)
        well = well.define_density(ic)
        tt = ic.tto
        t3 = ic.tco
        hc = heatcoefficients.heat_coef(well, 1, tt, t3)
        self.assertEqual(len(hc), 8)
        self.assertEqual(len(hc[0]), 4)     # len of hc_1
        self.assertEqual(len(hc[0][0]), depths.zstep)   # len of c1z
        self.assertEqual(len(hc[0][1]), depths.zstep)   # len of c1e
        self.assertEqual(len(hc[0][2]), depths.zstep)   # len of c1
        self.assertEqual(len(hc[0][3]), depths.zstep)   # len of c1t
        self.assertEqual(len(hc[1]), 4)  # len of hc_2
        self.assertEqual(len(hc[1][0]), depths.zstep)  # len of c2z
        self.assertEqual(len(hc[1][1]), depths.zstep)  # len of c2e
        self.assertEqual(len(hc[1][2]), depths.zstep)  # len of c2w
        self.assertEqual(len(hc[1][3]), depths.zstep)  # len of c2t
        self.assertEqual(len(hc[2]), 4)  # len of hc_3
        self.assertEqual(len(hc[2][0]), depths.zstep)  # len of c3z
        self.assertEqual(len(hc[2][1]), depths.zstep)  # len of c3e
        self.assertEqual(len(hc[2][2]), depths.zstep)  # len of c3w
        self.assertEqual(len(hc[2][3]), depths.zstep)  # len of c3t
        self.assertEqual(len(hc[3]), 4)  # len of hc_4
        self.assertEqual(len(hc[3][0]), depths.zstep)  # len of c4z
        self.assertEqual(len(hc[3][1]), depths.zstep)  # len of c4e
        self.assertEqual(len(hc[3][2]), depths.zstep)  # len of c4w
        self.assertEqual(len(hc[3][3]), depths.zstep)  # len of c4t
        self.assertEqual(len(hc[4]), 4)  # len of hc_5
        self.assertEqual(len(hc[4][0]), depths.zstep)  # len of c5z
        self.assertEqual(len(hc[4][1]), depths.zstep)  # len of c5e
        self.assertEqual(len(hc[4][2]), depths.zstep)  # len of c5w
        self.assertEqual(len(hc[4][3]), depths.zstep)  # len of c5t

    def test_heat_coef_injection(self):
        from pwptemp.injection import input, heatcoefficients, initcond
        depths = wellpath.get(100, 50)
        well = input.set_well(input.data(), depths)
        ic = initcond.init_cond(well)
        well = well.define_density(ic)
        tt = ic.tto
        t3 = ic.tco
        hc = heatcoefficients.heat_coef(well, 1, tt, t3)
        self.assertEqual(len(hc), 8)
        self.assertEqual(len(hc[0]), 4)     # len of hc_1
        self.assertEqual(len(hc[0][0]), depths.zstep)   # len of c1z
        self.assertEqual(len(hc[0][1]), depths.zstep)   # len of c1e
        self.assertEqual(len(hc[0][2]), depths.zstep)   # len of c1
        self.assertEqual(len(hc[0][3]), depths.zstep)   # len of c1t
        self.assertEqual(len(hc[1]), 4)  # len of hc_2
        self.assertEqual(len(hc[1][0]), depths.zstep)  # len of c2z
        self.assertEqual(len(hc[1][1]), depths.zstep)  # len of c2e
        self.assertEqual(len(hc[1][2]), depths.zstep)  # len of c2w
        self.assertEqual(len(hc[1][3]), depths.zstep)  # len of c2t
        self.assertEqual(len(hc[2]), 4)  # len of hc_3
        self.assertEqual(len(hc[2][0]), depths.zstep)  # len of c3z
        self.assertEqual(len(hc[2][1]), depths.zstep)  # len of c3e
        self.assertEqual(len(hc[2][2]), depths.zstep)  # len of c3w
        self.assertEqual(len(hc[2][3]), depths.zstep)  # len of c3t
        self.assertEqual(len(hc[3]), 4)  # len of hc_4
        self.assertEqual(len(hc[3][0]), depths.zstep)  # len of c4z
        self.assertEqual(len(hc[3][1]), depths.zstep)  # len of c4e
        self.assertEqual(len(hc[3][2]), depths.zstep)  # len of c4w
        self.assertEqual(len(hc[3][3]), depths.zstep)  # len of c4t
        self.assertEqual(len(hc[4]), 4)  # len of hc_5
        self.assertEqual(len(hc[4][0]), depths.zstep)  # len of c5z
        self.assertEqual(len(hc[4][1]), depths.zstep)  # len of c5e
        self.assertEqual(len(hc[4][2]), depths.zstep)  # len of c5w
        self.assertEqual(len(hc[4][3]), depths.zstep)  # len of c5t
