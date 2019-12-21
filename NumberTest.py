print ("Guess my number")

number = (16)

guess = int(input("Enter a number from 1-25: "))

if guess == number:
        print ("You Won first guess, well done")
        quit(print("Exit? "))

while guess != number: 


    if guess < number:
        print ("Too Low")
        guess = int(input("Enter a number from 1-25: "))
    elif guess > number:
        print ("Too High")
        guess = int(input("Enter a number from 1-25: "))
    
    
else:
    print ("You got it good job") 
git remote add origin https://github.com/Lifedeather/Basic-Number-Guessing-Game.git
git push -u origin master
