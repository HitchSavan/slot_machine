from random import randrange, shuffle, uniform
from copy import deepcopy
import numpy as np
from progressbar import progressbar

symbols = [1, 2, 3, 4, 5, 6, 7, 8]
wild = 'W'

theorethical_drums = False
wild_combo = False
tune = False
target_ret_percentage = 87
needed_ret_percentage = 92
trial = 300000

if wild_combo:
    symbols[-1] = wild
else:
    symbols.append(wild)

wins = {
    symbols[0]: {
        3: 3,
        4: 15,
        5: 45
    },
    symbols[1]: {
        3: 5,
        4: 30,
        5: 75
    },
    symbols[2]: {
        3: 7,
        4: 50,
        5: 150
    },
    symbols[3]: {
        3: 9,
        4: 60,
        5: 250
    },
    symbols[4]: {
        3: 12,
        4: 75,
        5: 350
    },
    symbols[5]: {
        3: 15,
        4: 90,
        5: 500
    },
    symbols[6]: {
        3: 20,
        4: 120,
        5: 750
    },
    symbols[7]: {
        3: 30,
        4: 150,
        5: 1000
    }
}

drums = [
    [
        symbols[0],
        symbols[1],
        symbols[2],
        symbols[3],
        symbols[4],
        symbols[5],
        symbols[6],
        symbols[7]
    ],
    [
        symbols[0],
        symbols[1],
        symbols[2],
        symbols[3],
        symbols[4],
        symbols[5],
        symbols[6],
        symbols[7]
    ],
    [
        symbols[0],
        symbols[1],
        symbols[2],
        symbols[3],
        symbols[4],
        symbols[5],
        symbols[6],
        symbols[7]
    ],
    [
        symbols[0],
        symbols[1],
        symbols[2],
        symbols[3],
        symbols[4],
        symbols[5],
        symbols[6],
        symbols[7]
    ],
        [
        symbols[0],
        symbols[1],
        symbols[2],
        symbols[3],
        symbols[4],
        symbols[5],
        symbols[6],
        symbols[7]
    ]
]


lines = [
    [
        (1, 0),
        (1, 1),
        (1, 2),
        (1, 3),
        (1, 4)
    ],
    [
        (0, 0),
        (0, 1),
        (0, 2),
        (0, 3),
        (0, 4)
    ],
    [
        (2, 0),
        (2, 1),
        (2, 2),
        (2, 3),
        (2, 4)
    ],
    [
        (0, 0),
        (1, 1),
        (2, 2),
        (1, 3),
        (0, 4)
    ],
    [
        (2, 0),
        (1, 1),
        (0, 2),
        (1, 3),
        (2, 4)
    ]
]

if not wild_combo:
    for drum in drums[1:]:
        drum.append(wild)

payment = 5

if theorethical_drums:
    # for theorethical
    if not wild_combo:
        pre_drums = [
            [1, 4, 3, 5, 4, 2, 7, 8, 2, 6, 4, 3],
            [3, 8, 7, 3, 1, 2, 5, 1, 3, 6, 1, 4, wild, 5],
            [2, 7, 5, 1, 8, 2, 1, 4, 3, wild, 5, 6, 4, 5],
            [5, 3, 4, 1, wild, 2, 6, 5, 3, 7, 1, 4, 8],
            [5, 4, 8, 7, 1, 3, wild, 6, 2]
        ]
        pass
    else:
        pre_drums = [
            [3, 2, 4, 3, 5, 6, 7, wild, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 1, 3, 4, 1],
            [2, 1, 3, 4, 5, 6, 7, wild, 3, 2, 5, 3, 2, 4, 3, 2, 5, 4, 3, 5, 4, 2, 1, 5, 2, 1, 5],
            [1, 5, 3, 1, 7, 6, 1, wild, 4, 5, 1, 4, 2, 3, 4, 1, 3, 4, 1, 3, 4, 1, 5, 3, 1, 2, 4, 1, 2, 4],
            [1, 4, 3, 1, 4, 5, 1, 6, 7, 1, wild, 3, 1, 2, 3, 1, 4, 2, 1, 5, 3, 1, 4, 3, 1, 2, 5, 1, 4, 2],
            [1, 2, 3, 4, 5, 6, 7, wild]
        ]
        pass
