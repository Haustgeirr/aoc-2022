# rock = ['A', 'X']
# paper = ['B', 'Y']
# scissors = ['C', 'Z']

# a,y = 2 + 6 = 8
# b,x = 1 + 0 = 1
# c,z = 3 + 3 = 6

# input = '''A Y
# B X
# C Z
# '''

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


def play(opponent_move, player_move):
    opponent_sign = opponent_moves[opponent_move]
    player_sign = player_moves[player_move]
    move_score = player_moves[player_move].score
    game_score = result_scores['draw']

    if (opponent_sign != player_sign):
        result = sign_relationships[player_sign][opponent_sign]
        game_score = result_scores[result]

    return move_score + game_score


total_score = 0
for game in input:
    moves = game.split()
    total_score += play(moves[0], moves[1])


print(total_score)
