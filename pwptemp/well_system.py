import torque_drag as td
import numpy as np
from math import pi, log
from copy import deepcopy


def create_depth_cells(trajectory):
    md_new = list(np.linspace(0, max(trajectory.md), num=100))
    tvd_new, inclination, azimuth = [], [], []
    for i in md_new:
        tvd_new.append(np.interp(i, trajectory.md, trajectory.tvd))
        inclination.append(np.interp(i, trajectory.md, trajectory.inclination))
        azimuth.append(np.interp(i, trajectory.md, trajectory.azimuth))
    depth_step = md_new[1]

    return md_new, tvd_new, depth_step, inclination, azimuth


def set_well(temp_dict, trajectory):
    q_conv = 60  # from m^3/min to m^3/h
    an_conv = 1 / 1500  # from in^2 to m^2
    diameter_conv = 0.0254  # from in to m

    class NewWell(object):
        def __init__(self):

            # DIMENSIONS
            self.trajectory = trajectory
            self.md, self.tvd, self.depth_step, self.inclination, self.azimuth = create_depth_cells(trajectory)
            self.deltaz = self.depth_step
            self.cells_no = self.zstep = len(self.md)
            self.casings = temp_dict["casings"]  # casings array
            self.pipe_id = temp_dict["pipe_id"] * diameter_conv  # Drill String Inner  Diameter, m
            self.pipe_od = temp_dict["pipe_od"] * diameter_conv  # Drill String Outer Diameter, m
            # OFFSHORE
            self.water_depth = temp_dict["water_depth"]  # Water Depth, m
            self.riser_cells = round(self.water_depth / self.depth_step)  # number of grid cells for the riser
            self.riser_id = temp_dict["riser_id"] * diameter_conv  # Riser diameter Inner Diameter, m
            self.riser_od = temp_dict["riser_od"] * diameter_conv  # Riser diameter Outer Diameter, m
            self.th_grad_seawater = temp_dict["th_grad_seawater"]  # Seawater thermal grad., °C/cell
            # RADIUS (CALCULATED)
            self.r1 = self.pipe_id / 2  # Drill String Inner  Radius, m
            self.r2 = self.pipe_od / 2  # Drill String Outer Radius, m
            self.annular_or = self.casings[0, 1] / 2  # Casing Inner Radius, m
            self.riser_ir = self.riser_id / 2  # Riser Inner Radius, m
            self.riser_or = self.riser_od / 2  # Riser Outer Radius, m
            # Surrounding Space Outer Diameter, m
            self.sr_od = sorted([self.riser_od + 0.03, self.casings[-1, 0] + 0.03])[-1]
            self.fm_diam = temp_dict["fm_diam"] * diameter_conv  # Undisturbed Formation Diameter, m
            self.sr_diam = self.casings[0, 0]  # Surrounding Space Inner Diameter, m
            self.sr_ir = self.sr_diam / 2  # Surrounding Space Inner Radius m
            self.sr_or = self.sr_od / 2  # Surrounding Space Outer Radius, m
            self.sr_thickness = self.sr_or - self.sr_ir  # Surrounding thickness, m
            self.sr_fractions = get_fractions(self)
            self.fm_rad = self.fm_diam * diameter_conv / 2  # Undisturbed Formation Radius, m

            # OPERATIONAL
            self.temp_surface = temp_dict["temp_surface"]  # Surface Temperature (RKB), °C
            if temp_dict["temp_inlet"] is None:
                self.temp_inlet = self.temp_surface
            else:
                self.temp_inlet = temp_dict["temp_inlet"]  # Inlet Fluid temperature, °C
            self.th_grad_fm = temp_dict["th_grad_fm"]  # Geothermal gradient, from °C/m to °C/cell
            self.q = temp_dict["flowrate"] * q_conv  # Flow rate, m^3/h
            # Fluid velocity through the annular
            self.va = (self.q / (pi * ((self.annular_or ** 2) - (self.r2 ** 2)))) / 3600
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600  # Fluid velocity through the drill pipe
            self.rpm = temp_dict["rpm"]  # Revolutions per minute
            self.tbit = temp_dict["tbit"]  # Torque on the bit, kN*m
            self.wob = temp_dict["wob"]  # Weight on bit, kN
            self.rop_list = temp_dict["rop"]
            self.rop = temp_dict["rop"][0]  # Rate of Penetration, m/h
            self.an = temp_dict["an"] * an_conv  # Area of the nozzles, m^2
            self.bit_n = temp_dict["bit_n"]  # drill bit efficiency
            self.dp_e = temp_dict["dp_e"]  # drill pipe eccentricity
            self.thao_o = temp_dict["thao_o"]
            self.k = temp_dict["k"]
            self.n = temp_dict["n"]
            self.visc = temp_dict['visc']

            # DENSITIES
            self.rho_fluid = temp_dict["rho_fluid"]  # Fluid
            self.rho_pipe = temp_dict["rho_pipe"]  # Drill Pipe
            self.rho_csg = temp_dict["rho_csg"]  # Casing
            self.rho_riser = temp_dict["rho_riser"]  # Riser
            self.rho_cem = temp_dict["rho_cem"]  # Cement Sheath
            self.rho_fm = temp_dict["rho_fm"]  # Formation
            self.rho_seawater = temp_dict["rho_seawater"]  # Seawater

            # Thermal conductivity  W/(m*°C)
            self.tc_fluid = temp_dict["tc_fluid"]  # Fluid
            self.tc_csg = temp_dict["tc_csg"]  # Casing
            self.tc_cem = temp_dict["tc_cem"]  # Cement
            self.tc_pipe = temp_dict["tc_pipe"]  # Drill Pipe
            self.tc_fm = temp_dict["tc_fm"]  # Formation
            self.tc_riser = temp_dict["tc_riser"]  # Riser
            self.tc_seawater = temp_dict["tc_seawater"]  # Seawater

            self.beta = temp_dict["beta"]  # isothermal bulk modulus, Pa
            self.alpha = temp_dict['alpha']  # Fluid Thermal Expansion Coefficient, 1/°C

            # Specific heat capacity, J/(kg*°C)
            self.shc_fluid = temp_dict["shc_fluid"]  # Fluid
            self.shc_csg = temp_dict["shc_csg"]  # Casing
            self.shc_cem = temp_dict["shc_cem"]  # Cement
            self.shc_pipe = temp_dict["shc_pipe"]  # Drill Pipe
            self.shc_riser = temp_dict["shc_riser"]  # Riser
            self.shc_seawater = temp_dict["shc_seawater"]  # Seawater
            self.shc_fm = temp_dict["shc_fm"]  # Formation

            self.sections = create_system(self)

            self.sections, self.temp_fm = calc_formation_temp(self)

            td_obj = td.calc(self,
                             dimensions={'od_pipe': self.pipe_od, 'id_pipe': self.pipe_id, 'length_pipe': self.md[-1],
                                         'od_annular': self.annular_or * 2},
                             case='static',
                             densities={'rhof': self.rho_fluid, 'rhod': self.rho_pipe},
                             fric=0.24, wob=self.wob, tbit=self.tbit, torque_calc=True)

            self.drag = td_obj.force['static']  # drag forces, kN
            self.torque = td_obj.torque['static']  # torque, kN*m

            self.sections, self.h1, self.h2, self.h3, self.h3r = extra_calcs(self)
            self.temperatures = None

            if len(self.casings) != len(self.rop_list) - 1 and self.casings[0, 2] != 0:
                raise ValueError('ROP must be set for all the sections.')

    return NewWell()


