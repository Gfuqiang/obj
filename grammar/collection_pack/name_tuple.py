from collections import namedtuple

Point = namedtuple('Point', 'x,y')
# p = Point._make([1, 2])
p = Point(1, 2)
print(p.x)
print(p._asdict())
p._replace(x=5)
print(p)