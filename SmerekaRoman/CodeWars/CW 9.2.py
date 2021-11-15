import random

class Ghost(object):
    
    def __init__(self):
        self.color = random.choice(['white','purple', 'red', 'yellow'])

        