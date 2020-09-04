import pprint
Board = {'1': ' ','2':' ','3':' ',
         '4':' ','5':' ','6':' ',
         '7':' ','8':' ','9':' ',
}



def PrintBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    

def win(board):
    if ((board['1'] == board['2'] == board['3'] != ' ') or (board['1'] == board['4'] == board['7'] != ' ') or (board['1'] == board['5'] == board['9'] != ' ')):
        print(board['1'] + ' wins')
        w = 1
        return w
        
    elif ((board['4'] == board['5'] == board['6'] != ' ') or (board['7'] == board['8'] == board['9'] != ' ') or (board['7'] == board['5'] == board['3'] != ' ')):
        print(board['4']+ ' wins')
        w = 1  
        return w
        
    elif ((board['2'] == board['5'] == board['8'] != ' ') or (board['3'] == board['6'] == board['9'] != ' ')):
        print(board['2'] + 'wins')
        w = 1
        return w
    else:
        pass
        

turn = 'X'

for i in range(9):
    
    PrintBoard(Board)
    if i >=5 :
        z = win(Board)
        
        if z == 1:
            break
        
        
        
    print("Where you want to put " + turn)
    val = input()
    Board[val] = turn
    
    
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    

if z != 1:
    print("It's a tie")

    
    
    
    
