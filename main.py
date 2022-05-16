import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user = int(input("What do you choose? Type 0 for Rock, 1 for Paper, and 2 for Scissors"))

if user == 0:
  print(rock)
elif user == 1:
  print (paper)
elif user == 2:
  print(scissors)
  
#computer player
cpu_choice = random.randint(0,2)
print("Computer chose: \n")
if cpu_choice == 0:
  print(rock)
elif cpu_choice == 1:
  print (paper)
elif cpu_choice == 2:
  print(scissors)


if user == 0 and cpu_choice == 0:
  print("You tied.")
elif user == 0 and cpu_choice == 1:
  print("You lose.")
elif user == 0 and cpu_choice == 2:
  print("You won.")

if user == 1 and cpu_choice == 0:
  print("You won.")
elif user == 1 and cpu_choice == 1:
  print("You tied.")
elif user == 1 and cpu_choice == 2:
  print("You lose.")

if user == 2 and cpu_choice == 0:
  print("You lose.")
elif user == 2 and cpu_choice == 1:
  print("You won.")
elif user == 2 and cpu_choice == 2:
  print("You tied.")