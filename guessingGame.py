import random
number = random.randint(0,9)
chances = 5
print("guess the number betweeen 0 to 9")
while(chances>0):
    guess = int(input('enter your guess'))
    if(guess == number):
        print('Congratulations!You Won')
        break
    elif guess<number:
        print('Youre Guess Was Too Low, Try A Higher Number')
    else:
        print('Youre Guess Was Too High, Try A Lower Number')
    chances -= 1 
if(chances == 0):
    print('You Lose , Please Try Again')  