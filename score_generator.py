#!/usr/bin/env python3
import sys
import os
import argparse
import csv
import random

def get_parser():
    '''Get ArgumentParser'''
    parser = argparse.ArgumentParser(
        description='''Generate a random set of football (soccer) scores based
        on historical data from the English first four divisions.''')
    parser.add_argument('-n', '--number', type=int,
                        default=10,
                        help='''Number of scores to generate. Default=10''')
    parser.add_argument('-y', '--years', metavar='[1993-2018]', type=int,
                        nargs='+',
                        help='''One or more years to read data from. Defaults
                        to all available years (1993-2018).''')
    parser.add_argument('-t', '--tiers', metavar='[1-4]', type=int, nargs='+',
                        help='''Which tiers/divisions to read data from.
                        Defaults to all available tiers (1-4).''')
    parser.add_argument('-s', '--scorelines', action='store_true',
                        help='''Pick from results from full scorelines. By
                        default goals for home and away sides are randomly
                        drawn individually from the historical data. If you
                        prefer to randomly pull full scorelines use this
                        option.''')
    return parser

def read_scores(filename):
    ''' Read CSV files as downloaded from http://www.football-data.co.uk '''
    scores = []
    with open(filename, 'rt', errors='ignore', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = dict((col, i) for i, col in enumerate(next(reader)))
        for col in ['FTHG', 'FTAG']:
            if col not in header:
                raise ValueError("Required column '{}' ".format(col) +
                                 "not found in {}".format(filename))
        for row in reader:
            home = row[header['FTHG']]
            away = row[header['FTAG']]
            if home != '' and away != '':
                scores.append((home, away))
    return scores

def generate_scores(number, years=[], tiers=[], scorelines=False):
    '''
        Args:
            number: Number of scores to return

            years:  Years to extract previous scores from. Defaults to
                    1993-2018 (i.e. 93/94 season to 18/19 season).

            tiers:  Which football tiers (divisions) to extract previous
                    scores from. Defaults to tiers 1-4 (all available
                    tiers).

            use_scores:
                    Default behaviour is to randomly pull from home
                    goals and away goals separately. Set this argument
                    to True to in order to pull randomly from full
                    scorelines from individual games instead.
    '''
    if not years:
        years = range(1993, 2019)
    if not tiers:
        tiers = range(1, 5)
    scores = [] #tuple of home score and away score
    for t in tiers:
        for y in years:
            score_file=os.path.join(os.path.dirname(__file__),
                                    "data",
                                    str(y),
                                    "E" + str(t-1) + '.csv')
            try:
                scores.extend(read_scores(score_file))
            except Exception:
                raise RuntimeError("Error reading data for year {}".format(y) +
                                   " tier {}.".format(t))
    for n in range(number):
        if scorelines:
            home, away = random.choice(scores)
        else:
            home = random.choice(scores)[0]
            away = random.choice(scores)[1]
        print("{}-{}".format(home, away))


if __name__ == '__main__':
    parser = get_parser()
    args = parser.parse_args()
    generate_scores(**vars(args))
