import numpy as np


def inputs_dict(casings=None):
    inputs = {'temp_inlet': None, 'temp_surface': 15.0, 'water_depth': 0.0,
              'pipe_id': 4.0, 'pipe_od': 4.5, 'riser_id': 17.716, 'riser_od': 21.0, 'fm_diam': 80.0,
              'q': 794.933,

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
