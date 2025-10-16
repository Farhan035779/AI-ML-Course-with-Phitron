def factorial(num):
  fact = 1
  for i in range(1, num):
    fact *= i
  return fact

number = int(input("Input: "))
arm_num = 0
while number != 0:
  rem = number % 10
  arm_num += factorial(rem)
  number /= 10

if arm_num == number:
  print("Strong Number")
else:
  print("Not Strong Number")