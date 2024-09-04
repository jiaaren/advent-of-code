with open('input.txt') as f:
    file = f.read()

pairs = [x.split(' ') for x in file.split('\n')]
score = []

me_dict = {
    'X': 'A', # rock
    'Y': 'B', # paper
    'Z': 'C'  # scissors
}

score_dict = {
    'A': 1, # rock
    'B': 2, # paper
    'C': 3  # scissors
}


def eval(opp_choice, me_choice):
    if opp_choice == me_choice:
        return 3
    if me_choice == 'A':
        if opp_choice == 'B':
            return 0
        else:
            return 6
    elif me_choice == 'B':
        if opp_choice == 'C':
            return 0
        else:
            return 6
    elif me_choice == 'C':
        if opp_choice == 'A':
            return 0
        else:
            return 6

tot_score = 0

for opp, me in pairs:
    me_translated = me_dict[me]
    choice_score  = score_dict[me_translated]
    match_score = eval(opp, me_translated)
    round_score = choice_score + match_score
    # print(choice_score, match_score, round_score)

    tot_score += round_score

print(tot_score)