def create_system(well):
    section_0, section_1, section_2, section_3, section_4 = [], [], [], [], []
    for x in range(well.cells_no):
        initial_dict = {'component': '', 'material': '', 'rho': 2.24, 'tc': '', 'shc': '',
                        'depth': well.md[x]}
        section_0.append(deepcopy(initial_dict))
        section_1.append(deepcopy(initial_dict))
        section_2.append(deepcopy(initial_dict))
        section_3.append(deepcopy(initial_dict))
        section_4.append(deepcopy(initial_dict))
    sections = [section_0, section_1, section_2, section_3, section_4]
    sections_names = ['section_0', 'section_1', 'section_2', 'section_3', 'section_4']

    for x, i in zip(sections, sections_names):
        for y in range(well.cells_no):
            x[y]['material'] = get_material(i, well.md[y],
                                            first_casing_depth=well.casings[0, 2],
                                            water_depth=well.water_depth)
            if x[y]['material'] == 'mixture':
                pipe_fraction, cement_fraction = get_fractions_at_depth(well, y)
                x[y]['rho'] = get_mixture_density(pipe_fraction, cement_fraction, well) * 1000
                x[y]['tc'] = get_mixture_thermal_conductivity(pipe_fraction, cement_fraction, well)
                x[y]['shc'] = get_mixture_heat_capacity(pipe_fraction, cement_fraction, well)

            else:
                x[y]['rho'] = get_density(x[y]['material'], well) * 1000
                x[y]['tc'] = get_thermal_conductivity(x[y]['material'], well)
                x[y]['shc'] = get_heat_capacity(x[y]['material'], well)
                if x[y]['material'] == 'fluid':
                    x[y]['visc'] = get_viscosity(well)

    return sections


