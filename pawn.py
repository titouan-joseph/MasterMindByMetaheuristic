import random
import statistics

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
        self.maxTry = 10

    def __str__(self):
        return self.color

    def __eq__(self, other):
        return self.color == other.color


class Board:
    def __init__(self, solution):
        self.list = []
        self.solution = solution
        self.tryCount = 0  # number of trys
        self.history = []

    def fillRandomly(self):
        for _ in range(4):
            self.list.append(random.choice(COLORS))

    def isGameFinished(self):
        return self.get_pm()[0] == 4

    def getGameState(self):
        state = []
        # for i in len(self.list):
        # if self.list[i] != self.solution[i] :
        pass

    def fitness(self):
        return statistics.mean([self.getScore(story) for story in self.history])

    def jumpingJack(self):
        print("🏃‍ 🏃‍ 🏃️ 🏃‍ 🏃‍ 🏃️")
        self.fitness()

    def geneticSolution(self):
        self.fillRandomly()
        scores = self.getScore()
        toBeTestedList = self.list

        while self.getScore(toBeTestedList) < scores:
            toBeTestedList = self.permutation(self.list)

        # On aura un meilleur score



def score(p, m):
    """
    :param p: number of correctly placed colors
    :param m: number of misplaced colors, but still correct
    :return: the current game score
    """
    return (p / BALL_COUNT) * 25 + (m / BALL_COUNT) * 12.5




def compare(c1, c2):
    """
    :param c1: candidate solution list of balls
    :param c2: target solution list of balls
    :return: p and m
    """
    p, m = 0, 0
    for index, ball in enumerate(c1):
        if ball == c2[index]:
            p += 1
        elif ball in c2:
            m += 1
    return p, m


SOLUTION = [Ball(color) for color in COLORS]
BALL_COUNT = len(SOLUTION)


def geneticSolution(board):
    while board.getScore() < 4 and board.tryCount < board.maxTry:
        pass


if __name__ == '__main__':
    mBoard = Board(SOLUTION)
