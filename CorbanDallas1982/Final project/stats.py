class Stats():
    """statistika"""

    def __init__(self):
        """inicializacija statistiki"""
        self.reset_stats()
        self.run_game = True
        with open ('highscore.txt', 'r') as f:
            self.high_score = int(f.readline())

    def reset_stats(self):
        """izmenjajuschajasja statistika"""
        self.guns_left = 2
        """chislo giznej 2+1 = 3"""
        self.score = 0
        """schet"""
