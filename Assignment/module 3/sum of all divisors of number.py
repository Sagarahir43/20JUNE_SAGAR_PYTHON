def sum_of_divisors(number):
    divisors=[]
    for i in range(1,number+1):
      if number % i == 0:
       divisors.append(i)
    return sum(divisors)

number=int(input("enter a number:"))
result=sum_of_divisors(number)
print(f"the sum of all divisors of {number} is:{result}")


