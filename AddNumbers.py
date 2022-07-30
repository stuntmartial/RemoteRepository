def addNumbers(nums)-> int:
    sum_= 0
    for num in nums: sum_+= num
    return sum_

nums= [int(num) for num in input().split()]
sum_= addNumbers(nums)
print("Sum-> ", sum_)