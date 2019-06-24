# subclasses podem ter __init__ com quantidade de args diferente da superclasse

class A(object):

    def __init__(self, x):
        self.x = x

    def __str__(self):
        return f'A: x = {self.x}\n'

class B(A):

    def __init__(self, x, y):
        super().__init__(x)
        self.y = y

    def __str__(self):
        s1 = super().__str__()
        return s1 + f'B: y = {self.y}\n'

a = A(1)
b = B(2, 3)

print(a)
print(b)
