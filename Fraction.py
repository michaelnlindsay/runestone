def gcd(m, n):
    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn

    return n

class Fraction:

    def __init__(self, top, bottom):

        self.num = top
        self.den = bottom

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        """Return a Fraction that is the sum of self and other
        
        >>> print(Fraction(1, 2) + Fraction(1, 4))
        3/4
        
        """
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den

        return self.simplify(newnum,newden)

    def __sub__(self, other):
        """Return a Fraction that is the difference between self and other
        
        >>> print(Fraction(1, 2) - Fraction(1, 8))
        3/8
        """
        newnum = self.num * other.den - self.den * other.num
        newden = self.den * other.den

        return self.simplify(newnum,newden)

    def __mul__(self, other):
        """Return a Fraction that is self times other
        
        >>> print(Fraction(2, 1) * Fraction(1, 4))
        1/2
        >>> print(Fraction(1, 2) * Fraction(1, 4))
        1/8
        """
        newnum = self.num * other.num
        newden = self.den * other.den

        return self.simplify(newnum,newden)

    def __truediv__(self, other):
        """Return a Fraction that is self divided by other

        >>> print(Fraction(2, 3) / Fraction(1, 4))
        8/3
        >>> print(Fraction(1, 2) / Fraction(1, 6))
        3/1
        """
        newnum = self.num * other.den
        newden = self.den * other.num

        return self.simplify(newnum,newden)

    def __eq__(self, other):
        n1 = self.num * other.den
        n2 = other.num * self.den

        return n1 == n2

    def __gt__(self, other):
        n1 = self.num * other.den
        n2 = other.num * self.den

        return n1 > n2


    def __lt__(self, other):
        n1 = self.num * other.den
        n2 = other.num * self.den

        return n1 < n2

    def simplify(self, num, den):
        common = gcd(num, den)
        return Fraction(num//common, den//common)

    def show(self):
        print(str(self.num) + '/' + str(self.den))

f1 = Fraction(1, 4)
f2 = Fraction(1, 2)

f3 = f1 + f2
print(f3)

f4 = Fraction(6, 8)
f5 = Fraction(6, 9)
if f3 == f4:
    print('so true')
else:
    print('not so')

if f3 == f5:
    print('so true')
else:
    print('not so')


print(Fraction(1, 2) + Fraction(1, 4))
print(Fraction(1, 2) - Fraction(1, 8))

print(Fraction(2, 1) * Fraction(1, 4))
print(Fraction(1, 2) * Fraction(1, 4))

print(Fraction(2, 3) / Fraction(1, 4))
print(Fraction(1, 2) / Fraction(1, 6))

print(Fraction(1, 2) > Fraction(1, 4))
print(Fraction(1, 2) < Fraction(1, 4))

print(Fraction(1, 8) > Fraction(1, 4))
print(Fraction(1, 8) < Fraction(1, 4))
