import numpy as np


def inputs_dict(casings=None):
    inputs = {'temp_inlet': None,           # fluid inlet temperature, °C
              'temp_surface': 15.0,         # surface temperature, °C
              'water_depth': 0.0,           # water depth, m
              'pipe_id': 4.0,               # pipe inner diameter, in
              'pipe_od': 4.5,               # pipe outer diameter, in
              'riser_id': 17.716,           # riser inner diameter, in
              'riser_od': 21.0,             # riser outer diameter, in
              'fm_diam': 80.0,              # undisturbed formation diameter, in
              'flowrate': 0.79,             # flow rate, m3/min
              'time': 10,                   # operation time if circulating, h

              # thermal conductivities, W / (m *°C)
              'tc_fluid': 0.635,            # fluid in pipe
              'tc_csg': 43.3,               # casing wall
              'tc_cem': 0.7,                # cement
              'tc_pipe': 40.0,              # pipe wall
              'tc_fm': 2.249,               # formation
              'tc_riser': 15.49,            # riser wall
              'tc_seawater': 0.6,           # seawater

              # specific heat capacities, J / (kg *°C)
              'shc_fluid': 3713.0,          # fluid in pipe
              'shc_csg': 469.0,             # casing wall
              'shc_cem': 2000.0,            # cement
              'shc_pipe': 400.0,            # pipe wall
              'shc_riser': 464.0,           # riser wall
              'shc_seawater': 4000.0,       # seawater
              'shc_fm': 800.0,              # formation

              # densities, sg
              'rho_fluid': 1.198,           # fluid in pipe
              'rho_pipe': 7.8,              # pipe wall
              'rho_csg': 7.8,               # casing wall
              'rho_riser': 7.8,             # riser wall
              'rho_fm': 2.245,              # formation
              'rho_seawater': 1.029,        # seawater
              'rho_cem': 2.7,               # cement

              'th_grad_fm': 0.0238,         # geothermal gradient, °C/m
              'th_grad_seawater': -0.005,   # seawater thermal gradient, °C/m
              'hole_diam': 0.216,           # diameter of open hole section, m
              'rpm': 100.0,                 # revolutions per minute
              'tbit': 5.0,                  # torque on the bit, kN*m
              'wob': 90.0,                  # weight on bit, kN
              'rop': [30.4],                # rate of penetration, m/h
              'an': 3100.0,                 # area of the nozzles, in^2
              'bit_n': 1.0,                 # drill bit efficiency, 0 to 1
              'dp_e': 0.0,                  # drill pipe eccentricity
              'thao_o': 1.82,               # yield stress, Pa
              'beta': 44983 * 10 ** 5,      # isothermal bulk modulus, Pa
              'alpha': 960 * 10 ** -6,      # expansion coefficient, 1/°C
              'k': 0.3832,                  # consistency index, Pa*s^n
              'n': 0.7,                     # flow behavior index, dimensionless
              'visc': 0.009                 # fluid viscosity
              }

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
