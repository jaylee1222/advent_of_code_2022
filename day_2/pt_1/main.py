scores = []
total = 0
counter = 0
def determine_shape(letter_value):
    player_shape_values = {'A' : 'Rock', 'B' : 'Paper', 'C' : 'Scissors', 'X' : 'Rock', 'Y' : 'Paper', 'Z' : 'Scissors'}

    return player_shape_values[letter_value]

def fight(first_player, second_player):
    if second_player == 'Rock':
        match first_player:
            case 'Rock':
                return 'Tie'
            case 'Paper':
                return 'Lose'
            case 'Scissors':
                return 'Win'
    elif second_player == 'Paper':
        match first_player:
            case 'Rock':
                return 'Win'
            case 'Paper':
                return 'Tie'
            case 'Scissors':
                return 'Lose'
    else:
        match first_player:
            case 'Rock':
                return 'Lose'
            case 'Paper':
                return 'Win'
            case 'Scissors':
                return 'Tie'

def who_wins(fight_result, tool):
    player_two_values = {'Rock' : 1, 'Paper' : 2, 'Scissors' : 3}
    player_two_value = player_two_values[tool]

    match fight_result:
        case 'Win':
            player_two_value += 6
            return player_two_value
        case 'Tie':
            player_two_value += 3
            return player_two_value
        case 'Lose':
            return player_two_value

    # print(player_one_value, player_two_value)

    # if player_two_value > player_one_value:
    #     player_two_value += 6
    #     return player_two_value
    # elif player_two_value < player_one_value:
    #     return player_two_value
    # else:
    #     player_two_value += 3
    #     return player_two_value

with open('input.txt') as file:
    lines = file.readlines()

for round in lines:
    round = round.strip('\n')
    # print(round)
    a, b = round.split()
    print(a, b)
    player_one_shape = determine_shape(a)
    player_two_shape = determine_shape(b)
    fight_outcome = fight(player_one_shape, player_two_shape)
    player_two_value = who_wins(fight_outcome, player_two_shape)
    scores.append(player_two_value)
    counter +=1

# print(scores)
total = sum(scores)

print(total)
print(counter)