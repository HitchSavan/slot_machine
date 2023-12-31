from random import shuffle, uniform
from copy import deepcopy
import numpy as np
from progressbar import progressbar
import os

symbols = [8, 7, 6, 5, 4, 3, 2, 1]
wild = 'W'

theoretical_drums = False
wild_combo = False
generate_drums = False

if wild_combo:
    target_ret_percentage = 92
else:
    target_ret_percentage = 92
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
'''
'''
if not wild_combo:
    for drum in drums[1:]:
        drum.append(wild)

line_payment = 1
payment = len(lines) * line_payment

if theoretical_drums:
    # for theoretical 92%
    if not wild_combo:
        pre_drums = [
            [6, 8, 5, 4, 6, 1, 3, 4, 7, 3, 6, 8, 5, 6, 4, 3, 5, 4, 8, 2],
            [7, wild, 5, 7, 6, 4, 5, 6, 4, 5, 7, 6, 1, 7, 6, 4, 7, 6, 5, 7, 6, 4, 7, 3, 2, 7, 8, 6, 7, 3, 6, 7, 3, 6, 7, 3, 4],
            [6, 4, 5, 6, 8, 5, 1, 8, 5, 4, 6, 3, 7, 5, 8, 7, 4, wild, 6, 5, 4, 6, 5, 2, 7, 6, 4, 5, 6, 7, 8, 5, 7, 4, 3, 6, 4, 5],
            [5, 4, 6, 7, 5, 4, 7, 1, 8, 7, 3, 5, 6, 8, 2, 7, 4, wild, 6],
            [4, wild, 5, 6, 7, 3, 1, 8, 2]
        ]
        pass
    else:
        pre_drums = [
            [6, 7, 5, 6, 4, 3, 2, wild, 5, 8, 7, 6, 5, 4, 8, 7, 6, 5, 8, 6, 5, 8],
            [7, 8, 6, 5, 4, 3, 2, wild, 6, 7, 4, 6, 7, 5, 6, 7, 4, 5, 6, 4, 5, 7, 8, 4, 7, 8, 4],
            [8, 4, 6, 8, 2, 3, 8, wild, 5, 4, 8, 5, 7, 6, 5, 8, 6, 5, 8, 6, 5, 8, 4, 6, 8, 7, 5, 8, 7, 5],
            [8, 5, 6, 8, 5, 4, 8, 3, 2, 8, wild, 6, 8, 7, 6, 8, 5, 7, 8, 4, 6, 8, 5, 6, 8, 7, 4, 8, 5, 7],
            [8, 7, 6, 5, 4, 3, 2, wild]
        ]
        pass
