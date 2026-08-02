from math import sqrt

class Vector:
    def __init__(self, pos=(0,0)):
        self.x, self.y = pos

    def set(self, pos):
        self.x, self.y = pos

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector([self.x + other.x, self.y + other.y])

    def __radd__(self, other):
        return self.__add__(other)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __sub__(self, other):
        return Vector([self.x - other.x, self.y - other.y])

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector([-self.x, -self.y])

    def __mul__(self, k):
        return Vector([self.x*k, self.y*k])

    def __truediv__(self, k):
        return Vector([self.x/k, self.y/k])

    def coords(self):
        return [self.x, self.y]

    def round(self):
        return Vector([round(self.x), round(self.y)])

    def r2(self):
        return self.x*self.x + self.y*self.y

    def r(self):
        return sqrt(self.r2())

    def length(self):
        return self.r()

    def normalize(self):
        length = self.length()
        return Vector([self.x/length, self.y/length])