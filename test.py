from shape_calculator import *

r1 = Rectangle(10, 5)
print(r1)
r1.set_width(12)
r1.set_height(3)
print(r1.get_picture())
r1.set_width(2)
print(r1.get_picture())

r2 = Rectangle(3, 3)
print(r2.get_picture())
print(r2.get_perimeter())
print(r2.get_diagonal())
print(r2.get_area())
print(r2.get_amount_inside(r1))


