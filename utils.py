# for printing and reading

import parse_temps as pt
from dateutil import parser


def read_file(input_file):
    # Following code adapted from Prof Kennedy
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
    full_date = parser.parse(input_file, fuzzy=True)
    date = str(full_date)[:10]

    return date


def print_all_cores(times, core0, core1, core2, core3):
    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core0[i]:<5} | {core1[i]:<5} | {core2[i]:<5} | {core3[i]:<5} |')


def print_single_core(times, core):
    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core[i]:<5} |')


def create_output_file(date, core, times, data, type):
    output_file = "output/" + date + "-" + type + "-" + core + ".txt"
    output = open(output_file, "w")

    for i,t in enumerate(times):
        if i == len(times) - 1:
            break

        y_int, m = data[i]
        data_rounded = '{:.4f}'.format(round(m, 4))

        output.write(f'{times[i]:<7} <= x < {times[i+1]:<7}; y_{i:<5} = {y_int:<5} + {data_rounded:>7}x; {type} \n')
        # print(f'{times[i]:<6} <= x < {times[i + 1]:>6}; y_{i:<5} = {y_int:<5} + {data_rounded:>7}x; {type}')

    output.close()
