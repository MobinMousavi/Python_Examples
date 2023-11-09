class algebra:

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a - b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        return a-b

    def pow(self,a,b):
        return a**b

    def sqrt(self,a):
        return a**0.5

    def mod(self,a,b):
        return a%b

    def abs(self,a):
        if a > 0 :
            return a
        else:
            return -a

class discrete:

    def factorial(self,a):
        f = 1
        for i in range(1,a+1):
            f = f * i
        return f

class geometry:

    def pythagoras(self,a,b,c):
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            return "yes"
        else:
            return "No"

