''' CS 517 Semester Project: CPU Temps
Kayla Pineda   UIN: 01168338 '''

import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input data file')
args = parser.parse_args()


def piecewise_linear_interpolation(times, data):
    pli = []
    # take the slope between two points
    for i,t in enumerate(times):
        if i == len(times) - 1:
            break
        # print(data[i+1], data[i], times[i+1], times[i])
        m = (data[i+1] - data[i]) / (times[i+1] - times[i])
        # print(m)
        pli.append([data[i], m])

    return pli


def least_squares_approximation(time, data):
    print("Not yet implemented")


if __name__ == "__main__":
    date = utils.get_date(args.input_file)

    times, core0, core1, core2, core3 = utils.read_file(args.input_file)
    # utils.print_all_cores(times, core0, core1, core2, core3)

    core0_PLI = piecewise_linear_interpolation(times, core0)

    utils.create_output_file(date, "core0", times, core0_PLI, "interpolation")



