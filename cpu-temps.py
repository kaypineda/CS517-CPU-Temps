''' CS 517 Semester Project: CPU Temps
Kayla Pineda   UIN: 01168338 '''

import argparse
import parse_temps as pt

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input data file')
args = parser.parse_args()


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


def piecewise_linear_interpolation(times, data):
    # print("Not yet implemented")
    pli = []
    # take the slope between two points
    for i,t in enumerate(times):
        if i == len(times) - 1:
            break
        m = (data[i+1] - data[i]) / times[i+1] - times[i]
        pli.append(m)

    return pli


def least_squares_approximation(time, data):
    print("Not yet implemented")


if __name__ == "__main__":
    print(args.input_file)

    times, core0, core1, core2, core3 = read_file(args.input_file)
    print_all_cores(times, core0, core1, core2, core3)

    core0_PLI = piecewise_linear_interpolation(times, core0)



