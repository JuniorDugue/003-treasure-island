'''Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

Under 18.5 they are underweight
Over 18.5 but below 25 they have a normal weight
Over 25 but below 30 they are slightly overweight
Over 30 but below 35 they are obese
Above 35 they are clinically obese'''

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = height / weight **2

if bmi < 18.5:
  print("you're underweight")
elif bmi > 18.5:
  print("you have a normal weight")
elif bmi <  25:
  print("you have a normal weight")
elif bmi > 25:
  print("you are slightly overweight")
elif bmi < 30:
  print("you are slightly overweight")
elif bmi > 30:
  print("you are obese")
elif bmi < 35:
  print("you are obese")
elif bmi > 35:
  print("you are clinically obese")
else:
  print("error")



