import numpy as np
from math import pi, log
from copy import deepcopy
import torque_drag as td
import plotly.graph_objects as go


def create_depth_cells(trajectory):
    md_new = list(np.linspace(0, max(trajectory.md), num=100))
    tvd_new, inclination, azimuth = [], [], []
    for i in md_new:
        tvd_new.append(np.interp(i, trajectory.md, trajectory.tvd))
        inclination.append(np.interp(i, trajectory.md, trajectory.inclination))
        azimuth.append(np.interp(i, trajectory.md, trajectory.azimuth))
    depth_step = md_new[1]

    return md_new, tvd_new, depth_step, inclination, azimuth


def inputs_dict(casings=None):
    inputs = {'temp_inlet': None, 'temp_surface': 15.0, 'water_depth': 0.0,
              'pipe_id': 4.0, 'pipe_od': 4.5, 'riser_id': 17.716, 'riser_od': 21.0, 'fm_diam': 80.0,
              'q': 700,

              'tc_fluid': 0.635, 'tc_csg': 43.3, 'tc_cem': 0.7, 'tc_pipe': 40.0,
              'tc_fm': 2.249, 'tc_riser': 15.49, 'tc_seawater': 0.6,

              'shc_fluid': 3713.0, 'shc_csg': 469.0, 'shc_cem': 2000.0, 'shc_pipe': 400.0,
              'shc_riser': 464.0, 'shc_seawater': 4000.0, 'shc_fm': 800.0,

              'rho_fluid': 1.198, 'rho_pipe': 7.8, 'rho_csg': 7.8, 'rho_riser': 7.8,
              'rho_fm': 2.245, 'rho_seawater': 1.029, 'rho_cem': 2.7,

              'th_grad_fm': 0.0238, 'th_grad_seawater': -0.005, 'hole_diam': 0.216,
              'rpm': 100.0, 'tbit': 0.0, 'wob': 0.0, 'rop': 30.4, 'an': 3100.0, 'bit_n': 1.0, 'dp_e': 0.0,
              'thao_o': 1.82, 'beta': 44983 * 10 ** 5, 'alpha': 960 * 10 ** -6,
              'k': 0.3832, 'n': 0.7}

    dict_with_casings = add_casings(casings, inputs)

    return dict_with_casings


def add_casings(casings, inputs):
    if casings is None:
        inputs['casings'] = [[(inputs['hole_diam'] + inputs['riser_od'] * 0.0254), inputs['hole_diam'], 0]]
        inputs['casings'] = np.asarray(inputs['casings'])
    else:
        csg_od = sorted([x['od'] * 0.0254 for x in casings])  # in to m
        csg_id = sorted([x['id'] * 0.0254 for x in casings])  # in to m
        depth = sorted([x['depth'] for x in casings], reverse=True)
        inputs['casings'] = [[csg_od[x], csg_id[x], depth[x]] for x in range(len(casings))]
        inputs['casings'] = np.asarray(inputs['casings'])

    return inputs


def set_well(temp_dict, trajectory):
    q_conv = 0.06  # from lpm to m^3/h
    an_conv = 1 / 1500  # from in^2 to m^2
    diameter_conv = 0.0254

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
            self.fm_rad = self.fm_diam / 2  # Undisturbed Formation Radius, m

            # OPERATIONAL
            self.temp_surface = temp_dict["temp_surface"]  # Surface Temperature (RKB), °C
            if temp_dict["temp_inlet"] is None:
                self.temp_inlet = self.temp_surface
            else:
                self.temp_inlet = temp_dict["temp_inlet"]  # Inlet Fluid temperature, °C
            self.th_grad_fm = temp_dict["th_grad_fm"]  # Geothermal gradient, from °C/m to °C/cell
            self.q = temp_dict["q"] * q_conv  # Flow rate, m^3/h
            # Fluid velocity through the annular
            self.va = (self.q / (pi * ((self.annular_or ** 2) - (self.r2 ** 2)))) / 3600
            self.vp = (self.q / (pi * (self.r1 ** 2))) / 3600  # Fluid velocity through the drill pipe
            self.rpm = temp_dict["rpm"]  # Revolutions per minute
            self.tbit = temp_dict["tbit"]  # Torque on the bit, kN*m
            self.wob = temp_dict["wob"]  # Weight on bit, kN
            self.rop = temp_dict["rop"]  # Rate of Penetration, m/h
            self.an = temp_dict["an"] * an_conv  # Area of the nozzles, m^2
            self.bit_n = temp_dict["bit_n"]  # drill bit efficiency
            self.dp_e = temp_dict["dp_e"]  # drill pipe eccentricity
            self.thao_o = temp_dict["thao_o"]
            self.k = temp_dict["k"]
            self.n = temp_dict["n"]

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

    return NewWell()


