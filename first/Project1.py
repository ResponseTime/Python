import random

cl =int(0) 
pl = int(0)
def takeIn():
    global choice;
    choice = input("Enter: ")

def game():
    global CompWin;
    global PlayerWin;
    
    PlayerWin = False
    CompWin = False
    result = 'tie'
    rand = random.randint(0,2)
    list = ['rock','paper','scissor']
    comp = list[rand]
    if choice == comp:
        print("Draw both are same")
    elif ((choice == 'rock') and (comp == 'paper')) or ((choice =='scissor') and (comp == 'rock')) or((choice == 'paper') and (comp == 'scissor')):
        print("Computer wins")
        result = 'lose'
        cl  = cl + 1
    elif ((choice == 'paper') and (comp == 'rock')) or ((choice =='rock') and (comp == 'scissor')) or((choice == 'scissor') and (comp == 'paper')):
        print("You win")
        result = 'win'
        pl= pl + 1
    else:
        print("Enter valid command")  
def score():       
    print(f"Player {pl}")    
    print(f"comp {cl}")    

i = 0
while i<5:
    takeIn()
    game()
    i+=1
score()

