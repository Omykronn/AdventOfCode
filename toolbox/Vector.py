from math import sqrt


class Vector(tuple):
    def __add__(self, x):
        assert len(self) == len(x)

        return Vector(self[i] + x[i] for i in range(len(self)))

    def __sub__(self, x):
        assert len(self) == len(x)

        return Vector(self[i] - x[i] for i in range(len(self)))

    def __mul__(self, x):
        if type(x) is int or type(x) is float:
            return Vector(u * x for u in self)
        elif type(x) is Vector:
            assert len(self) == len(x)

            return Vector(self[i] * x[i] for i in range(len(self)))
        else:
            raise TypeError

    def __truediv__(self, x):
        if type(x) is int or type(x) is float:
            return Vector(u / x for u in self)
        elif type(x) is Vector:
            assert len(self) == len(x)

            return Vector(self[i] / x[i] for i in range(len(self)))
        else:
            raise TypeError

    def __eq__(self, x) -> bool:
        try:
            flag = len(self) == len(x)
        except TypeError:
            flag = False

        i = 0

        while flag and i < len(self):
            flag = flag and (self[i] == x[i])
            i += 1

        return flag

    def norm(self):
        return sqrt(sum([u**2 for u in self]))

    def normalize(self):
        return self / self.norm()

    def dotProduct(self, x):
        assert len(self) == len(x)

        return sum([self[i] * x[i] for i in range(len(self))])

    def crossProduct(self, x):
        assert len(self) == len(x)

        if len(self) == 2:
            return Vector([0, 0, self[0] * x[1] - self[1] * x[0]])
        elif len(self) == 3:
            return Vector([self[1] * x[2] - self[2] * x[1], 
                           self[2] * x[0] - self[0] * x[2], 
                           self[0] * x[1] - self[1] * x[0]])
        else:
            raise ValueError("Vector dimension should be 2 or 3")
