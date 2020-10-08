from math import pi, log


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
