# for printing and reading

import parse_temps as pt
from dateutil import parser


def read_file(input_file):
    '''
    Read data from an input file and store, code adapted from Prof Kennedy's parse_temps example
    :param input_file: the input file

    :return: array containing the times and an array containing cpu temps for each core
    '''

    temp_file = open(input_file, 'r')

    times = []
    core0 = []
    core1 = []
    core2 = []
    core3 = []
    for time, core_data in pt.parse_raw_temps(temp_file):
        times.append(time)
        core0.append(core_data[0])
        core1.append(core_data[1])
        core2.append(core_data[2])
        core3.append(core_data[3])

    temp_file.close()

    return times, core0, core1, core2, core3


def get_date(input_file):
    '''
    Extract the date from an input file name
    :param input_file: the input file
    :return: the date from the input file
    '''

    full_date = parser.parse(input_file, fuzzy=True)
    date = str(full_date)[:10]

    return date


def print_all_cores(times, core0, core1, core2, core3):
    '''
    Print the data of all cores
    :param times: times in seconds
    :param core0: cpu temps of core 0
    :param core1: cpu temps of core 1
    :param core2: cpu temps of core 2
    :param core3: cpu temps of core 3

    :return: prints all data
    '''
    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core0[i]:<5} | {core1[i]:<5} | {core2[i]:<5} | {core3[i]:<5} |')


def print_single_core(times, core):
    '''
    Prints data of single core
    :param times: times in seconds
    :param core: cpu temps of a core

    :return: prints core data
    '''
    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core[i]:<5} |')


def write_output_file(date, core, times, data_LSA, data_PLI):
    """
    Creates output file
    :param date: the date the data was acquired
    :param core: name of the core
    :param times: times in seconds
    :param data_LSA: least squares approximation of a core
    :param data_PLI: piecewise linear interpolation of a core

    :return: output file listing piecewise linear interpolation data of a core
    """
    output_file = "output/" + date + "-" + core + ".txt"
    output = open(output_file, "w")

    output.write(f'{times[0]:<7} <= x < {times[len(times) - 1]:>7}; y_0 = {data_LSA[0]:>5} + {data_LSA[1]:>7}x; '
                 f'least squares \n')

    for i,t in enumerate(times):
        if i == len(times) - 1:
            break

        y_int, m = data_PLI[i]
        data_rounded = '{:.4f}'.format(round(m, 4))

        output.write(f'{times[i]:<7} <= x < {times[i+1]:>7}; y_{i:<5} = {y_int:>5} + {data_rounded:>7}x; '
                     f'interpolation \n')

    output.close()
