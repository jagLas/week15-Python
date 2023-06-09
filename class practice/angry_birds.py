class AngryBird:
    __slots__ = ['_x', '_y']

    def __init__(self, x=0, y=0) -> None:
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    def get_x(self):
        return self._x
    
    def get_y(self):
        return self._y
    
    def __repr__(self):
        return f"<AngryBird ({self._x}, {self._y})"

bird = AngryBird(x=2, y=4)
print(bird)
print(bird.get_y())
bird.move_up_by(2)
print(bird.get_y())