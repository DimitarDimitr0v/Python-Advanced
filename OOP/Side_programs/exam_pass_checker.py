class Triangle:

    def __int__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


    def get_perimeter(self, a, b, c):
        return a + b + c


t1 = Triangle(44, 2, 12)
result = t1.get_perimeter()
print(result)