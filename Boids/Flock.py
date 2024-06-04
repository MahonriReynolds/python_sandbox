
import numpy as np
from random import uniform, uniform
from Boid import Boid


class Flock():
    def __init__(self, boid_count, boid_style) -> None:
        self.__center = np.array((
            uniform(-100, 100), 
            uniform(-100, 100), 
            uniform(-100, 100)
        ))
        self.__boids = []
        for _ in range(boid_count):
            offset = np.array((
                uniform(-30, 30), 
                uniform(-30, 30), 
                uniform(-30, 30)
            ))
            velocity = np.array((
                uniform(-5, 5), 
                uniform(-5, 5), 
                uniform(-5, 5)
            ))
            new_boid = Boid((self.__center + offset), velocity)
            self.__boids.append(new_boid)
        
        self.__styling = boid_style
    
    
    def set_center(self):
        self.__center = np.array((0.0, 0.0, 0.0))
        for boid in self.__boids:
            self.__center += boid.locate()[0]
        self.__center /= len(self.__boids)
        return self.__center
    
    def __get_vectors(self, b1, centers):
        vector_center = self.__center - b1.locate()[0]
        
        d = 5
        vector_away = np.array((0.0, 0.0, 0.0))
        vector_others = np.array((0.0, 0.0, 0.0))
        for b2 in self.__boids:
            if b1 != b2:
                b1_pos = b1.locate()[0]
                b2_pos, b2_v = b2.locate()
                vector_others += b2_v
                squared_dist = np.sum((b1_pos - b2_pos)**2, axis=0)
                dist = np.sqrt(squared_dist)
                if dist < d:
                    vector_away -= (b2_pos - b1_pos)
        vector_others /= len(self.__boids)
        
        vector_zero = -b1_pos
        
        vector_other_flocks = -(centers - self.__center)
        
        return vector_center, vector_away, vector_others, vector_zero, vector_other_flocks
    
    def __flock(self, centers):
        self.set_center()
        for boid in self.__boids:
            vectors = self.__get_vectors(boid, centers)
            boid.move(vectors)
    
    def get_points(self, centers):
        self.__flock(centers)
        all_x = []
        all_y = []
        all_z = []
        for boid in self.__boids:
            p = boid.locate()[0]
            all_x.append(p[0])
            all_y.append(p[1])
            all_z.append(p[2])
        return all_x, all_y, all_z, self.__styling
        
    
