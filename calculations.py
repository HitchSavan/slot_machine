from random import randrange, shuffle
from copy import deepcopy
import numpy as np
from progressbar import progressbar

symbols = [1, 2, 3, 4, 5, 6, 7, 8]
wild = 'W'

wild_combo = True
no_output = False

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

    while(True):
        success = drum_sorting(pre_drums)
        if success:
            break

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

    for i in range(100):
        if not wild_combo:
            tuned_drums[randrange(4)].append(symbols[randrange(5)])
        else:
            tuned_drums[randrange(4)].append(symbols[randrange(5)])

        win_payment, ret_perc, win_chance = calculate_line_stats(symbols, wins, tuned_drums, wild_combo, payment=1, line=1, no_output=True, wild=-1)
        
        if ret_perc < 93:
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
        top = randrange(len(drum))
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
    win_payment, ret_perc, win_chance = calculate_line_stats(symbols, wins, pre_drums, wild_combo, payment=1, line=i, no_output=no_output, wild=wild)
    total_chance += win_chance
    total_win_payment += win_payment
print(f"Total win chance on every line (Hit): {total_chance}",
    f"Total win payment: {total_win_payment}",
    f"Total return percentage: {round((total_win_payment / payment) * 100, 2)}%", sep="\n")
'''
tests_quantity = 300000
print(f"Running {tests_quantity} spins...")
ret_perc = []
for i in range(tests_quantity):
    win_summ = 0
    res = roll(pre_drums, wild, lines, no_output)

    for w in res:
        win_summ += wins[w][res[w]]

    ret_perc.append((win_summ / 5) * 100)

    progressbar(tests_quantity, i)

print()
print(f"Mean of return percentage: {round(np.mean(np.array(ret_perc)), 2)}%")
print(f"Hit: {round((len(ret_perc) - ret_perc.count(0)) / len(ret_perc), 2)}")
print(f"STD of return percentage of every game: {round(np.std(np.array(ret_perc)), 2)}%")
print(f"STD of return percentage (target difference): {round(abs(np.mean(np.array(ret_perc)) - (total_win_payment / payment) * 100) / 3, 2)}%")
'''

'''
for i in range(100):
    tuned_drums, ret_perc = bruteforce(drums)
    if ret_perc > 91.95 and ret_perc < 92.10:
        break
print(f"Drums: {tuned_drums}")
'''