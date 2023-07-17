#include <iostream>
#include <fstream>
#include <vector>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include <map>
#include <tuple>
#include <sstream>
#include <numeric>
#include <algorithm>

double mean(std::vector<double>& v) {
    if (v.empty()) {
        return 0;
    }
    return std::reduce(v.begin(), v.end()) / v.size();
}

double stdiv(std::vector<double>& v) {
    double sq_sum = std::inner_product(v.begin(), v.end(), v.begin(), 0.0);
    double stdev = std::sqrt(sq_sum / v.size() - mean(v) * mean(v));
    return stdev;
}

struct DrumCell {
    DrumCell* prev = nullptr;
    DrumCell* next = nullptr;
    std::string symbol;
};


class Drum {
    public:
        Drum(std::vector<char>& drumList) {
            for (char s : drumList) {
                appendNode(s);
            }
        }

        ~Drum() {
            removeNodes();
        }

        int count(std::string s) {
            int count = 0;
            DrumCell* p;
            p = this->head;
            do {
                if (s == p->symbol) {
                    count++;
                }
                p = p->next;
            } while (p != this->head);
            return count;
        }

        void removeNodes() {
            removeNode(this->head);
            this->head = nullptr;
            this->quantity = 0;
        }

        void removeNode(DrumCell* p) {
            if (p->next != this->head) {
                removeNode(p->next);
            }
            delete p;
        }

        void printOut() {
            DrumCell* p = this->head;
            
            do {
                std::cout << p->symbol << " ";
                p = p->next;
            } while (p != this->head);
        }

        void appendNode(char s) {
            DrumCell* p;
            DrumCell* tmp;
            p = new DrumCell;

            if (this->quantity == 0) {
                this->head = p;
                p->next = p;
                p->prev = p;
            } else {
                tmp = this->head->prev;
                this->head->prev = p;
                p->next = this->head;
                tmp->next = p;
                p->prev = tmp;
            }

            this->quantity++;

            p->symbol = s;
        }

        std::string& operator[](int index) {
            DrumCell* p;
            p = this->head;
            for (int i = 0; i < index; i++) {
                p = p->next;
            }
            return p->symbol;
        }

        int size() {
            return this->quantity;
        }

    private:
        DrumCell* head = nullptr;
        int quantity = 0;
};


class SlotMachine {
    public:
        SlotMachine(std::string filename) {
            std::vector<std::vector<char>> drums;
            std::vector<char> drum;
            std::map<std::string, std::map<int, int>> winTable;
            std::vector<std::string> symbols;
            std::vector<std::vector<std::vector<int>>> winLines;
            std::vector<std::vector<int>> winLine;
            std::vector<int> lineCoords;

            std::ifstream configFile(filename);

            std::string line, str;
            char wild;
            int s, trials;

            srand(time(NULL));

            if (configFile.is_open()) {
                std::getline(configFile, line);
                wild = line[0];

                while (std::getline(configFile, line) && line != "win_table") {
                    for (auto a : line)
                        if (a != ' ')
                            drum.push_back(a);
                    drums.push_back(drum);
                    drum.clear();
                }

                std::getline(configFile, line);
                std::stringstream ss(line);
                while (getline(ss, str, ' '))
                    symbols.push_back(str);
                int i;
                while (std::getline(configFile, line) && line != "lines") {
                    std::stringstream ss(line);
                    i = -1;
                    while (getline(ss, str, ' ')) {
                        if (i == -1) {
                            s = stoi(str);
                        } else {
                            winTable[symbols[i]][s] = stoi(str);
                        }
                        i++;
                    }
                }

                while (std::getline(configFile, line) && line != "trials") {
                    std::stringstream ss(line);
                    i = 0;
                    while (getline(ss, str, ' ')) {
                        lineCoords.push_back(stoi(str));
                        i++;
                        if (i > 1) {
                            i = 0;
                            winLine.push_back(lineCoords);
                            lineCoords.clear();
                        }
                    }
                    winLines.push_back(winLine);
                    winLine.clear();
                }

                std::getline(configFile, line);
                trials = stoi(line);

                this->setConfig(wild, drums, winTable, winLines, trials);

            } else {
                std::cout << "Cant open config file";
            }
        }

        ~SlotMachine() {
            for (Drum* drum : this->drums) {
                delete drum;
            }
        }

