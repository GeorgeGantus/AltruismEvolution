from tracemalloc import start


from classes.home import Home
from classes.blob import Blob
import random
class Simulation:
    def __init__(self,forest_size,predators_size, starting_blobs):
        self.forest_size = forest_size
        self.predators_size = predators_size
        self.starting_blobs = starting_blobs
        self.alive_blobs = []
    
    def initialize_simulation(self):
        self.homes = [Home() for _ in range(self.forest_size)]
        self.alive_blobs = []
        predators = random.sample(range(0,self.forest_size),self.predators_size)
        for predator in predators:
            self.homes[predator].tree.has_predator = True
        
        for i in range(self.starting_blobs):
            if i % 2 == 0:
                blob = Blob(False)
            else:
                blob = Blob(True)
            self.homes[i].blobs.append(blob)

    def look_for_food(self):
        for home in self.homes:
            if not home.blobs: continue

            if not home.tree.has_predator:
                self.alive_blobs += home.blobs
            else:
                if home.blobs[0].is_altruist:
                    self.alive_blobs += home.blobs[1:]
                else:
                    self.alive_blobs.append(home.blobs[0])
            home.blobs = []
    
    def return_home(self):
        altruist = 0
        not_altruist = 0
        random.shuffle(self.alive_blobs)
        for i,blob in enumerate(self.alive_blobs):
            if i < len(self.homes):
                self.homes[i].blobs.append(blob)
                # Reproduction
                self.homes[i].blobs += blob.assexual_reproduction()
                if blob.is_altruist:
                    altruist += 4
                else:
                    not_altruist += 4
        self.alive_blobs = []
        return altruist,not_altruist
    
    def day(self,print_enable=False):
        self.look_for_food()
        altruist,not_altruist = self.return_home()
        ratio = altruist/(altruist + not_altruist)
        if print_enable:
            print(altruist,not_altruist,ratio)
        return altruist,not_altruist,ratio
    
    def simulate(self,days,print_enable=False):
        self.initialize_simulation()
        for i in range(days):
            alt,not_alt,ratio = self.day(print_enable=print_enable)
        print(alt,not_alt,ratio)