
import numpy as np


class Boid():
    def __init__(self, position, velocity) -> None:
        self.__position = position
        self.__velocity = velocity

    def move(self, vectors):
        self.__velocity += vectors[0] / 300
        self.__velocity += vectors[1] * 500
        self.__velocity += vectors[2] / 10
        self.__velocity += vectors[3] / 300
        self.__velocity += vectors[4] / 500
        
        self.__velocity = (self.__velocity / np.linalg.norm(self.__velocity)) * 5
        
        self.__position += self.__velocity

    def locate(self):
        return self.__position, self.__velocity
    
