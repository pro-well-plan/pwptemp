from unittest import TestCase
import well_profile as wp

trajectory = wp.load('trajectory1.xlsx')


class TestHC(TestCase):
    def test_heat_coef_drilling(self):
        from pwptemp import well_system, inputs, heat_coefficients
        well = well_system.set_well(inputs.inputs_dict(), trajectory)
        well.op = 'drilling'
        bit_pos = 1
        heat_coefficients.add_heat_coefficients(well, 600, bit_pos)
        hc = well.sections
        self.assertTrue('comp_N/S' and 'comp_E' and 'comp_HeatSource' and 'comp_time' in hc[0][0])  # Inside Pipe
        self.assertTrue('comp_N/S' and 'comp_E' and 'comp_W' and 'comp_time' in hc[1][0])  # Pipe Wall
        self.assertTrue('comp_N/S' and 'comp_E' and 'comp_W' and 'comp_time' and 'comp_HeatSource' in hc[2][0])
        # Annulus
        self.assertTrue('comp_N/S' and 'comp_E' and 'comp_W' and 'comp_time' in hc[3][0])  # First Casing
        self.assertTrue('comp_N/S' and 'comp_E' and 'comp_W' and 'comp_time' in hc[4][0])  # Surrounding space

    def test_heat_coef_production(self):
        from pwptemp.production import input, heatcoefficients, initcond
        well = input.set_well(input.data(), trajectory)
        ic = initcond.init_cond(well)
        well = well.define_viscosity(ic)
        well = well.define_density(ic)
        tt = ic.tto
        t3 = ic.tco
        hc = heatcoefficients.heat_coef(well, 1, tt, t3)
        self.assertEqual(len(hc), 8)
        self.assertEqual(len(hc[0]), 4)     # len of hc_1
        self.assertEqual(len(hc[0][0]), trajectory.cells_no)   # len of c1z
        self.assertEqual(len(hc[0][1]), trajectory.cells_no)   # len of c1e
        self.assertEqual(len(hc[0][2]), trajectory.cells_no)   # len of c1
        self.assertEqual(len(hc[0][3]), trajectory.cells_no)   # len of c1t
        self.assertEqual(len(hc[1]), 4)  # len of hc_2
        self.assertEqual(len(hc[1][0]), trajectory.cells_no)  # len of c2z
        self.assertEqual(len(hc[1][1]), trajectory.cells_no)  # len of c2e
        self.assertEqual(len(hc[1][2]), trajectory.cells_no)  # len of c2w
        self.assertEqual(len(hc[1][3]), trajectory.cells_no)  # len of c2t
        self.assertEqual(len(hc[2]), 4)  # len of hc_3
        self.assertEqual(len(hc[2][0]), trajectory.cells_no)  # len of c3z
        self.assertEqual(len(hc[2][1]), trajectory.cells_no)  # len of c3e
        self.assertEqual(len(hc[2][2]), trajectory.cells_no)  # len of c3w
        self.assertEqual(len(hc[2][3]), trajectory.cells_no)  # len of c3t
        self.assertEqual(len(hc[3]), 4)  # len of hc_4
        self.assertEqual(len(hc[3][0]), trajectory.cells_no)  # len of c4z
        self.assertEqual(len(hc[3][1]), trajectory.cells_no)  # len of c4e
        self.assertEqual(len(hc[3][2]), trajectory.cells_no)  # len of c4w
        self.assertEqual(len(hc[3][3]), trajectory.cells_no)  # len of c4t
        self.assertEqual(len(hc[4]), 4)  # len of hc_5
        self.assertEqual(len(hc[4][0]), trajectory.cells_no)  # len of c5z
        self.assertEqual(len(hc[4][1]), trajectory.cells_no)  # len of c5e
        self.assertEqual(len(hc[4][2]), trajectory.cells_no)  # len of c5w
        self.assertEqual(len(hc[4][3]), trajectory.cells_no)  # len of c5t

    def test_heat_coef_injection(self):
        from pwptemp.injection import input, heatcoefficients, initcond
        well = input.set_well(input.data(), trajectory)
        ic = initcond.init_cond(well)
        well = well.define_viscosity(ic)
        well = well.define_density(ic)
        tt = ic.tto
        t3 = ic.tco
        hc = heatcoefficients.heat_coef(well, 1, tt, t3)
        self.assertEqual(len(hc), 8)
        self.assertEqual(len(hc[0]), 4)     # len of hc_1
        self.assertEqual(len(hc[0][0]), trajectory.cells_no)   # len of c1z
        self.assertEqual(len(hc[0][1]), trajectory.cells_no)   # len of c1e
        self.assertEqual(len(hc[0][2]), trajectory.cells_no)   # len of c1
        self.assertEqual(len(hc[0][3]), trajectory.cells_no)   # len of c1t
        self.assertEqual(len(hc[1]), 4)  # len of hc_2
        self.assertEqual(len(hc[1][0]), trajectory.cells_no)  # len of c2z
        self.assertEqual(len(hc[1][1]), trajectory.cells_no)  # len of c2e
        self.assertEqual(len(hc[1][2]), trajectory.cells_no)  # len of c2w
        self.assertEqual(len(hc[1][3]), trajectory.cells_no)  # len of c2t
        self.assertEqual(len(hc[2]), 4)  # len of hc_3
        self.assertEqual(len(hc[2][0]), trajectory.cells_no)  # len of c3z
        self.assertEqual(len(hc[2][1]), trajectory.cells_no)  # len of c3e
        self.assertEqual(len(hc[2][2]), trajectory.cells_no)  # len of c3w
        self.assertEqual(len(hc[2][3]), trajectory.cells_no)  # len of c3t
        self.assertEqual(len(hc[3]), 4)  # len of hc_4
        self.assertEqual(len(hc[3][0]), trajectory.cells_no)  # len of c4z
        self.assertEqual(len(hc[3][1]), trajectory.cells_no)  # len of c4e
        self.assertEqual(len(hc[3][2]), trajectory.cells_no)  # len of c4w
        self.assertEqual(len(hc[3][3]), trajectory.cells_no)  # len of c4t
        self.assertEqual(len(hc[4]), 4)  # len of hc_5
        self.assertEqual(len(hc[4][0]), trajectory.cells_no)  # len of c5z
        self.assertEqual(len(hc[4][1]), trajectory.cells_no)  # len of c5e
        self.assertEqual(len(hc[4][2]), trajectory.cells_no)  # len of c5w
        self.assertEqual(len(hc[4][3]), trajectory.cells_no)  # len of c5t
