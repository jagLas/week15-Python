# Write your class here.
class Quadrilateral:
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Quadrilateral):
    def __init__(self, length, width):
        if length != width:
            raise Exception('A square must have equal length and width')
        super().__init__(length, width)

quad = Quadrilateral(20, 10)
print(f"{quad.length}, {quad.width}") # 20, 10

square = Square(10, 10)
print(f"{square.length}, {square.width}") # 10, 10

not_square = Square(5, 10) # Exception: A square must have an equal length and width.