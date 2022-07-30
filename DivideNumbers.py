def divideNumbers(num1,  num2):
    return num1/ num2 if num1> num2 else num2/num1

num1, num2= int(input()), int(input())
quotient= divideNumbers(num1, num2)
print("Quotient-> ", quotient)