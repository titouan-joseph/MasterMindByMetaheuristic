import random
import statistics
import copy
from typing import List

BLACK = "black"
WHITE = "white"
YELLOW = "yellow"
RED = "red"
PURPLE = "purple"
GREEN = "green"
BLUE = "blue"
ORANGE = "orange"

COLORS = [BLACK, WHITE, YELLOW, RED, PURPLE, GREEN, BLUE, ORANGE]


class Ball:
    def __init__(self, color):
        self.color = color
        self.tryCount = 0
        self.isWellPlaced = False
        self.isColorCorrect = False

    def __str__(self):
        return self.color

    def __eq__(self, other):
        return self.color == other.color
    
    def __repr__(self):
        return str(self)


class Board:
    def __init__(self, solution):
        self.list = []  # jeu actuel, contenant des balls
        self.solution = solution
        self.tryCount = 0  # number of trys
        self.history = []
        self.maxTry = 10

    def fillRandomly(self):
        for _ in range(4):
            self.list.append(random.choice(COLORS))
        return self

    def getGameState(self):
        # state = []
        # for i in len(self.list):
        # if self.list[i] != self.solution[i] :
        raise NotImplementedError

    def fitness(self, current_candidate):
        # return statistics.mean([eval(current_candidate, story) for story in self.history])
        results = 0
        for story in self.history:
            results += eval(current_candidate, story)
        if len(self.history) == 0:
            return results
        else:
            return results / len(self.history)

    def jumpingJack(self, current_candidate):
        print("🏃‍ 🏃‍ 🏃️ 🏃‍ 🏃‍ 🏃️")
        self.fitness(current_candidate)

    def geneticSolution(self):
        self.fillRandomly()
        scores = self.getScore()
        toBeTestedList = self.list

        while self.getScore(toBeTestedList) < scores:
            toBeTestedList = self.permutation(self.list)

        # On aura un meilleur score

    def permutation(self, list):
        tmp = list
        random.shuffle(tmp)
        return tmp

    def get_pm(self, list=None):
        if list is None:
            list = self.list
        # if type(list) == Board:
        #     list = list.list
        return compare(list, SOLUTION)

    def getScore(self, list=None):
        if list is None:
            list = self.list
        return score(*self.get_pm(list))
    
    def __str__(self):
        return str(self.list)
    
    def __repr__(self):
        return str(self)


def eval(current_candidate, previous_candidate):
    previous_pm = compare(previous_candidate, SOLUTION)
    virtual_pm = compare(current_candidate, previous_candidate)

    return abs(score(*previous_pm) - score(*virtual_pm))


def score(p, m):
    """
    :param p: number of correctly placed colors
    :param m: number of misplaced colors, but still correct
    :return: the current game score
    """
    return (p ) * WEIGHT_P + (m ) * WEIGHT_M


def compare(c1, c2):
    """
    :param c1: candidate solution list of balls
    :param c2: target solution list of balls
    :return: p and m
    """
    p, m = 0, 0
    for index, ball in enumerate(c1):
        # print('[DEBUG]', type(ball))
        # print('[DEBUG]', type(c2[index]))
        ball = Ball(ball)
        if ball == c2[index]:
            p += 1
        elif ball in c2:
            m += 1
    return p, m

def get_m_candidats(proposals: List[Board], NUM_SELECTED):
    """
    :param proposals: the candidates solution list
    :param NUM_SELECTED: the maximum of solution selected
    :return: the NUM_SELECTED best proposals, associated with their fitness
    """
    best = []
    out = []
    # Computing fitness values of the candidates
    for elem in proposals:
        fit = elem.fitness(elem.list)
        best.append((fit, elem))
    # Sorting the fitness values computed, according to their fitness
    best.sort(key=lambda tup: tup[0], reverse=True)
    # Selecting the final best elements (appart from the null values)
    i = 0
    for val in range(len(best)):
        if i < NUM_SELECTED and best[i] != 0:
            out.append(best[val][1])
            i += 1
    # WARNING CAN RETURN NULL
    return out


def proposal_mutation(proposal: Board):
    """
    :param proposal: the candidate solution
    :return: the mutated solution
    """
    # Chose randomly a given index to swap the value
    random_index = random.randint(0, len(proposal.list)-1)
    current_color = proposal.list[random_index]
    color_candidate = copy.deepcopy(COLORS)
    color_candidate = [color for color in color_candidate if color != current_color] 
    random_color = random.choice(color_candidate)
    proposal.solution[random_index].color = random_color
    return proposal


def population_mutation(proposals):
    """
    :param proposal: list the candidate solution
    :return: the mutated solution list
    """
    for elem in proposals:
        elem = proposal_mutation(elem)
    return proposals


def proposal_generation(p1: Board, p2: Board):
    # Choses from both parents to generate a child proposal
    # Uses random indexes not to be influenced
    out = []
    mBoard = Board(SOLUTION)
    for index in range(len(p1.list)):
        propability = random.random()
        
        if propability > 0.5:
            out.append(p1.list[index])
        else:
            out.append(p2.list[index])
    
    mBoard.list = out
    mBoard.history += p1.history
    mBoard.history += p2.history
    return mBoard

def get_next_generation(proposals: List[Board]):
    res = []
    for index, proposal in enumerate(proposals):
        if index != len(proposals) - 1:
            res.append(proposal_generation(proposal, proposals[index + 1]))
    random.shuffle(res)
    return res
            


def geneticSolution(board, proposals):
    won = False
    while  board.tryCount <= board.maxTry:
        proposals = population_mutation(proposals)
        proposals = get_m_candidats(proposals, len(proposals) / 2)
        proposals = get_next_generation(proposals)
        #board.history.append(proposals)
        board.tryCount += 1
        
        for proposal in proposals: 
            if proposal.getScore() == 100:
                print("🥳 solution found ", proposal)
                break 
            
        print("Proposal : ", proposals)
    if board.tryCount < board.maxTry: 
        won = True
        print("Game ended with " + board.tryCount+ " attempts. The solution was : ")
        print(board.list)
    else : 
        print("WARNING You lost !")
        print("Your score is", proposals[0].getScore(), " %")
    return won 

if __name__ == '__main__':
    
    NUM_SELECTED = 100 # Number of selected values for the fitness choice
    WEIGHT_P = 25
    WEIGHT_M = 12.5
    FIRST_GENERERATION_POPULATION = 8000
    BALLS_COUNT = 4


    # Pawns initialisation before starting the game
    SOLUTION = [Ball(random.choice(COLORS)) for _ in range(BALLS_COUNT)]
    first_proposal_set = [Board(SOLUTION) for _ in range(FIRST_GENERERATION_POPULATION)]
    first_proposal_set = list(map(lambda x: x.fillRandomly(), first_proposal_set))
    print("Solution : ", SOLUTION)
    mBoard = Board(SOLUTION)
    geneticSolution(mBoard, first_proposal_set)
    print("Solution : ", SOLUTION)
