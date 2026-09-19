# A list comprehension to generate a list of all odd numbers between 1 and 50 that are divisible by 3. 

odd_divisible_by_3 = [
    num for num in range(1, 51) if num % 2 != 0 and num % 3 == 0
]
print(odd_divisible_by_3)
