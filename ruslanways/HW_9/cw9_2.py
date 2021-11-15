from random import choice

class Ghost(object):
    
    def __init__(self, color=("white", "yellow", "purple", "red")):
        self.color = choice(color)

ghost = Ghost()
print(ghost.color)
