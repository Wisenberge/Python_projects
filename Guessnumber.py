#bisection search
print("Please think of a number between 0 and 100!")

guesscheck = False
Max = 100
Min = 0
Guess = 50
Response =  ""
while(not guesscheck):
    print("Is your number", Guess, "?", end=" ")
    Response = input("Enter l for low, h for high, or c for correct guess. ")
    if(Response == 'l'):
        Min = Guess
        Guess = int((Max + Min)/2)
    elif(Response == 'h'):
        Max = Guess
        Guess = int((Max + Min)/2)
    elif(Response == 'c'):
        print("Game over. Your secret number was", Guess)
        guesscheck = 1
    else:
        print("Sorry, I did not understand your input.")

        
    