def get_fractions_at_depth(well, cell):
    the_index = -1
    casing_depths = reversed([x[2] for x in well.casings])
    for x in casing_depths:
        if well.md[cell] > x:
            the_index -= 1

    pipe_fraction = well.sr_fractions[the_index][0]
    cement_fraction = well.sr_fractions[the_index][1]

    return pipe_fraction, cement_fraction


def get_density(material, well):
    rho = {'formation': well.rho_fm,
           'fluid': well.rho_fluid,
           'pipe': well.rho_fm,
           'casing': well.rho_csg,
           'riser': well.rho_riser,
           'seawater': well.rho_seawater,
           'cement': well.rho_cem}

    return rho[material]


def get_mixture_density(pipe_fraction, cement_fraction, well):
    formation_fraction = 1 - pipe_fraction - cement_fraction
    rho = pipe_fraction * get_density('casing', well) + \
        cement_fraction * get_density('cement', well) + \
        formation_fraction * get_density('formation', well)

    return rho


def get_viscosity(well):
    rho = {'fluid': well.visc}

    return rho['fluid']


def get_thermal_conductivity(material, well):
    tc = {'formation': well.tc_fm,
          'fluid': well.tc_fluid,
          'pipe': well.tc_fm,
          'casing': well.tc_csg,
          'riser': well.tc_riser,
          'seawater': well.tc_seawater,
          'cement': well.tc_cem}

    return tc[material]


def get_mixture_thermal_conductivity(pipe_fraction, cement_fraction, well):
    formation_fraction = 1 - pipe_fraction - cement_fraction
    rho = pipe_fraction * get_thermal_conductivity('casing', well) + \
        cement_fraction * get_thermal_conductivity('cement', well) + \
        formation_fraction * get_thermal_conductivity('formation', well)

    return rho


def get_heat_capacity(material, well):
    shc = {'formation': well.shc_fm,
           'fluid': well.shc_fluid,
           'pipe': well.shc_fm,
           'casing': well.shc_csg,
           'riser': well.shc_riser,
           'seawater': well.shc_seawater,
           'cement': well.shc_cem}

    return shc[material]


def get_mixture_heat_capacity(pipe_fraction, cement_fraction, well):
    formation_fraction = 1 - pipe_fraction - cement_fraction
    rho = pipe_fraction * get_heat_capacity('casing', well) + \
        cement_fraction * get_heat_capacity('cement', well) + \
        formation_fraction * get_heat_capacity('formation', well)

    return rho


def get_fractions(well):
    fractions = []
    for x in range(len(well.casings) - 1):
        pipe_thickness = (well.casings[x, 0] - well.casings[x, 1]) / 2
        pipe_fraction = pipe_thickness / well.sr_thickness
        cement_thickness = (well.casings[x + 1, 1] - well.casings[x, 0]) / 2
        cement_fraction = cement_thickness / well.sr_thickness
        fractions.append([pipe_fraction, cement_fraction])

    last_pipe_fraction = ((well.casings[-1, 0] - well.casings[-1, 1]) / 2) / well.sr_thickness
    last_cement_fraction = ((well.sr_or - well.casings[-1, 0]) / 2) / well.sr_thickness

    fractions.append([last_pipe_fraction, last_cement_fraction])

    fractions[0][0] = 0

    cement = 0  # cement layer fraction for the first casing (the deepest)
    pipe = 0
    fractions_per_section = [[pipe, cement]]
    for x in fractions:
        cement += x[1]
        pipe += x[0]
        fractions_per_section.append([pipe, cement])

    return fractions_per_section


