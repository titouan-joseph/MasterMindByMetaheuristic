import pawn
import random
import statistics

if __name__ == '__main__':

    pawn.NUM_SELECTED = 30  # Number of selected values for the fitness choice
    pawn.WEIGHT_P = 25
    pawn.WEIGHT_M = 12.5
    pawn.FIRST_GENERERATION_POPULATION = 2000
    pawn.BALLS_COUNT = 4
    pawn.STATS = True

    ITER = 2000
    scores = []

    for i in range(ITER):
        pawn.SOLUTION = [pawn.Ball(random.choice(pawn.COLORS)) for _ in range(pawn.BALLS_COUNT)]
        first_proposal_set = [pawn.Board(pawn.SOLUTION) for _ in range(pawn.FIRST_GENERERATION_POPULATION)]
        first_proposal_set = list(map(lambda x: x.fillRandomly(), first_proposal_set))
        mBoard = pawn.Board(pawn.SOLUTION)
        scores.append(pawn.geneticSolution(mBoard, first_proposal_set))
        print(f"Iteration {i}/{ITER}")

    wonCounter = 0
    for elem in scores:
        if elem[0]:
            wonCounter += 1
    print("accuracy: ", (wonCounter/ITER)*100, "%")
    print("Nombre de tour moyen : ", statistics.mean([elem[2] for elem in scores]))
