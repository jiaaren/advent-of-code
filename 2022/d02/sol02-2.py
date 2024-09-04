with open('input.txt') as f:
    file = f.read()

pairs = [x.split(' ') for x in file.split('\n')]


me_dict = {
    'X': 0, # lose
    'Y': 3, # draw
    'Z': 6  # win
}

score_dict = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3  # scissors
}

tot_score = 0

def get_choice(opp_choice, score):
    if score == 3:
        return opp_choice
    if opp_choice == 'A':
        if score == 0:
            return 'C'
        else:
            return 'B'
    if opp_choice == 'B':
        if score == 0:
            return 'A'
        else:
            return 'C'
    if opp_choice == 'C':
        if score == 0:
            return 'B'
        else:
            return 'A'

for opp, me in pairs:
    outcome_score = me_dict[me]
    my_choice = get_choice(opp, outcome_score)
    my_choice_score = score_dict[my_choice]

    round_score = outcome_score + my_choice_score

    tot_score += round_score

print(tot_score)