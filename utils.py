# for printing and reading

import parse_temps as pt
from dateutil import parser


def read_file(input_file):
    """
    Read data from an input file and store, code adapted from Prof Kennedy's parse_temps example

    :param input_file: the input file

    :return: array containing the times and an array containing cpu temps for each core
    """

    temp_file = open(input_file, 'r')

    times = []
    cores = [[] for _ in range(0, 4)]

    for time, raw_core_data in pt.parse_raw_temps(temp_file):
        times.append(time)
        for i, reading in enumerate(raw_core_data):
            cores[i].append(reading)

    temp_file.close()

    return times, cores


def get_date(input_file):
    """
    Extract the date from an input file name

    :param input_file: the input file

    :return: the date from the input file
    """

    full_date = parser.parse(input_file, fuzzy=True)
    date = str(full_date)[:10]

    return date


def print_core(times, core):
    """
    Prints data of a core

    :param times: times in seconds
    :param core: cpu temps of a core

    :return: prints core data
    """

    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core[i]:<5} |')


def write_output_file(date, core_num, times, data_PLI, data_LSA):
    """
    Creates output file for a core

    :param date: the date the data was acquired
    :param core_num: number of the core
    :param times: times in seconds
    :param data_PLI: piecewise linear interpolation of a core
    :param data_LSA: least squares approximation of a core

    :return: output file listing piecewise linear interpolation data of a core
    """

    output_file = "output/" + date + "-core" + str(core_num) + ".txt"
    output = open(output_file, "w")

    c_0_rounded = '{:.5f}'.format(round(data_LSA[0], 5))

    output.write(f'{times[0]:<7} <= x < {times[len(times) - 1]:>7}; y       = {c_0_rounded:>5} + {data_LSA[1]:.5e}x; '
                 f'least squares \n'
                 f'-----------------------------------------------------------------------------\n')

    for i,t in enumerate(times):
        if i == len(times) - 1:
            break

        y_int, m = data_PLI[i]
        m_rounded = '{:.4f}'.format(round(m, 4))

        output.write(f'{times[i]:<7} <= x < {times[i+1]:>7}; y_{i:<5} = {y_int:>5} + {m_rounded:>7}x; '
                     f'interpolation \n')

    output.close()
