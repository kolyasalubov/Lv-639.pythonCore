class Human(object):
    def __init__(self):
        pass
class Man(Human):
    def __init__(self):
        super().__init__()
class Woman(Human):
    def __init__(self):
        super().__init__()
        
def God():
    adam = Man()
    eva = Woman()
    return [adam,eva]
