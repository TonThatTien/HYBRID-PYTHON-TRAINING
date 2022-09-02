print(len(12352))

# #string
print("Hello [0]")
print("Hello" + "World")
# #Integer
print(123 + 345)
# #Float
3.14159
# #Boolean
True
False

num_char = len(input("What is your name? "))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")

a = float(123)
print(type(a))

print(70 + float("100.5"))

print(str(70) + str(100))

two_digit_number = input("Type a two digit number: ")
print(type(two_digit_number))
first_digit = two_digit_number[0]
second_digit = two_digit_number[1]
print("Result =", int(first_digit) + int(second_digit))

print(3*(3 + 3) / 3 -3)

height = input("Enter your height in m: ")
weight = input("Enter your weight in kg: ")
height = float(height)
weight = float(weight)
bmi = weight / (height * height)
bmi_as_int = int(bmi)
print(bmi_as_int)

print(8 // 3) # print result in integer
print(type( 8 // 3))
print(type(4/2))
print(8%3)

score = 0
score += 1
print(score)

score = 0 
height = 1.8
isWinning = True
#f-String
print(f"Your score is {score}, your height is {height} and you are winning is {isWinning}")
# Or you can write that print("Your score is {0}, your height is {1} and you are winning is {2}".format(score,height,isWinning))

age = input("What is your current age: ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months left"
print(message)

print("Welcome to the tip caculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
money = (total_bill + (total_bill * (percentage_tip/100))) / people
print("Each person should pay: $", round(money,2))  
# bill = round(money,2)
# print(f"Each person should pay: ${bill}")