import sys
#Ex:1

# for i in range(5):
#     for j in range(i):
#         print ("* ", end="")
#     print("")

# for i in range(5,0,-1):
#     for j in range(i):
#         print("* ", end="")
#     print('')


num__ = input("Enter a number:" )
num__ = num__ + 1 if num__ % 2 == 0 else num__
mid_row = num__ // 2 + 1 
for i in range(1, num__ + 1):
	if i < mid_row:
		print(i + "* ")
	else:
		j = mid_row * 2 - i
		print(j + "* ")

#Ex:2
for i in range(1,11):
	if i == 1:
		previous = 1
	else:
		previous = i - 1
	print(f"{previous} + {i} = {previous + i}")

#Ex:3

num = input("Enter a number:\n")

if not (num and num.isdigit()):
	sys.exit()
else:
	num = int(num)

for i in range(1, num // 2 + 1):
	if num % i == 0:
		print("The divisors of ",num, "is",i)



#Ex:4

factorial_num = input("Tell me number:\n")
factorial = 1

if not (factorial_num  and factorial_num.isdigit()):
	sys.exit()
else:
	factorial_num = int(factorial_num)

if factorial_num < 0:
   print("Factorial does not exist for negative number")
elif factorial_num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,factorial_num + 1):
       factorial = factorial*i
   print("The factorial of",factorial_num,"is",factorial)



#Ex:5

num_1, num_2 = 0, 1

while num_2 <= 50:
	print(num_2, " ", end="")
	num_1, num_2 = num_2, num_1 + num_2