def create_system(well):
    section_0, section_1, section_2, section_3, section_4 = [], [], [], [], []
    for x in range(well.cells_no):
        initial_dict = {'component': '', 'material': '', 'rho': 2.24, 'visc': 0.02, 'tc': '', 'shc': ''}
        section_0.append(deepcopy(initial_dict))
        section_1.append(deepcopy(initial_dict))
        section_2.append(deepcopy(initial_dict))
        section_3.append(deepcopy(initial_dict))
        section_4.append(deepcopy(initial_dict))
    sections = [section_0, section_1, section_2, section_3, section_4]
    sections_names = ['section_0', 'section_1', 'section_2', 'section_3', 'section_4']

    for x, i in zip(sections, sections_names):
        for y in range(well.cells_no):
            x[y]['material'] = get_material(i, well.md[y], first_casing_depth=well.casings[0, 2])
            if x[y]['material'] in 'mixture':
                pipe_fraction, cement_fraction = get_fractions_at_depth(well, y)
                x[y]['rho'] = get_mixture_density(pipe_fraction, cement_fraction, well) * 1000
                x[y]['tc'] = get_mixture_thermal_conductivity(pipe_fraction, cement_fraction, well)
                x[y]['shc'] = get_mixture_heat_capacity(pipe_fraction, cement_fraction, well)

            elif x[y]['material'] in 'seawater':
                x[y]['rho'] = well.rho_seawater
                x[y]['tc'] = well.tc_seawater
                x[y]['shc'] = well.shc_seawater

            else:
                x[y]['rho'] = get_density(x[y]['material'], well) * 1000
                x[y]['tc'] = get_thermal_conductivity(x[y]['material'], well)
                x[y]['shc'] = get_heat_capacity(x[y]['material'], well)

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
        section_4 = 'formation'
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


def calc_temp(time, trajectory, casings=None, set_inputs=None):
    tcirc = time * 3600  # circulating time, s
    time_step = tcirc / 100
    tstep = int(tcirc / time_step)

    tdata = inputs_dict(casings)

    if set_inputs is not None:
        for x in set_inputs:  # changing default values
            if x in tdata:
                tdata[x] = set_inputs[x]
            else:
                raise TypeError('%s is not a parameter' % x)

    well = set_well(tdata, trajectory)
    well.delta_time = time_step
    well = calc_temperature_distribution(well, time_step)

    for x in range(tstep - 1):
        if tstep > 1:
            well = calc_temperature_distribution(well, time_step)

    well = define_temperatures(well)
    well.time = time

    return well


def calc_temperature_distribution(well, time_step):
    add_heat_coefficients(well, time_step)
    well = add_values(well)
    temp_list = solve_pentadiagonal_system(well)
    well = update_temp(well, temp_list)

    return well


