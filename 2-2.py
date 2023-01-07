# rock = ['A', 'X']
# paper = ['B', 'Y']
# scissors = ['C', 'Z']

# a,y = 2 + 6 = 8
# b,x = 1 + 0 = 1
# c,z = 3 + 3 = 6

# file = '''A Y
# B X
# C Z
# '''

# input = file.splitlines()

file = open('input/2.txt', 'r')
input = file.readlines()


class Sign:
    def __init__(self, name, score):
        self.name = name
        self.score = score


rock = Sign('rock', 1)
paper = Sign('paper', 2)
scissors = Sign('scissors', 3)

opponent_moves = {
    'A': rock,
    'B': paper,
    'C': scissors
}

player_moves = {
    'X': rock,
    'Y': paper,
    'Z': scissors
}

result_scores = {
    'win': 6,
    'draw': 3,
    'lose': 0
}

sign_relationships = {
    rock: {
        paper: 'lose',
        scissors: 'win',
    },
    paper: {
        rock: 'win',
        scissors: 'lose',
    },
    scissors: {
        rock: 'lose',
        paper: 'win',
    }
}

outcomes = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}


def play(opponent_move, player_move):
    opponent_sign = opponent_moves[opponent_move]
    player_sign = player_moves[player_move]
    move_score = player_moves[player_move].score
    game_score = result_scores['draw']

    if (opponent_sign != player_sign):
        result = sign_relationships[player_sign][opponent_sign]
        game_score = result_scores[result]

    return move_score + game_score


def choose_sign(opponent_move, outcome):
    opponent_sign = opponent_moves[opponent_move]
    desired_outcome = outcomes[outcome]

    game_score = result_scores[desired_outcome]

    if desired_outcome == 'draw':
        return game_score + opponent_sign.score

    if desired_outcome == 'win':
        desired_outcome = 'lose'
    else:
        desired_outcome = 'win'

    possible_outcomes = sign_relationships[opponent_sign]
    player_sign = list(possible_outcomes.keys())[list(
        possible_outcomes.values()).index(desired_outcome)]

    return player_sign.score + game_score


def get_score_by_sign():
    total_score = 0
    for game in input:
        moves = game.split()
        total_score += play(moves[0], moves[1])

    return total_score


def get_score_by_outcome():
    total_score = 0
    for game in input:
        moves = game.split()
        total_score += choose_sign(moves[0], moves[1])

    return total_score


# 1
print(get_score_by_sign())

# 2
print(get_score_by_outcome())
