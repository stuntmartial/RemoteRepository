def subtractNumbers(nums):
    length= len(nums)
    assert length== 2

    num1, num2= nums
    return abs(num1- num2)

nums= [int(num) for num in input().split()]
difference= subtractNumbers(nums)
print("Difference-> ", difference)