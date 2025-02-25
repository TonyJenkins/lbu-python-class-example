#!/usr/bin/env python3

import sys

from competitor import Competitor, CompetitorFileFormatError


def read_scores(scores_file):

    scores = []
    with open(scores_file, 'r') as sf:
        for entry in sf:
            try:
                scores.append(Competitor(entry))
            except:
                raise CompetitorFileFormatError('Problem in the data file')

    return scores


def print_leaderboard(sorted_scores):

    for entry in sorted_scores:
        print(entry.leaderboard_line())


if __name__ == '__main__':

    try:
        scores = read_scores(sys.argv[1])
        scores.sort(reverse=True)
        print_leaderboard(scores)

    except FileNotFoundError:
        print(f'Cannot open "{sys.argv[1]}"')
    except IndexError:
        print(f'No filename provided')
    except CompetitorFileFormatError:
        print(f'Invalid file format found')