def add_heat_coefficients(well, delta_time):
    for x, y in enumerate(well.sections[0]):
        y['comp_N/S'] = ((y['rho'] * y['shc'] * well.vp) / well.depth_step) / 2
        y['comp_E'] = (2 * well.h1[x] / well.r1) / 2
        y['comp_HeatSource'] = calc_heat_source(well, well.torque[x], y['f'], y['rho'], case='pipe')
        y['comp_time'] = y['rho'] * y['shc'] / delta_time
    for x, y in enumerate(well.sections[1]):
        y['comp_N/S'] = (y['tc'] / (well.depth_step ** 2)) / 2
        y['comp_E'] = (2 * well.r2 * well.h2[x] / ((well.r2 ** 2) - (well.r1 ** 2))) / 2
        y['comp_W'] = (2 * well.r1 * well.h1[x] / ((well.r2 ** 2) - (well.r1 ** 2))) / 2
        y['comp_time'] = y['rho'] * y['shc'] / delta_time
    for x, y in enumerate(well.sections[2]):
        y['comp_N/S'] = (y['rho'] * y['shc'] * well.va / well.depth_step) / 2
        y['comp_E'] = (2 * well.annular_or * well.h3[x] / ((well.annular_or ** 2) - (well.r2 ** 2))) / 2
        y['comp_W'] = (2 * well.r2 * well.h2[x] / ((well.annular_or ** 2) - (well.r2 ** 2))) / 2
        y['comp_HeatSource'] = calc_heat_source(well, well.torque[x], y['f'], y['rho'], case='annular')
        y['comp_time'] = y['rho'] * y['shc'] / delta_time
    for x, y in enumerate(well.sections[3]):
        y['comp_N/S'] = (y['tc'] / (well.depth_step ** 2)) / 2
        y['comp_E'] = (2 * y['tc'] / ((well.sr_ir ** 2) - (well.annular_or ** 2))) / 2
        y['comp_W'] = (2 * well.annular_or * well.h3[x] / ((well.sr_ir ** 2) - (well.annular_or ** 2))) / 2
        y['comp_time'] = y['rho'] * y['shc'] / delta_time
    for x, y in enumerate(well.sections[4]):
        y['comp_N/S'] = (y['tc'] / (well.depth_step ** 2)) / 2
        y['comp_E'] = (y['tc'] / (well.sr_or * (well.sr_or - well.sr_ir) * log(well.sr_or / well.sr_ir))) / 2
        y['comp_W'] = (y['tc'] / (well.sr_or * (well.sr_or - well.sr_ir) * log(well.fm_rad / well.sr_or))) / 2
        y['comp_time'] = y['rho'] * y['shc'] / delta_time


def calc_heat_source(well, torque, f, rho_fluid, case='pipe'):
    if case == 'pipe':
        qp = 2 * pi * (well.rpm / 60) * torque
        + 0.2 * well.q * 2 * f * rho_fluid * (well.vp ** 2) * (well.md[-1] / (well.pipe_id * 127.094 * 10 ** 6))
        heat_source_term = qp / (pi * (well.r1 ** 2))
    else:
        qa = (0.085 * (2 * well.k * well.md[-1] / ((well.annular_or - well.r2) * (127.094 * 10 ** 6))) *
              ((2 * (well.n + 1) * well.q) / (well.n * pi * (well.annular_or + well.r2) *
                                              (well.annular_or - well.r2) ** 2)) ** well.n) * (
                         1 + (3 / 2) * well.dp_e ** 2) ** 0.5
        heat_source_term = qa / (pi * ((well.annular_or ** 2) - (well.r2 ** 2)))

    return heat_source_term


def add_values(well):
    well = define_system_section0(well, well.sections)  # System section 0

    well = define_system_section1(well, well.sections)  # System section 1

    well = define_system_section2(well, well.sections)  # System section 2

    well = define_system_section3(well, well.sections)  # System section 3

    well = define_system_section4(well, well.sections)  # System section 4

    for x in ['N', 'W', 'C', 'E', 'S', 'B']:
        well.sections[1][-1][x] = well.sections[3][-1][x]
        well.sections[2][-1][x] = well.sections[4][-1][x]

    return well


def define_system_section0(well, sections):
    for x, y in enumerate(sections[0]):
        if x == 0:
            y['N'] = 0
            y['W'] = 0
            y['C'] = 0
            y['E'] = 0
            y['S'] = 0
            y['B'] = 0
            y['temp'] = well.temp_inlet

        if x == 1:
            y['N'] = 0
            y['W'] = 0
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = 0
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_HeatSource'] \
                     + y['comp_E'] * (sections[1][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[0][x - 1]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[0][x - 1]['temp'])

        if 1 < x <= well.cells_no - 1:
            y['N'] = - y['comp_N/S']
            y['W'] = 0
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = 0
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_HeatSource'] \
                     + y['comp_E'] * (sections[1][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[0][x - 1]['temp'] - y['temp'])

    return well


