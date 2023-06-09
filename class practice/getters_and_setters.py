# Write your class here.
class Game:
    def __init__(self) -> None:
        self._score = 0
    
    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, value):
        self._score += value * 10

my_game = Game()
print(my_game.score) # 0

my_game.score = 5
print(my_game.score) # 50