else:
    # for practice
    if not wild_combo:
        pre_drums = [
            [8, 4, 1, 3, 6, 1, 5, 4, 1, 3, 4, 1, 6, 5, 2, 7, 5, 1, 2, 5, 1, 4, 5, 1, 4, 5, 2, 3, 5, 2, 1, 5],
            [5, 3, 2, 5, 4, 2, 5, 6, 2, 5, 4, 6, 5, 1, 6, 5, 4, 6, 5, 1, 6, 5, 8, 4, 6, 1, wild, 5, 6, 2, 5, 7, 6, 5, 2, 3, 6, 2, 3, 1, 2, 3, 5, 2, 3, 5, 2, 1, 5, 4, 2, 5, 3, 2],
            [wild, 5, 2, 3, 5, 2, 1, 5, 2, 6, 5, 3, 2, 1, 4, 3, 2, 4, 5, 2, 3, 4, 7, 3, 1, 4, 3, 1, 5, 4, 2, 5, 4, 6, 5, 1, 4, 5, 1, 8, 5, 1, 3, 5, 1, 3, 5, 6],
            [2, 3, 4, 5, 2, 4, 1, 5, 4, 6, 2, 1, 5, 3, 2, 8, 6, 4, wild, 6, 4, 2, 7, 4],
            [3, 5, 2, 1, wild, 6, 4, 7, 8]
        ]
        pass
    else:
        pre_drums = [
            [1, 2, 3, wild, 2, 3, 5, 2, 4, 5, 1, 4, 6, 1, 3, 2, 4, 1, 3, 2, 1, 3, 7, 6],
            [2, wild, 3, 2, 4, 3, 2, 4, 3, 7, 4, 3, 2, 5, 4, 2, 1, 3, 2, 5, 1, 2, 4, 1, 5, 4, 1, 6, 4, 5, 6, 4, 1, 2, 6, 5, 4, 6, 5, 4, 3, 1, 4, 3],
            [5, 2, 1, 5, 2, 4, 6, 2, 5, 3, 4, 2, 3, wild, 5, 3, 1, 5, 2, 4, 3, 2, 5, 3, 2, 1, 6, 7, 5, 6, 4, 5, 3, 2, 5, 6, 4, 5, 2, 3],
            [5, 3, 2, 5, 3, 7, 5, 3, 4, 6, 3, 4, 6, 3, 2, 5, 3, 2, 5, wild, 2, 6, 1],
            [4, 2, 5, 6, 7, wild, 3, 1]
        ]
        pass

def drum_sorting(drums):
    success = True
    for drum in drums:
        for first in range(len(drum)):
            if drum[first] == drum[(first + 1) % len(drum)]:
                drum[(first + 1) % len(drum)], drum[(first+3) % len(drum)] = drum[(first+3) % len(drum)], drum[(first + 1) % len(drum)]
                success = False
            if drum[first] == drum[(first + 2) % len(drum)]:
                drum[(first + 2) % len(drum)], drum[(first+3) % len(drum)] = drum[(first+3) % len(drum)], drum[(first + 2) % len(drum)]
                success = False
        print(drum, success)
    return success

def sort_drums(drums):
    for drum in drums:
        shuffle(drum)

    for i in range(500):
        success = drum_sorting(drums)
        if success:
            break
    return success

def calculate_line_stats(symbols, wins, drums, wild_combo, payment, line, no_output, wild):
    win_payment = 0
    win_chance = 0
    for s in symbols:
        if not wild_combo and s == wild:
            continue
        for win in wins[s]:
            chance = 1
            for j, drum in enumerate(drums):
                duplicates = drum.count(s) + (0 if s == wild else drum.count(wild))
                if j < win:
                    chance *= duplicates / len(drum)
                else:
                    chance *= (len(drum) - duplicates) / len(drum)
            win_payment += chance * wins[s][win]
            win_chance += chance
            if not no_output:
                print(f"Chances of {s} occurs {win} times on line {line+1}: {chance}, with payment {chance * wins[s][win]}")
    ret_perc = round(win_payment / payment * 100, 2)
    if not no_output:
        print(f"Mean win payment: {win_payment}", f"Casino salary: {payment - win_payment}",
              f"Return percentage: {ret_perc}%",
              f"Win chances: {win_chance}", sep="\n")
    return (win_payment, ret_perc, win_chance)

