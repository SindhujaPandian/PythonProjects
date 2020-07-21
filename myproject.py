from os import system,name

def clear():
    if name=='nt':
        _=system('cls')
def display(arr):
    
    print('-------------')
    for i in range(0,len(arr),3):
        print('|',arr[i],'|',arr[i+1],'|',arr[i+2],'|')
        print('-------------')
def error(i):
    print('You entered worng position ')
    return i-1
def check(arr):
    for i in range(0,9,3):
        if arr[i]==arr[i+1]==arr[i+2] and arr[i]!=' ':
            return True
    for i in range(0,3):
        if arr[i]==arr[i+3]==arr[i+6] and arr[i]!=' ':
            return True
    if arr[0]==arr[4]==arr[8] and arr[0]!=' ':
        return True
    if arr[2]==arr[4]==arr[6] and arr[2]!=' ':
        return True
    return False
    
def winX():
    if player1_symbol=='X':
        return 1
    return 2
def winO():
    if player1_symbol=='O':
        return 1
    return 2
if __name__=='__main__':
    count = 1 
    print("              TIC TAC TOE              ")
    print("              --- --- ---              ")
    arr=[' ',' ',' ',' ',' ',' ',' ',' ',' ']
    #display(arr)
    print('Player 1 : Do you want to be X or O ?')
    player1_symbol=input()
    i=1
    if(player1_symbol=='X' or player1_symbol=='x'):
        player2_symbol='O'
        print('player 1 will start')
    else:
        player2_symbol='X'
        print('player 2 will start')
    display(arr)
    
    while(i<=9):
        if i%2!=0:
            print("Choose your position of X (1-9)")
            inp=int(input())
            if(inp<=9):
                if arr[inp-1]==' ':
                    arr[inp-1]='X'
                else:
                    i=error(i)
            else:
                i=error(i)
        else:
            print("Choose your position of O (1-9)")
            inp=int(input())
            if(inp<=9):
                if arr[inp-1]==' ':
                    arr[inp-1]='O'
                else:
                    i=error(i)
            else:
                i=error(i)
        clear()
        display(arr)
        if(check(arr)):
            if(i%2!=0):
                res=winX()
                print('Player',res,'win !!!!')
            else:
                res=winO()
                print('Player',res,'win !!!!')
            break
        i+=1
    if not check(arr):
        print('Match Draw !!!')
