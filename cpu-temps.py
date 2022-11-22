""" CS 517 Semester Project: CPU Temps
Kayla Pineda   UIN: 01168338 """

import argparse
import utils

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='input data file')
args = parser.parse_args()


def piecewise_linear_interpolation(time, data):
    """
    Find piecewise linear interpolation for a core

    :param time: array of times in seconds
    :param data:  cpu temp data from one core

    :return: an array of tuples containing the slope and y-intercept
             for each linear interpolation
    """

    pli = []
    # take the slope between two points
    for i,t in enumerate(time):
        if i == len(times) - 1:
            break
        m = (data[i+1] - data[i]) / (times[i+1] - times[i])
        pli.append([data[i], m])

    return pli


def least_squares_approximation(time, data):
    """
    Find least squares approximation for data.
    Only care about the linear case, so we can simplify the process.

    :param time: array of times (s)
    :param data: cpu temp data for a core
    :return:
    """
    n = len(time)
    S_x, S_x2, S_f, S_xf = 0, 0, 0, 0

    for i,t in enumerate(time):
        S_x += time[i]
        S_x2 += time[i] ** 2
        S_f += data[i]
        S_xf += time[i] * data[i]

    c_0 = ((S_x2 * S_f) - (S_x * S_xf)) / ((n * S_x2) - S_x ** 2)
    c_1 = ((n * S_xf) - (S_x * S_f)) / ((n * S_x2) - S_x ** 2)

    return c_0, c_1


if __name__ == "__main__":
    date = utils.get_date(args.input_file)

    times, cores = utils.read_file(args.input_file)

    cores_PLI = []
    cores_LSA = []
    for i,core in enumerate(cores):
        cores_PLI.append(piecewise_linear_interpolation(times, core))
        cores_LSA.append(least_squares_approximation(times, core))

    for i, core in enumerate(cores):
        utils.write_output_file(date, i, times, cores_LSA[i], cores_PLI[i])

