import random as rnd
names = ["Johnny", "Anja", "Felix", "Rikard"]

for name in names:
    age = rnd.randint(1, 100)
    print(f"{name} is {age} years old")

