from random import randint

javab = randint (1, 6)

i = int(input("Guess What number is chosen?"))
if (i == javab):
    print ("Correct Guess!")
else:
    print(f"Wrong Guess! {javab} was my number!")