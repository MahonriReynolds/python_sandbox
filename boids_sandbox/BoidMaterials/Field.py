
from matplotlib import pyplot as plt
from Flock import Flock


class Field():
    def __init__(self, flock_sizes) -> None:
        
        self.__flocks = []
        for size, style in zip(flock_sizes, ('bo', 'gs', 'rp', 'go', 'rs', 'bp')):
            new_flock = Flock(size, style)
            self.__flocks.append(new_flock)
        
        plt.ion() 
        self.__fig = plt.figure(figsize=(12, 8))
        self.__subplot = self.__fig.add_subplot(projection='3d')


    def view(self):
        while True:
            self.__subplot.clear()
            
            for flock in self.__flocks:
                x, y, z, s = flock.get_points()
                self.__subplot.plot(x, y, z, s)
            
            self.__subplot.set_xlim3d([-200, 200])
            self.__subplot.set_xlabel('X')
            self.__subplot.set_ylim3d([-200, 200])
            self.__subplot.set_ylabel('Y')
            self.__subplot.set_zlim3d([-200, 200])
            self.__subplot.set_zlabel('Z')
            self.__fig.canvas.draw() 
            self.__fig.canvas.flush_events()
            # plt.pause(0.5)
     
        
        
        
        
        
            
                    