def bruteforce(drums):
    
    tuned_drums = deepcopy(drums)

    for i in range(1000):
        if not wild_combo:
            tuned_drums[round(uniform(0, 3))].append(symbols[round(uniform(0, 5))])
        else:
            tuned_drums[round(uniform(0, 3))].append(symbols[round(uniform(0, 5))])

        win_payment, ret_perc, win_chance = calculate_line_stats(symbols, wins, tuned_drums, wild_combo, payment=1, line=0, no_output=True, wild='W')
        print(ret_perc, end=" ")
        if ret_perc < target_ret_percentage+1:
            break
    return tuned_drums, ret_perc

def check_win(matrix, wild, lines):
    lines_wins = {}
    for line in lines:
        symbol = matrix[line[0][0]][line[0][1]]
        for i in range(1, 5):
            if symbol == wild:
                symbol = matrix[line[i][0]][line[i][1]]
            else:
                break

        if (symbol == matrix[line[1][0]][line[1][1]] or matrix[line[1][0]][line[1][1]] == wild) and (symbol == matrix[line[2][0]][line[2][1]] or matrix[line[2][0]][line[2][1]] == wild):
            lines_wins[symbol] = 3
            if symbol == matrix[line[3][0]][line[3][1]] or matrix[line[3][0]][line[3][1]] == wild:
                lines_wins[symbol] += 1
                if symbol == matrix[line[4][0]][line[4][1]] or matrix[line[4][0]][line[4][1]] == wild:
                    lines_wins[symbol] += 1

    return lines_wins

def roll(drums, wild, lines, no_output):
    out_matrix = [[],[],[]]
    for drum in drums:
        top = round(uniform(0, len(drum)-1))
        out_matrix[0].append(drum[top])
        out_matrix[1].append(drum[(top + 1) % len(drum)])
        out_matrix[2].append(drum[(top + 2) % len(drum)])

    if not no_output:
        for row in out_matrix:
            print(row)
        
    return check_win(out_matrix, wild, lines)


total_chance = 0
total_win_payment = 0
for i in range(5):
    win_payment, ret_perc, win_chance = calculate_line_stats(symbols, wins, pre_drums, wild_combo, payment=payment/5, line=i, no_output=True, wild=wild)
    total_chance += win_chance
    total_win_payment += win_payment
print("_______________________________________________",
      f"Total win chance on every line (Hit): {total_chance}",
      f"Total win payment: {total_win_payment}",
      f"Total return percentage: {round((total_win_payment / payment) * 100, 2)}%", sep="\n")


if tune:
    for i in range(100):
        tuned_drums, ret_perc = bruteforce(drums)
        if ret_perc > target_ret_percentage-0.05 and ret_perc < target_ret_percentage+0.05:
            break
    print()
    if not (ret_perc > target_ret_percentage-0.05 and ret_perc < target_ret_percentage+0.05):
        print("Cannot get target return percentage, try again")
    else:    
        print(f"Drums: {tuned_drums}")

        if not sort_drums(tuned_drums):
            print("Cannot generate drums, try again")
        else:
            pre_drums = tuned_drums

if trial:
    trial_STDs = []
    trials_num = 5
    for j in range(trials_num):
        print(f"Running {trial} spins...")
        ret_perc = []
        for i in range(trial):
            win_summ = 0
            res = roll(pre_drums, wild, lines, no_output=True)

            for w in res:
                win_summ += wins[w][res[w]]

            ret_perc.append((win_summ / 5) * 100)

            progressbar(trial, i)

        #trial_STDs.append(round(abs(np.mean(np.array(ret_perc)) - (total_win_payment / payment) * 100) / 3, 2))
        trial_STDs.append(round(abs(np.mean(np.array(ret_perc)) - needed_ret_percentage) / 3, 2))
        print()
        print(f"Mean of return percentage: {round(np.mean(np.array(ret_perc)), 2)}%")
        print(f"Hit: {round((len(ret_perc) - ret_perc.count(0)) / len(ret_perc), 2)}")
        print(f"STD of return percentage of every game: {round(np.std(np.array(ret_perc)), 2)}%")
        print(f"STD of return percentage (target difference): {trial_STDs[-1]}%")
    print(f"Mean of STD of {trials_num} trials of {trial}: {round(np.mean(np.array(trial_STDs)), 2)}%")