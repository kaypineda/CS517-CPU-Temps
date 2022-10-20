# for printing and reading

import parse_temps as pt


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


def print_all_cores(times, core0, core1, core2, core3):
    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core0[i]:<5} | {core1[i]:<5} | {core2[i]:<5} | {core3[i]:<5} |')


def print_single_core(times, core):
    for i,t in enumerate(times):
        print(f'{times[i]:<7} || {core[i]:<5} |')
