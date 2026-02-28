import random

random_numbers=random.randint(1,10)
# print(random_numbers)
guess_number=int(input("Enter guess number: "))

while(random_numbers!= guess_number):
    guess_number=int(input("Enter again: "))
print("perfect played")            