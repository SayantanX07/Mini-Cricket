choice=["HEAD","TAIL"]
user=()                                                              #empty string
comp=()                                                              #empty string
while True:
    coin=input("Enter your choice (HEAD OR TAIL): \n").upper()
    print(f"Your choice: {coin}")
    if coin == "HEAD":
        user="HEAD"                                                    #adding the variable to the string user()
        print("Computer's choice: TAIL \n")
        comp="TAIL"                                                      #adding the variable to the string comp()
        break
    elif coin == "TAIL":
        user="TAIL"
        print("Computer's choice: HEAD \n")
        comp="HEAD"
        break
    else:
        print("Invalid input! Please enter either 'HEAD' or 'TAIL'.")
        
print("Toss : ")
import random
tossing=random.choice(["HEAD","TAIL"])
print(f"Its'{tossing}' ")

user_toss_choice=[]
comp_toss_choice=[]
if (tossing=="HEAD" and user=="HEAD") or (tossing=="TAIL" and user=="TAIL"):
    print("You won the toss \n")
    while True:
        toss_choice=["BAT","BALL"]
        user_decision=input("Whats your choice (BAT OR BALL) : ").upper()
        if user_decision in toss_choice:
            print(f"You chose to: {user_decision}")
            user_toss_choice.append(user_decision)
            break
        else:
            print("Invalid input! Please enter either 'BAT' or 'BALL'")
    if user_decision=="BAT":
        comp_toss_choice.append("BALL")
    else:
        comp_toss_choice.append("BAT")
else:
    print("Computer has won the toss \n")
    com_choice=random.choice(["BAT","BALL"])
    print(f"Computer chose to : {com_choice}")
    comp_toss_choice.append(com_choice)
    if com_choice=="BAT":
        user_toss_choice.append("BALL")
    else:
        user_toss_choice.append("BAT")
        
import random
user_score=0
comp_score=0
def user_batting(target):
    global user_score
    out=False
    while not out:
        user_run=int(input("Enter your run (1 to 6):"))
        if user_run > 6:
            print("Invalid run input")
            continue
        comp_ball=random.randint(1,6)
        print(f"Computer's ball : {comp_ball}")
        if comp_ball==user_run:
            print("You are out !! \n")
            out=True
        else:
            user_score +=user_run
        print(f"Your score = {user_score}")
        if target>0 and user_score>target:
            print("You have chased the target \n")
            out=True
            break
        elif target>0 and target==user_score:
            print("You have tied \n")
            out=True
            
def comp_batting(target):
    global comp_score
    out=False
    while not out:
        user_ball=int(input("Throw ball from (1 to 6) :"))
        if user_ball > 6:
            print("Invalid ball")
            continue
        comp_run=random.randint(1,6)
        print(f"Computer's run : {comp_run}")
        if comp_run==user_ball:
            print("Computer is out !! \n")
            out=True
        else:
            comp_score += comp_run
        print(f"Computer's score is : {comp_score}")
        if target>0 and comp_score>target:
            print("Computer has chased the target \n")
            out=True
            break
        elif target >0 and target==comp_score:
            print("Computer has tied \n")
            out=True
            
if user_toss_choice[0]=="BAT":                              #If user is batting first
    user_batting(target=0)
    print(f"Your final score- {user_score}\n")
    print("Computer is batting now.\n")
    print("Your bowl:")
    comp_batting(target=user_score)
    print(f"Computer's final score- {comp_score}")
else:                                                       #If user is bowling first
    print("You are bowling first.")
    comp_batting(target=0)
    print(f"Computer's final score- {comp_score}\n")
    print("You are batting now.\n")
    print("Computer bowl:")
    user_batting(target=comp_score)
    print(f"Your final score- {user_score} \n")
    
#Determine the winner
if user_score>comp_score:
    print("You won the match !!! \n")
elif user_score<comp_score:
    print("Computer won the match !!! \n")
else:
    print("Its a tie!")
