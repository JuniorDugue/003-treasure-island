print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height > 120: #using >= operator will include people 120cm tall and taller
  print("You can ride the rollercoaster!") #is a block of code that lives inside of the if statement
else:
  print("Sorry, you have to grow taller before you can ride.") #is a block of code that lives inside of the else statement

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")


if height == 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")


if height != 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride.")