scores = []
total = 0
counter = 0
def determine_shape(letter_value):
    player_shape_values = {'A' : 'Rock', 'B' : 'Paper', 'C' : 'Scissors'}

    return player_shape_values[letter_value]

def determine_outcome(letter_value):
    win_values = {'X' : 'Lose', 'Y' : 'Tie', 'Z' : 'Win'}

    return win_values[letter_value]

def determine_second_value(first_player, needed_outcome):
    if first_player == 'Rock':
        match needed_outcome:
            case 'Lose':
                return 'Scissors'
            case 'Tie':
                return 'Rock'
            case 'Win':
                return 'Paper'
    if first_player == 'Paper':
        match needed_outcome:
            case 'Lose':
                return 'Rock'
            case 'Tie':
                return 'Paper'
            case 'Win':
                return 'Scissors'
    else:
        match needed_outcome:
            case 'Lose':
                return 'Paper'
            case 'Tie':
                return 'Scissors'
            case 'Win':
                return 'Rock'

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

with open('input.txt') as file:
    lines = file.readlines()

for round in lines:
    round = round.strip('\n')
    a, b = round.split()
    player_one_shape = determine_shape(a)
    outcome_needed = determine_outcome(b)
    player_two_shape = determine_second_value(player_one_shape, outcome_needed)
    fight_outcome = fight(player_one_shape, player_two_shape)
    print(f"{player_one_shape} vs. {player_two_shape}, second player {fight_outcome}")
    player_two_value = who_wins(fight_outcome, player_two_shape)
    scores.append(player_two_value)
    counter +=1

# print(scores)
total = sum(scores)

print(total)
print(counter)