#TIC-TAC-TOE in Python

#board is dictionary wuth key=num and value=blank 
myboard = { '7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in myboard:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0
    for i in range(10):
        printBoard(myboard)
        print("It's your turn," + turn + " write place number?")

        move = input()        

        if myboard[move] == ' ':
            myboard[move] = turn
            count =count+1
        else:
            print("Already filled. Write another place number?")
            continue

        if count == 9:
            print("\nGame Over.\n")                
            print("It's a Tie!!")

        #change the turn
        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'  

       #wheck winning condn after 5 moves
        if count >= 5:
            if myboard['7'] == myboard['8'] == myboard['9'] != ' ':
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won")                
                break
            elif myboard['4'] == myboard['5'] == myboard['6'] != ' ': 
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won")  
                break
            elif myboard['1'] == myboard['2'] == myboard['3'] != ' ': 
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won")  
                break
            elif myboard['1'] == myboard['4'] == myboard['7'] != ' ': 
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won") 
                break
            elif myboard['2'] == myboard['5'] == myboard['8'] != ' ': 
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won") 
                break
            elif myboard['3'] == myboard['6'] == myboard['9'] != ' ': 
                print("\nGame Over.\n")                
                print( turn + " won") 
                break 
            elif myboard['7'] == myboard['5'] == myboard['3'] != ' ': 
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won") 
                break
            elif myboard['1'] == myboard['5'] == myboard['9'] != ' ': 
                printBoard(myboard)
                print("\nGame Over.\n")                
                print( turn + " won") 
                break 

     
      
    

    re = input("Restart again?(y/n)")
    if re == "y" or re == "Y":  
        for key in board_keys:
            myboard[key] = " "

        game()

if __name__ == "__main__":
    game()