import random

cl =int(0) 
pl = int(0)
i = 0
while i<5:
    choice = input("Enter: ")
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
    print(f"Player {pl}")    
    print(f"comp {cl}")    
    i +=1
