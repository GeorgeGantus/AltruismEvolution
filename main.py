import random
from classes.home import Home
from classes.tree import Tree
from classes.blob import Blob
from classes.simulation import Simulation
random.seed(22)
FOREST_SIZE = 100
NUMBER_OF_PREDATORS = 10
STARTING_BLOBS = 4

simu = Simulation(FOREST_SIZE,NUMBER_OF_PREDATORS,STARTING_BLOBS)
simu.simulate(30)

""" forest = []
homes = []

for i in range(FOREST_SIZE):
    forest.append(Tree(i,False))
    homes.append(Home(i,False))

predators = random.sample(range(0,FOREST_SIZE),NUMBER_OF_PREDATORS)

for pred in predators:
    forest[pred].has_predator = True

for i in range(STARTING_BLOBS):
    if i % 2 == 0:
        homes[i].blobs.append(Blob(False))
    else:
        homes[i].blobs.append(Blob(True))

def runDay():
    alive_blobs = []

    for home in homes:

        if not home.blobs: continue

        if not forest[home.id].has_predator:
            alive_blobs += home.blobs
        else:

            if home.blobs[0].is_altruist:
                alive_blobs += home.blobs[1:]
            else:
                alive_blobs.append(home.blobs[0])

        home.blobs = []

    altruist = 0
    not_altruist = 0
    random.shuffle(alive_blobs)
    for i,blob in enumerate(alive_blobs):
        if i < len(homes):
            homes[i].blobs.append(blob)
            # Reproduction
            homes[i].blobs += [Blob(blob.is_altruist), Blob(blob.is_altruist), Blob(blob.is_altruist)]
            if blob.is_altruist:
                altruist += 4
            else:
                not_altruist += 4
    print(not_altruist, altruist)

for i in range(100):
    runDay() """