import random
n=random.randint(1,100)
for i in range (0,3):
    a=int(input("Guess the no. "))
    if a==n:
        print(f"BINGO !!!\n You Guessed Right Number\n the Number is {n}")
        break
    elif a>n:
        print("You guess the Number too high !!!")
    elif a<n:
        print("You Guessed the Number too Small !!!")
else:
    print("YOU LOSE !!!!")
    print("You Tried Very Good But")
    print(f"The Right Number is {n}")            
