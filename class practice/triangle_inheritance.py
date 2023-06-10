import math

# Write your class here.
class RegularPolygon():
    def __init__(self, sides = 3, length = 1) -> None:
        if sides < 3:
            raise Exception('A polygon must have at least 3 sides')
        self.num_sides = sides
        self.length = length
        self.type = 'Polygon'

    def identify_polygon(self):
        sides = self.num_sides
        if (sides == 3):
            self.type = 'Triangle'
        elif sides == 4:
            self.type = 'Quadrilateral'
        elif sides == 5:
            self.type = 'Pentagon'
        elif sides == 6:
            self.type = 'Hexagon'
        elif sides == 7:
            self.type = 'Heptagon'
        elif sides == 8:
            self.type = 'Octagon'
        elif sides == 9:
            self.type = 'Nonagon'
        elif sides == 10:
            self.type = 'Decagon'
        else:
            self.type = f'Polygon with {sides} sides'

    @classmethod
    def polygon_factory(cls, lst):
        return [cls(sides, length) for sides, length in lst]

    @staticmethod
    def get_perimeter(polygon):
        return polygon.num_sides * polygon.length
    
    def __repr__(self) -> str:
        return f'{self.num_sides} sided polygon of length {self.length}'


class Triangle(RegularPolygon):
    def __init__(self, sides=3, length=1):
        if sides != 3: raise Exception('A Triangle must have exactly three sides')
        super().__init__(sides, length)
        self.perimeter = self.get_perimeter(self)
        s = self.perimeter / 2
        self.area = math.sqrt(s*(s-length)**3)


triangle_a = Triangle(3, 3)
print(triangle_a.perimeter) # 9
print(triangle_a.area) # 3.8971...

triangle_b = Triangle(3, 12)
print(triangle_b.perimeter) # 36
print(triangle_b.area) # 62.3538...

triangle_c = Triangle(4, 12)
print(triangle_c.perimeter) # Exception: A triangle must have exactly three sides