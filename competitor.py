#!/usr/bin/env python3

class CompetitorFileFormatError(Exception):
    pass

class Competitor:

    def __init__(self, result=''):
        if not result:
            self.name = ''
            self.score = 0
        else:
            self.name = result.split(',')[0]
            self.score = int(result.split(',')[1])

    def is_top_player(self):
        return self.score >= 10

    def update_score(self, new_score):
        self.score = new_score

    def leaderboard_line(self):
        return f'{self.name:8} : {self.score}.'

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __str__(self):
        return f'{self.name.title()} scored {self.score}.'


if __name__ == '__main__':

    tom = Competitor()
    print(tom)

    dick = Competitor('Dick, 12')
    print(dick)

    dick.update_score(14)
    print(dick)

    tom.score = 4
    print(tom > dick)

