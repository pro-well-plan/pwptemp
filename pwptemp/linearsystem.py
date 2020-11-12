import numpy as np
from .heat_coefficients import add_heat_coefficients


def define_system_section0(well, sections, bit_position):
    for x, y in enumerate(sections[0][:bit_position+1]):
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

        if 1 < x <= bit_position:
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


def define_system_section1(well, sections, bit_position):
    for x, y in enumerate(sections[1][:bit_position+1]):
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

        if 0 < x < bit_position:
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

        if x == bit_position:
            y['N'] = 0
            y['W'] = 0
            y['C'] = 0
            y['E'] = 0
            y['S'] = 0
            y['B'] = 0

    return well


def define_system_section2(well, sections, bit_position):
    for x, y in enumerate(sections[2][:bit_position+1]):
        if x < well.cells_no - 1:
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

        if x == bit_position:
            y['N'] = 0
            y['W'] = 0
            y['C'] = 0
            y['E'] = 0
            y['S'] = 0
            y['B'] = 0

    return well


def define_system_section3(well, sections, bit_position):
    for x, y in enumerate(sections[3][:bit_position+1]):
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

        if 0 < x < bit_position:
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

        if x == bit_position:
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


def define_system_section4(well, sections, bit_position):
    for x, y in enumerate(sections[4][:bit_position+1]):
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

        if 0 < x < bit_position:
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

        if x == bit_position:
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


def solve_pentadiagonal_system(well, bit_position):
    # Creating penta-diagonal matrix
    number_of_cells = bit_position + 1
    a = np.zeros((5 * number_of_cells, 5 * number_of_cells + 10))

    matrix = populate_matrix(a, well, bit_position)

    matrix = crop_matrix(matrix)

    constant_values = define_b_list(well, bit_position)

    temp_list = np.linalg.solve(matrix, constant_values)

    return temp_list


def populate_matrix(matrix, well, bit_position):
    row = 0
    column_base = 0

    for x in range(bit_position + 1):
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

    """# Uncomment this to check the matrix cropped as a dataframe
    import pandas as pd
    df = pd.DataFrame(matrix)
    print(df.to_string())"""

    return matrix


def define_b_list(well, bit_position):
    b_list = []

    for x in range(bit_position + 1):
        for y in well.sections:
            b_list.append(y[x]['B'])

    b_list = b_list[1:-2]

    return b_list


def calc_temperature_distribution(well, time_step, bit_position):
    add_heat_coefficients(well, time_step, bit_position)
    well = add_values(well, bit_position)
    temp_list = solve_pentadiagonal_system(well, bit_position)
    well = update_temp(well, temp_list, bit_position)

    return well


def add_values(well, bit_position):
    well = define_system_section0(well, well.sections, bit_position)  # System section 0

    well = define_system_section1(well, well.sections, bit_position)  # System section 1

    well = define_system_section2(well, well.sections, bit_position)  # System section 2

    well = define_system_section3(well, well.sections, bit_position)  # System section 3

    well = define_system_section4(well, well.sections, bit_position)  # System section 4

    for x in ['N', 'W', 'C', 'E', 'S', 'B']:
        well.sections[1][bit_position][x] = well.sections[3][bit_position][x]
        well.sections[2][bit_position][x] = well.sections[4][bit_position][x]

    return well


def update_temp(well, temp_list, bit_position):
    rebuilt = [well.temp_inlet] + list(temp_list[:-3]) + [temp_list[-3]] * 3 + list(temp_list[-2:])

    list_index = 0
    for x in range(bit_position + 1):
        for y in well.sections:
            y[x]['temp'] = rebuilt[list_index]
            list_index += 1

    return well