def get_material(section, md, operation='drilling', first_casing_depth=None, water_depth=0):
    if first_casing_depth is None:
        first_casing_depth = -1

    if md <= first_casing_depth:
        if md >= water_depth:
            section_3 = 'casing'
        else:
            section_3 = 'riser'
    else:
        section_3 = 'formation'

    if md >= water_depth:
        section_4 = 'mixture'
        if first_casing_depth != -1:
            section_4 = 'mixture'
    else:
        section_4 = 'seawater'

    if operation == 'drilling':
        component = {'section_0': 'fluid',
                     'section_1': 'pipe',
                     'section_2': 'fluid',
                     'section_3': section_3,
                     'section_4': section_4}
    else:
        component = None
    return component[section]


def extra_calcs(well):
    h1, h2, h3, h3r = [], [], [], []
    sections = well.sections.copy()
    for x, y in zip(sections[0], sections[2]):
        # Reynolds number
        x['re'] = calc_re(well, x['rho'], x['visc'], section=0)  # Section 0
        y['re'] = calc_re(well, y['rho'], y['visc'], section=2)  # Section 2 - Annulus
        # Prandtl number
        x['pr'] = calc_pr(x['shc'], x['tc'], x['visc'])  # Section 0
        y['pr'] = calc_pr(y['shc'], y['tc'], y['visc'])  # Section 2 - Annulus
        # Friction factor
        x['f'] = calc_friction_factor(x['re'])  # Section 0
        y['f'] = calc_friction_factor(y['re'])  # Section 2 - Annulus
        # Nusselt number
        nu_int = calc_nu(well, x['f'], x['re'], x['pr'], section=1)  # Section 1
        nu_ext = calc_nu(well, y['f'], y['re'], y['pr'], section=1)  # Section 1
        nu_ann = calc_nu(well, y['f'], y['re'], y['pr'], section=2)  # Section 2 - Annulus
        # Heat transfer coefficients
        h1.append(calc_heat_transfer_coef(x['tc'], nu_int, well.pipe_id))
        h2.append(calc_heat_transfer_coef(x['tc'], nu_ext, well.pipe_od))
        h3.append(calc_heat_transfer_coef(x['tc'], nu_ann, well.annular_or * 2))
        h3r.append(calc_heat_transfer_coef(x['tc'], nu_ann, well.riser_ir * 2))

    return sections, h1, h2, h3, h3r


def calc_re(well, rho_fluid, viscosity, section=0):
    if section == 0:
        # Reynolds number inside pipe
        re = rho_fluid * well.vp * 2 * well.r1 / viscosity
    else:
        # Reynolds number - annular
        re = rho_fluid * well.va * 2 * (well.annular_or - well.r2) / viscosity

    return re


def calc_pr(shc_fluid, tc_fluid, viscosity):
    pr = viscosity * shc_fluid / tc_fluid

    return pr


def calc_friction_factor(re):
    f = 64 / re

    if 2300 < re < 10000:
        f = 1.63 / log(6.9 / re) ** 2

    if re >= 10000:
        f = 1.63 / log(6.9 / re) ** 2

    return f


def calc_nu(well, f, re, pr, section=1):
    nu = 4.36
    if section != 1 and re < 2300:
        nu = 1.86 * ((re * pr) ** (1 / 3)) * \
             ((2 * (well.annular_or - well.r2) / well.md[-1]) ** (1 / 3)) \
             * (1 ** 0.14)

    if 2300 < re < 10000:
        nu = (f / 8) * (re - 1000) * pr / (1 + (12.7 * (f / 8) ** 0.5) * (pr ** (2 / 3) - 1))

    if re >= 10000:
        nu = 0.027 * (re ** (4 / 5)) * (pr ** (1 / 3)) * (1 ** 0.14)

    return nu


def calc_heat_transfer_coef(tc, nu, diameter):
    h = tc * nu / diameter

    return h


def calc_formation_temp(well):
    temp_fm = [well.temp_surface]
    for j in range(1, well.cells_no):

        if j <= well.riser_cells:
            th_grad = well.th_grad_seawater  # Water Thermal Gradient for the Riser section
        else:
            th_grad = well.th_grad_fm  # Geothermal Gradient below the Riser section
        temp_delta = temp_fm[j - 1] + th_grad * (well.tvd[j] - well.tvd[j - 1])

        # Generating the Temperature Profile at t=0
        temp_fm.append(temp_delta)

    for x in well.sections:
        for y in range(well.cells_no):
            x[y]['temp'] = temp_fm[y]
            x[y]['temp_fm'] = temp_fm[y]

    return well.sections, temp_fm
