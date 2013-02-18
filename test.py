from math import pi

class Circle:
	def __init__(s, radius):
		s.r = radius
	def circumference(s):
		return 2*s.r*pi
	def area(s):
		return s.r**2*pi

c1 = Circle(10)
c2 = Circle(2)

print c1.circumference()
print c1.area()
print c2.circumference()
print c2.area()