else:
    # for practical 92%
    if not wild_combo:
        pre_drums = [
            [1, 3, 8, 5, 6, 4, 7, 6, 4, 2, 8, 4],
            [8, 5, wild, 2, 5, 1, 3, 4, 5, 6, 4, 7, 6, 4, 3, 6, 7, 5, 3],
            [8, 5, 1, 6, 7, 5, 6, 8, 2, 4, 3, wild, 5, 6, 3, 5, 7],
            [4, 6, 7, 4, 8, 3, 4, 2, 5, 7, 1, 5, wild, 7],
            [7, 4, 1, 3, 2, 6, 8, 5, wild]
        ]
        pass
    else:
        pre_drums = [
            [8, 7, 6, wild, 7, 6, 4, 7, 5, 4, 8, 5, 3, 8, 6, 7, 5, 8, 6, 7, 8, 6, 2, 3],
            [7, wild, 6, 7, 5, 6, 7, 5, 6, 2, 5, 6, 7, 4, 5, 7, 8, 6, 7, 4, 8, 7, 5, 8, 4, 5, 8, 3, 5, 4, 3, 5, 8, 7, 3, 4, 5, 3, 4, 5, 6, 8, 5, 6],
            [4, 7, 8, 4, 7, 5, 3, 7, 4, 6, 5, 7, 6, wild, 4, 6, 8, 4, 7, 5, 6, 7, 4, 6, 7, 8, 3, 2, 4, 3, 5, 4, 6, 7, 4, 3, 5, 4, 7, 6],
            [4, 6, 7, 4, 6, 2, 4, 6, 5, 3, 6, 5, 3, 6, 7, 4, 6, 7, 4, wild, 7, 3, 8],
            [5, 7, 4, 3, 2, wild, 6, 8]
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
    win_payment = []
    win_chance = []
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
                    chance *= (len(drum) - duplicates) / (len(drum) - ((len(drum) - duplicates) / len(drum)))

            win_payment.append(chance * wins[s][win])
            win_chance.append(chance)

            if not no_output:
                print(f"Chances of {s} occurs {win} times on line {line+1}: {chance}, with payment {chance * wins[s][win]} (for {wins[s][win]})")
    
    ret_perc = np.sum(win_payment) / payment * 100
    if not no_output:
        print(f"Mean win payment: {np.sum(win_payment)}", f"Casino salary: {payment - np.sum(win_payment)}",
              f"Return percentage: {round(ret_perc, 2)}%",
              f"Win chances: {np.sum(win_chance)}", sep="\n")
    return (np.sum(win_payment), ret_perc, np.sum(win_chance))

def bruteforce(drums):
    
    tuned_drums = deepcopy(drums)

    for i in range(1000):
        if not wild_combo:
            tuned_drums[round(uniform(0, 3))].append(symbols[round(uniform(0, 5))])
        else:
            tuned_drums[round(uniform(0, 3))].append(symbols[round(uniform(0, 5))])

        win_payment, ret_perc, win_chance = calculate_line_stats(symbols, wins, tuned_drums, wild_combo, payment=line_payment, line=0, no_output=True, wild='W')
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
            if 3 in wins[symbol]:
                lines_wins[symbol] = 3
            if symbol == matrix[line[3][0]][line[3][1]] or matrix[line[3][0]][line[3][1]] == wild:
                if 4 in wins[symbol]:
                    lines_wins[symbol] = 4
                if symbol == matrix[line[4][0]][line[4][1]] or matrix[line[4][0]][line[4][1]] == wild:
                    if 5 in wins[symbol]:
                        lines_wins[symbol] = 5
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


total_chance = []
total_win_payment = 0
for i in range(len(lines)):
    win_payment, ret_perc, win_chance = calculate_line_stats(symbols, wins, pre_drums, wild_combo, payment=line_payment, line=i, no_output=True, wild=wild)
    total_chance.append(win_chance)
    total_win_payment += win_payment
print("_______________________________________________",
      f"Total win chance on every line (Hit): {sum(total_chance)}",
      f"Total win payment: {total_win_payment}",
      f"Total return percentage: {round((total_win_payment / payment) * 100, 2)}%", sep="\n")

theoretical_ret_perc = ret_perc

if generate_drums:
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
    theor_trial_STDs = []
    trials_num = 5
    for j in range(trials_num):
        print(f"Running {trial} spins...")
        ret_perc = []
        for i in range(trial):
            win_summ = 0
            res = roll(pre_drums, wild, lines, no_output=(False if trial == 1 else True))

            for w in res:
                win_summ += wins[w][res[w]]

            ret_perc.append((win_summ / payment) * 100)

            progressbar(trial, i)

        #trial_STDs.append(round(abs(np.mean(np.array(ret_perc)) - (total_win_payment / payment) * 100) / 3, 2))
        trial_STDs.append(round(abs(np.mean(np.array(ret_perc)) - needed_ret_percentage) / 3, 2))
        theor_trial_STDs.append(round(abs(np.mean(np.array(ret_perc)) - theoretical_ret_perc) / 3, 2))
        print()
        print(f"Mean of return percentage: {round(np.mean(np.array(ret_perc)), 2)}%")
        print(f"Hit: {(len(ret_perc) - ret_perc.count(0)) / len(ret_perc)}")
        print(f"STD of return percentage of every game: {round(np.std(np.array(ret_perc)), 2)}%")
        print(f"STD of return percentage (target 92% difference): {trial_STDs[-1]}%")
        print(f"STD of return percentage (theoretical {theoretical_ret_perc} difference): {theor_trial_STDs[-1]}%")
    print(f"Mean of STD of {trials_num} trials of {trial}: {round(np.mean(np.array(trial_STDs)), 2)}%")

save_path = f"{os.getcwd()}\\output"
if not os.path.exists(save_path):
    os.makedirs(save_path)

with open(f"{save_path}\\config.txt", "w") as file:
    file.write(f"{wild} ")
    for line in pre_drums:
        file.write("\n")
        for s in line:
            file.write(f"{s} ")
    file.write("\nwin_table\n")
    for symbol in wins:
        file.write(f"{symbol} ")
    for win_num in list(wins[list(wins.keys())[0]]):
        file.write(f"\n{str(win_num)} ")
        for symbol in wins:
            file.write(f"{wins[symbol][win_num]} ")
    file.write("\nlines")
    for line in lines:
        file.write("\n")
        for coords in line:
            for coord in coords:
                file.write(f"{coord} ")
    file.write(f"\ntrials\n{1}")