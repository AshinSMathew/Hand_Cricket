import random
wickets=0
total_bot_runs=0
total_user_runs=0
def tossing():
    print(' ')
    print('*********************************************************************************************************************************************************\n')
    input("LET'S PLAY A GAME OF HAND CRICKET (PRESS ENTER TO CONTINUE)")
    print('\nINSTRUCTIONS')
    input('YOU CAN ONLY PUT ANY NUMBER BETWEEN 1 AND 6 (PRESS ENTER TO CONTINUE)')
    input("\nLETS PLAY")
    print('\nTOSSING')
    toss=input('DO YOU CHOOSE ODD OR EVEN: ')
    
    print()
    ts1=int(input('ENTER ANY NUMBER BETWEEN 1 AND 6 (for toss): '))
    ts2=random.randint(1,6)
    print('MINE IS ',ts2)
    
    global wickets
    if ((ts1+ts2)%2==0 and toss.lower()=='even') or ((ts1+ts2)%2!=0 and toss.lower()=='odd'):
        print('YOU WON THE TOSS\n')
        bb1=input('DO YOU CHOOSE BATTING OR BALLING (bat/ball): ')
        print()
        wickets=int(input('HOW MANY WICKETS: '))
        if bb1.lower()=='bat':
            batandball()
        if bb1.lower()=='ball':
            ballandbat()
    else:
        print('I WON THE TOSS\n')
        choice_array=['bat','ball']
        bb2=choice_array[random.randint(0,1)]
        wickets=random.randint(1,3)
        print('I CHOOSE ',wickets,' WICKETS')
        print('I CHOOSE TO ',bb2.upper())
        if bb2.lower()=='bat':
            ballandbat()
        if bb2.lower()=='ball':
            batandball()

def batandball():
    print()
    input("NOW IT'S YOUR TURN TO BAT, AND I WILL BOWL (PRESS ENTER TO START THE GAME)\n")
    global total_user_runs
    input("PRESS ENTER TO START BATTING")
    for i in range(1,wickets+1):
        while True:
            run_user=int(input('YOUR INPUT: '))
            if run_user>6:
                n=input('YOUR INPUT IS GREATER THAN 6\n')
                continue
            bowling_bot=random.randint(1,6)
            print('MINE IS ',bowling_bot,'\n')
            if run_user==bowling_bot:
                print('YOUR WICKET DOWN.... \n')
                print('SCOREBOARD: ',total_user_runs,'/',i)
                break
            else:
                total_user_runs+=run_user

                
    print()
    input("NOW IT'S MY TURN TO BAT, AND YOU WILL BOWL (PRESS ENTER TO CONTINUE)\n")
    global total_bot_runs
    input("PRESS ENTER TO START BOWLING")
    for j in range(1,wickets+1):
        while total_user_runs > total_bot_runs:
            bowling_user=int(input('YOUR INPUT: '))
            if bowling_user>6:
                input('YOUR INPUT IS GREATER THAN 6 (PRESS ENTER TO CONTINUE)\n')
                continue
            run_bot=random.randint(1,6)
            print('MINE IS ',run_bot,'\n')
            if bowling_user==run_bot:
                print('MY WICKET DOWN.... \n')
                print('SCOREBOARD: ',total_bot_runs,'/',j)
                break
            else:
                total_bot_runs+=run_bot
    check()
    
def ballandbat():
    print()
    input("NOW IT'S MY TURN TO BAT, AND YOU WILL BOWL (PRESS ENTER TO CONTINUE)\n")
    global total_bot_runs
    global total_user_runs
    input("PRESS ENTER TO START BOWLING")
    for j in range(1,wickets+1):
        while True:
            bowling_user=int(input('YOUR INPUT: '))
            if bowling_user>6:
                input('YOUR INPUT IS GREATER THAN 6 (PRESS ENTER TO CONTINUE)\n')
                continue
            run_bot=random.randint(1,6)
            print('MINE IS ',run_bot,'\n')
            if bowling_user==run_bot:
                print('MY WICKET DOWN.... \n')
                print('SCOREBOARD: ',total_bot_runs,'/',j)
                break
            else:
                total_bot_runs+=run_bot
    
    print()
    input("NOW IT'S YOUR TURN TO BAT, AND I WILL BOWL (PRESS ENTER TO START THE GAME)\n")
    input("PRESS ENTER TO START BATTING")
    for i in range(1,wickets+1):
        while total_bot_runs > total_user_runs:
            run_user=int(input('YOUR INPUT: '))
            if run_user>6:
                n=input('YOUR INPUT IS GREATER THAN 6\n')
                continue
            bowling_bot=random.randint(1,6)
            print('MINE IS ',bowling_bot,'\n')
            if run_user==bowling_bot:
                print('YOUR WICKET DOWN.... \n')
                print('SCOREBOARD: ',total_user_runs,'/',i)
                break
            else:
                total_user_runs+=run_user
    check()

def check():
    global total_bot_runs,total_user_runs
    print('YOU TOOK ',total_user_runs)
    print('I TOOK ',total_bot_runs)

    if total_user_runs > total_bot_runs:
        print('CONGRATS YOU WON\n')
    elif total_bot_runs > total_user_runs:
        print('HAHAHA..... I WON\n')
    else:
        print("IT'S A TIE MATCH\n")

    total_bot_runs=0
    total_user_runs=0
    print("GAMEOVER\n")
    print('_________________________________________________________________________________________________________________________________________________________\n')
tossing()
