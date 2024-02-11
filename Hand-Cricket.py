import random
u=0
run=0
runs=0
def toss():
    print(' ')
    print('*********************************************************************************************************************************************************\n')
    z=input("\tLET'S PLAY A GAME OF HAND CRICKET (PRESS ENTER TO CONTINUE)\n")
    print('INSTRUCTIONS')
    V=input('YOU CAN ONLY PUT ANY NUMBER BETWEEN 1 AND 6 (PRESS ENTER TO CONTINUE)\n')
    print('TOSSING TIME\n')
    PO=input('DO YOU CHOOSE ODD OR EVEN ')
    if PO.lower()=='odd':
        RO='even'
    elif PO.lower()=='even':
        RO='odd'
    print()
    ts=int(input('ENTER ANY NUMBER BETWEEN 1 AND 6 (for toss) '))
    ra=random.randint(1,6)
    print('MINE IS ',ra)
    global u
    if (ts+ra)%2==0:
        if PO.lower()=='even':
            print('YOU WON THE TOSS\n')
            q0=input('DO YOU CHOOSE BATTING OR BALLING (bat/ball) ')
            print()
            u=int(input('HOW MANY WICKETS '))
            if q0.lower()=='bat':
                batandball()
            if q0.lower()=='ball':
                ballandbat()
    else:
        print('I WON THE TOSS')
        lp=['bat','ball']
        q1=lp[random.randint(0,1)]
        u=random.randint(1,3)
        print('I CHOOSE ',u,' WICKETS')
        print('I CHOOSE TO ',q1.upper())
        if q1.lower()=='bat':
            ballandbat()
        if q1.lower()=='ball':
            batandball()

def batandball():
    print(' ')
    m=input("NOW IT'S YOUR TURN TO BAT, AND I WILL BALL (PRESS ENTER TO START THE GAME)\n")
    global runs
    for i in range(1,u+1):
        while True:
            a=int(input('YOUR TURN TO BAT '))
            if a>6:
                n=input('YOUR INPUT IS GREATER THAN 6\n')
                continue
            q=random.randint(1,6)
            print('MINE IS ',q,'\n')
            if a==q:
                print('YOU ARE OUT, YOU TOOK ',runs,'RUNS\n')
                print('YOU LOST ',i,'WICKETS\n')
                break
            else:
                runs=runs+a

                
    print(' ')
    z=input("NOW IT'S MY TURN TO BAT, AND YOU WILL BALL (PRESS ENTER TO CONTINUE)\n")
    global run
    for b in range(1,u+1):
        while runs>run:
            a1=int(input('YOUR TURN TO BALL '))
            if a1>6:
                l=input('YOUR INPUT IS GREATER THAN 6 (PRESS ENTER TO CONTINUE)\n')
                continue
            q1=random.randint(1,6)
            print('MINE IS ',q1,'\n')
            if a1==q1:
                print('I GOT OUT, I TOOK ',run,'RUNS\n')
                print('I LOST ',b,'WICKETS\n')
                break
            else:
                run=run+q1
    check()
    
def ballandbat():
    print(' ')
    global u
    z=input("NOW IT'S MY TURN TO BAT, AND YOU WILL BALL (PRESS ENTER TO CONTINUE)\n")
    global run
    for b in range(1,u+1):
        while True:
            a1=int(input('YOUR TURN TO BALL '))
            if a1>6:
                l=input('YOUR INPUT IS GREATER THAN 6 (PRESS ENTER TO CONTINUE)\n')
                continue
            q1=random.randint(1,6)
            print('MINE IS ',q1,'\n')
            if a1==q1:
                print('I GOT OUT, I TOOK ',run,'RUNS\n')
                print('I LOST ',b,'WICKETS\n')
                break
            else:
                run=run+q1
    print(' ')
    m=input("NOW IT'S YOUR TURN TO BAT, AND I WILL BALL (PRESS ENTER TO START THE GAME)\n")
    global runs
    for i in range(1,u+1):
        while run>runs:
            print()
            a=int(input('YOUR TURN TO BAT '))
            if a>6:
                n=input('YOUR INPUT IS GREATER THAN 6\n')
                continue
            q=random.randint(1,6)
            print('MINE IS ',q,'\n')
            if a==q:
                print('YOU ARE OUT, YOU TOOK ',runs,'RUNS\n')
                print('YOU LOST ',i,'WICKETS\n')
                break
            else:
                runs=runs+a
    check()
def check():
    global run
    global runs
    if runs>run:
        print('YOU TOOK ',runs)
        print('I TOOK ',run)
        print('CONGRATS YOU WON\n')
    elif run>runs:
        print('YOU TOOK ',runs)
        print('I TOOK ',run)
        print('HAHAHA..... I WON\n')
    else:
        print('YOU TOOK ',runs)
        print('I TOOK ',run)
        print("IT'S A TIE MATCH\n")
    run=0
    runs=0
    we=input('PREES ENTER TO CONTINUE')
    print('_________________________________________________________________________________________________________________________________________________________\n')
toss()
