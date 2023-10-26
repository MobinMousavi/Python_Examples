
#Converting a decimal number to binary format using Stack

n = eval(input("Enter n:"))

#Creating Stack
stack = list()

while n > 0:
    stack.append(n%2)
    n = n // 2

for i in range(len(stack)):
    print(stack.pop(),end="")