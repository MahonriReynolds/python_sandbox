
import numpy as np


class Boid():
    def __init__(self, position, velocity) -> None:
        self.__position = position
        self.__velocity = velocity

    def move(self, vectors):
        self.__velocity += vectors[0] / 300     # go to center of flock
        self.__velocity += vectors[1] * 600     # avoid others in flock
        self.__velocity += vectors[2] / 10      # match direction of flock
        self.__velocity += vectors[3] / 250     # go to center of map
        self.__velocity += vectors[4] / 300     # avoid other flocks
        
        self.__velocity = (self.__velocity / np.linalg.norm(self.__velocity)) * 5
        
        self.__position += self.__velocity

    def locate(self):
        return self.__position, self.__velocity
    
