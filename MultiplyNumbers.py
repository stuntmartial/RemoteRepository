def multiplyNumbers(nums)-> int:
    length= len(nums)
    product= 0 if length==0 else 1

    for num in nums: product*= num
    return product

nums= [int(num) for num in input().split()]
product= multiplyNumbers(nums)
print("Product-> ", product)

    