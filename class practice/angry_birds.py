class AngryBird:
    __slots__ = ['_x', '_y']

    def __init__(self, x=0, y=0) -> None:
        self._x = x
        self._y = y

    def move_up_by(self, delta):
        self._y += delta

    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, value):
        if value < 0:
            value = 0
        self._x = value
    
    @property
    def y(self):
        return self._y
    
    @y.setter
    def y(self, value):
        if value < 0:
            value = 0
        self._y = value
    
    def __repr__(self):
        return f"<AngryBird ({self._x}, {self._y})"

bird = AngryBird(x=2, y=4)
print(bird)
print(bird.y)
bird.move_up_by(2)
print(bird.y)
bird.x = 12
bird.y = -20
print(bird.x, bird.y)