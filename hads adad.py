from random import randint

javab = randint(1, 6)

while True:
    i = int(input("Guess what number is chosen? "))

    if i > javab:
        print("My number is smaller!")
    elif i < javab:
        print("My number is bigger!")
    else:
        print(f"Your guess is correct. That was {javab}")
        break

        