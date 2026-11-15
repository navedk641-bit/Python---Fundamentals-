class Complex:
    def _init_(self, real, imag):
        self.real = real
        self.imag = imag

    def _add_(self, other):
        return Complex(
            self.real + other.real,
            self.imag + other.imag
        )

    def display(self):
        print(self.real, "+", self.imag, "i")


c1 = Complex(5, 3)
c2 = Complex(2, 4)

c3 = c1 + c2

print("First Complex Number:")
c1.display()

print("Second Complex Number:")
c2.display()

print("Sum:")
c3.display()
