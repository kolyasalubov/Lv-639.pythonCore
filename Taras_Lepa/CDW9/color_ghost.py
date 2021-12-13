# color ghost


import random

class Ghost():
    def __init__(self,color = None):
        paint = ["white","yellow","purple","red"]
        if color is None:
            color= random.choice(paint)
        self.color = color

        