def define_system_section1(well, sections):
    for x, y in enumerate(sections[1]):
        if x == 0:
            y['N'] = 0
            y['W'] = 0
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * (sections[2][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[0][x]['temp'] - y['temp']) \
                     + y['comp_W'] * sections[0][x]['temp'] \
                     + y['comp_N/S'] * (sections[1][x + 1]['temp'] - y['temp'])

        if 0 < x < well.cells_no - 1:
            y['N'] = - y['comp_N/S']
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + 2 * y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * (sections[2][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[0][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[1][x - 1]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[1][x + 1]['temp'] - y['temp'])

        if x == well.cells_no - 1:
            y['N'] = 0
            y['W'] = 0
            y['C'] = 0
            y['E'] = 0
            y['S'] = 0
            y['B'] = 0

    return well


def define_system_section2(well, sections):
    for x, y in enumerate(sections[2]):
        if x == 0:
            y['N'] = 0
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_HeatSource'] \
                     + y['comp_E'] * (sections[3][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[1][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[2][x + 1]['temp'] - y['temp'])

        if 0 < x < well.cells_no - 1:
            y['N'] = 0
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_HeatSource'] \
                     + y['comp_E'] * (sections[3][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[1][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[2][x + 1]['temp'] - y['temp'])

        if x == well.cells_no - 1:
            y['N'] = 0
            y['W'] = 0
            y['C'] = 0
            y['E'] = 0
            y['S'] = 0
            y['B'] = 0

    return well


def define_system_section3(well, sections):
    for x, y in enumerate(sections[3]):
        if x == 0:
            y['N'] = 0
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * (sections[4][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[2][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[3][x + 1]['temp'] - y['temp'])

        if 0 < x < well.cells_no - 1:
            y['N'] = - y['comp_N/S']
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + 2 * y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * (sections[4][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[2][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[3][x - 1]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[3][x + 1]['temp'] - y['temp'])

        if x == well.cells_no - 1:
            y['N'] = - y['comp_N/S']
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = - y['comp_E']
            y['S'] = 0
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * (sections[4][x]['temp'] - y['temp']) \
                     + y['comp_W'] * (sections[2][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[3][x - 1]['temp'] - y['temp'])

    return well


def define_system_section4(well, sections):
    for x, y in enumerate(sections[4]):
        if x == 0:
            y['N'] = 0
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = 0
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * y['temp_fm'] \
                     + y['comp_W'] * (sections[3][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[4][x + 1]['temp'] - y['temp'])

        if 0 < x < well.cells_no - 1:
            y['N'] = - y['comp_N/S']
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + 2 * y['comp_N/S']
            y['E'] = 0
            y['S'] = - y['comp_N/S']
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * y['temp_fm'] \
                     + y['comp_W'] * (sections[3][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[4][x - 1]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[4][x + 1]['temp'] - y['temp'])

        if x == well.cells_no - 1:
            y['N'] = - y['comp_N/S']
            y['W'] = - y['comp_W']
            y['C'] = y['comp_time'] + y['comp_E'] + y['comp_W'] + y['comp_N/S']
            y['E'] = 0
            y['S'] = 0
            y['B'] = y['comp_time'] * y['temp'] \
                     + y['comp_E'] * y['temp_fm'] \
                     + y['comp_W'] * (sections[3][x]['temp'] - y['temp']) \
                     + y['comp_N/S'] * (sections[4][x - 1]['temp'] - y['temp'])

    return well


def solve_pentadiagonal_system(well):
    # Creating penta-diagonal matrix
    a = np.zeros((5 * well.cells_no, 5 * well.cells_no + 10))

    matrix = populate_matrix(a, well)

    matrix = crop_matrix(matrix)

    constant_values = define_b_list(well)

    temp_list = np.linalg.solve(matrix, constant_values)

    return temp_list


def populate_matrix(matrix, well):
    row = 0
    column_base = 0

    for x in range(well.cells_no):
        for y in well.sections:
            matrix[row, column_base] = y[x]['N']
            matrix[row, column_base + 4] = y[x]['W']
            matrix[row, column_base + 5] = y[x]['C']
            matrix[row, column_base + 6] = y[x]['E']
            matrix[row, column_base + 10] = y[x]['S']
            row += 1
            column_base += 1

    """# TRY THE CODE BELOW TO CHECK THAT THERE IS NOT ANY ROW WITH ONLY 0
    import pandas as pd
    df = pd.DataFrame(matrix)
    #df["sum"] = df.sum(axis=1)
    print(df)
    #print(df[df["sum"] == 0.0])"""

    return matrix


def crop_matrix(matrix):
    matrix = np.delete(matrix, 0, axis=0)
    matrix = np.delete(matrix, range(6), axis=1)
    matrix = np.delete(matrix, [-1, -2, -3, -4, -5], axis=1)
    matrix = np.delete(matrix, [-1, -2], axis=0)
    matrix = np.delete(matrix, [-1, -2], axis=1)

    matrix[-7, -3] = matrix[-7, -2]
    matrix[-7, -2] = 0
    matrix[-6, -3] = matrix[-6, -1]
    matrix[-6, -1] = 0

    """import pandas as pd
    df = pd.DataFrame(matrix)
    print(df.to_string())"""

    return matrix


def define_b_list(well):
    b_list = []

    for x in range(well.cells_no):
        for y in well.sections:
            b_list.append(y[x]['B'])

    b_list = b_list[1:-2]

    return b_list


def update_temp(well, temp_list):
    rebuilt = [well.temp_inlet] + list(temp_list[:-3]) + [temp_list[-3]] * 3 + list(temp_list[-2:])

    list_index = 0
    for x in range(well.cells_no):
        for y in well.sections:
            y[x]['temp'] = rebuilt[list_index]
            list_index += 1

    return well


def define_temperatures(well):
    new_md = list(np.linspace(0, well.md[-1], num=int(well.md[-1] / 10)))
    temp_fm = []
    temp_in_pipe = []
    temp_pipe = []
    temp_annulus = []
    temp_casing = []
    temp_riser = []
    temp_sr = []
    for x in new_md:
        temp_fm.append(np.interp(x, well.md, well.temp_fm))
        temp_in_pipe.append(np.interp(x, well.md, [x['temp'] for x in well.sections[0]]))
        temp_pipe.append(np.interp(x, well.md, [x['temp'] for x in well.sections[1]]))
        temp_annulus.append(np.interp(x, well.md, [x['temp'] for x in well.sections[2]]))
        temp_sr.append(np.interp(x, well.md, [x['temp'] for x in well.sections[4]]))

        if well.riser_cells > 0 and x < well.water_depth:
            temp_casing.append(None)
            temp_riser.append(np.interp(x, well.md, [x['temp'] for x in well.sections[3]]))
        else:
            temp_riser.append(None)
            if x <= well.casings[0, 2]:
                temp_casing.append(np.interp(x, well.md, [x['temp'] for x in well.sections[3]]))
            else:
                temp_casing.append(None)

    well.temperatures = {'md': new_md,
                         'formation': temp_fm,
                         'in_pipe': temp_in_pipe,
                         'pipe': temp_pipe,
                         'annulus': temp_annulus,
                         'casing': temp_casing,
                         'riser': temp_riser,
                         'sr': temp_sr}

    return well


def plot_distribution(temp_distribution, operation='drilling'):
    pipe_name = {'drilling': 'Drill String',
                 'production': 'Production Tubing',
                 'injection': 'Injection Tubing'}

    # Plotting Temperature PROFILE

    fig = go.Figure()
    md = temp_distribution.temperatures['md']
    riser = temp_distribution.riser_cells
    csg = temp_distribution.casings[0, 2]

    fig.add_trace(go.Scatter(x=temp_distribution.temperatures['in_pipe'], y=md,
                             mode='lines',
                             name='Fluid in ' + pipe_name[operation]))

    fig.add_trace(go.Scatter(x=temp_distribution.temperatures['annulus'], y=md,
                             mode='lines',
                             name='Fluid in Annulus'))

    if riser > 0:
        fig.add_trace(go.Scatter(x=temp_distribution.temperatures['riser'], y=md,
                                 mode='lines',
                                 name='Riser'))
    if csg > 0:
        fig.add_trace(go.Scatter(x=temp_distribution.temperatures['casing'], y=md,
                                 mode='lines',
                                 name='Casing'))
    fig.add_trace(go.Scatter(x=temp_distribution.temperatures['formation'], y=md,
                             mode='lines',
                             name='Formation'))  # Temp. due to gradient vs Depth

    fig.update_layout(
        xaxis_title='Temperature, °C',
        yaxis_title='Depth, m')

    title = 'Temperature Profile at %1.1f hours' % temp_distribution.time + ' of ' + operation
    fig.update_layout(title=title)

    fig.update_yaxes(autorange="reversed")

    return fig
