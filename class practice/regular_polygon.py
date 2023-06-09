# 3 sides - Triangle
# 4 sides - Quadrilateral
# 5 sides - Pentagon
# 6 sides - Hexagon
# 7 sides - Heptagon
# 8 sides - Octagon
# 9 sides - Nonagon
# 10 sides - Decagon
# Greater than 10 sides - Polygon with n sides


# Write your class here.
class RegularPolygon():
    def __init__(self, sides = 3, length = 1) -> None:
        if sides < 3:
            raise Exception('A polygon must have at least 3 sides')
        self._s = sides
        self._l = length
        self.type = 'Polygon'

    def identify_polygon(self):
        pass

    @classmethod
    def polygon_factory(cls):
        pass

    @staticmethod
    def get_permiter(polygon):
        pass


pentagon = RegularPolygon(5, 5)
octagon = RegularPolygon(8, 10)
dodecagon = RegularPolygon(12, 1)

print(f"{pentagon.num_sides} sides of length {pentagon.length}") # 5 sides of length 5
print(f"{octagon.num_sides} sides of length {octagon.length}") # 8 sides of length 10
print(f"{dodecagon.num_sides} sides of length {dodecagon.length}") # 12 sides of length 1

pentagon.identify_polygon()
octagon.identify_polygon()
dodecagon.identify_polygon()

print(pentagon.type) # Pentagon
print(octagon.type) # Octagon
print(dodecagon.type) # Polygon with 12 sides

print(RegularPolygon.get_perimeter(pentagon)) # 25
print(RegularPolygon.get_perimeter(octagon)) # 80
print(RegularPolygon.get_perimeter(dodecagon)) # 12

print(RegularPolygon.polygon_factory([(5, 5), (3, 2), (8, 10)])) # prints a list of 3 RegularPolygon objects

not_a_polygon = RegularPolygon(2, 5) # Exception: A polygon must have at least 3 sides.