        void printOutDrums() {
            for (Drum* drum : this->drums) {
                drum->printOut();
                std::cout << std::endl;
            }
        }

        void printOutWinTable() {
            std::vector<int> winSets;
            std::cout << "Symbols: ";

            for (auto const& [symbol, winSet] : this->winTable) {
                std::cout << symbol << " ";
            }
            for (auto const& [symbol, winSet] : this->winTable) {
                for (auto const& [set, sum] : winSet) {
                    winSets.push_back(set);
                }
                break;
            }
            for (int i : winSets) {
                std::cout << std::endl << i << " in row: ";
                for (auto const& [symbol, winSet] : this->winTable) {
                    std::cout << this->winTable[symbol][i] << " ";
                }
            }
            std::cout << std::endl;
        }

        void printOutWinLines() {
            char outMatrix[3][5];
            int l = 1;
            for (auto line : this->winLines) {
                std::cout << "Line " << l++ << ": " << std::endl;
                for (auto coords : line) {
                    outMatrix[coords[0]][coords[1]] = 'X';
                }
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 5; j++) {
                        if (outMatrix[i][j] != 'X') {
                            std::cout << "O ";
                        } else {
                            outMatrix[i][j] = 'O';
                            std::cout << "X ";
                        }
                    }
                    std::cout << std::endl;
                }
            }
        }

        void printOut() {
            std::cout << "Drums: " << std::endl;
            this->printOutDrums();
            std::cout << "Win table: " << std::endl;
            this->printOutWinTable();
            std::cout << "Win lines: " << std::endl;
            this->printOutWinLines();
        }
        

        void calcilateStats() {
            double totalChance = 0;
            double totalWinPayment = 0;
            for (int i = 0; i < this->winLines.size(); i++) {
                auto [winPayment, retPerc, winChance] = calculateLineStat(i);
                totalChance += winChance;
                totalWinPayment += winPayment;
            }
            std::cout << "_______________________________________________" << std::endl << "Total win chance on every line (Hit): " << totalChance << std::endl << "Total win payment: " << totalWinPayment << std::endl << "Total return percentage: " << (totalWinPayment / (this->payment * winLines.size())) * 100 << "%";
        }

        std::map<std::string, int> roll() {
            std::vector<std::vector<std::string>> outMatrix(3);
            int top;
            for (Drum* drum : this->drums) {
                top = rand() % drum->size();
                outMatrix[0].push_back((*drum)[top]);
                outMatrix[1].push_back((*drum)[top + 1]);
                outMatrix[2].push_back((*drum)[top + 2]);
            }

            std::map<std::string, int> result = checkWin(outMatrix);

            if (result.empty() && this->winstreak) {
                this->winstreakTime.push_back(this->winstreak);
                this->winstreak = 0;
            } else {
                this->winstreak++;
            }

            if (this->trials == 1) {
                std::cout << std::endl;
                for (int i = 0; i < outMatrix.size(); i++) {
                    for (int j = 0; j < outMatrix[i].size(); j++) {
                        std::cout << outMatrix[i][j] << " ";
                    }
                    std::cout << std::endl;
                }

                if (result.empty()) {
                    std::cout << "You lose :(" << std::endl;
                } else {
                    double winSum = 0;
                    for (auto [s, num] : result) {
                        winSum += this->winTable[s][num];
                    }
                    std::cout << "You win " << winSum << "!" << std::endl;
                }
            }

            return result;
        }

        void gambleTrials() {
            std::vector<double> trialSTDs;
            for (int j = 0; j < this->trialsNums; j++) {
                std::cout << std::endl << "Running " << this->trials <<" spins..." << std::endl;
                std::vector<double> retPerc;
                for (int i = 0; i < this->trials; i++) {
                    double winSumm = 0;
                    std::map<std::string, int> res = roll();

                    for (auto [s, nums] : res)
                        winSumm += this->winTable[s][nums];

                    retPerc.push_back((winSumm / 5) * 100);
                    std::cout << round(double(i) * 100 / this->trials) << "%" << "\r";
                }
                trialSTDs.push_back(abs(mean(retPerc) - 92) / 3);
                std::cout << std::endl << "Mean of return percentage: " << mean(retPerc) << "%" << std::endl << "Hit: " << double(retPerc.size() - std::count(retPerc.begin(), retPerc.end(), 0)) / retPerc.size() << std::endl << "STD of return percentage of every game: " << stdiv(retPerc) << "%" << std::endl << "STD of return percentage (target difference): " << trialSTDs.back() << "%" << std::endl;
                
            }
            std::cout << "Mean of STD of " << trialsNums << " trials of " << trials << ": " << mean(trialSTDs) << "%";
            if (this->winstreak) {
                this->winstreakTime.push_back(this->winstreak);
                this->winstreak = 0;
            }
            std::cout << std::endl << "Mean number of wins in a row: " << mean(this->winstreakTime);
        }

        void setTrials(int lenght) {
            this->trials = lenght;
        }

    private:
        std::vector<Drum*> drums;
        std::vector<std::string> symbols;
        std::string wild = "W";
        int rolls = 1;
        std::map<std::string, std::map<int, int>> winTable;
        std::vector<std::vector<std::vector<int>>> winLines;
        bool wildCombo = false;
        int payment = 1;
        int trials = 1;
        int trialsNums = 1;
        int winstreak = 0;
        std::vector<double> winstreakTime;

        void setConfig(char wild,
                std::vector<std::vector<char>>& drums,
                std::map<std::string, std::map<int, int>>& winTable,
                std::vector<std::vector<std::vector<int>>>& winLines,
                int trials) {
            Drum* drumP;
            this->wild = wild;
            for (std::vector<char> drum : drums) {
                drumP = new Drum(drum);
                this->drums.push_back(drumP);
            }

            this->winTable = winTable;
            this->winLines = winLines;
            this->trials = trials;
        }

        std::tuple<double, double, double> calculateLineStat(int line) {
            double winPayment = 0;
            double winChance = 0;
            for (auto [s, win] : this->winTable) {
                if (!wildCombo && s == this->wild)
                    continue;
                for (auto [nums, pay] : win) {
                    double chance = 1;
                    int j = 0;
                    for (auto drum : drums) {
                        double duplicates = drum->count(s) + (s == this->wild ? 0 : drum->count(this->wild));
                        if (j < nums)
                            chance *= duplicates / drum->size();
                        else
                            chance *= (drum->size() - duplicates) / drum->size();
                        j++;
                    }
                    winPayment += chance * pay;
                    winChance += chance;
                    std::cout << "Chances of " << s << " occurs " << nums << " times on line " << line+1 << ": " << chance << ", with payment " << chance * pay << std::endl;;
                }
            }
            double retPerc = winPayment * 100 / this->payment;
            std::cout << "Mean win payment: " << winPayment << std::endl << "Return percentage: " << retPerc << "%" << std::endl << "Win chances: " << winChance << std::endl;
            return {winPayment, retPerc, winChance};
        }

        std::map<std::string, int> checkWin(std::vector<std::vector<std::string>>& outMatrix) {
            std::map<std::string, int> linesWins;
            for (auto line : this->winLines) {
                std::string symbol = outMatrix[line[0][0]][line[0][1]];
                for (int i = 1; i < 5; i++) {
                    if (symbol == this->wild)
                        symbol = outMatrix[line[i][0]][line[i][1]];
                    else
                        break;
                }
                if ((symbol == outMatrix[line[1][0]][line[1][1]] || outMatrix[line[1][0]][line[1][1]] == wild) && (symbol == outMatrix[line[2][0]][line[2][1]] || outMatrix[line[2][0]][line[2][1]] == wild)) {
                    linesWins[symbol] = 3;
                    if (symbol == outMatrix[line[3][0]][line[3][1]] || outMatrix[line[3][0]][line[3][1]] == wild) {
                        linesWins[symbol] += 1;
                        if (symbol == outMatrix[line[4][0]][line[4][1]] || outMatrix[line[4][0]][line[4][1]] == wild) 
                            linesWins[symbol] += 1;
                    }
                }
            }

            return linesWins;
        }
};


int main() {
    
    SlotMachine* machine = new SlotMachine("config.txt");

    machine->printOut();
    machine->calcilateStats();
    
    std::vector<int> trials = {10000, 50000, 100000, 300000, 1000000};

    for (auto t : trials) {
        machine->setTrials(t);
        machine->gambleTrials();
    };

    return 0;
}