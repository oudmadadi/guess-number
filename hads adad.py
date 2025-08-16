from random import randint

javab = randint(0, 100)
count = 0

while True:
    i = int(input("Guess what number is chosen? (between 0 to 100)   "))
    count += 1

    if i > javab:
        print("My number is smaller!")
    elif i < javab:
        print("My number is bigger!")
    else:
        print(f"Your guess is correct. That was {javab}.")
        print (f"You guessed {count} times!")
        break

        