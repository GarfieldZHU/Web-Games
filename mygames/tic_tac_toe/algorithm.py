#coding=utf-8
#author=Garfield

def ai_judge(board):
    if board[1][1] == 0:
        #无论如何优先抢占-1
        return (1,1)


#判断每次计算后当前是否存在胜负状况
def if_win(board):
    #棋盘共有8条线，每条线可以是O或X两种情况
    win = 0
    print board
    if board[0][0] == board[0][1] and board[0][1] == board [0][2]:
        #第一行
        if board[0][0] == 1:
            win = 1
        elif board[0][0] == -1:
            win = -1
        else:
            win = 0
    if board[1][0] == board[1][1] and board[1][1] == board [1][2]:
        #第二行
        print "here"
        if board[1][0] == 1:
            win = 1
        elif board[1][0] == -1:
            win = -1
        else:
            win = 0
    if board[2][0] == board[2][1] and board[2][1] == board [2][2]:
        #第三行
        if board[2][0] == 1:
            win = 1
        elif board[2][0] == -1:
            win = -1
        else:
            win = 0
    if board[0][0] == board[1][0] and board[1][0] == board [2][0]:
        #第一列
        if board[0][0] == 1:
            win = 1
        elif board[0][0] == -1:
            win = -1
        else:
            win = 0
    if board[0][1] == board[1][1] and board[1][1] == board [2][1]:
        #第二列
        if board[0][1] == 1:
            win = 1
        elif board[0][1] == -1:
            win = -1
        else:
            win = 0
    if board[0][2] == board[1][2] and board[1][2] == board [2][2]:
        #第三列
        if board[0][2] == 1:
            win = 1
        elif board[0][2] == -1:
            win = -1
        else:
            win = 0
    if board[0][0] == board[1][1] and board[1][1] == board [2][2]:
        #左上到右下
        if board[0][0] == 1:
            win = 1
        elif board[0][0] == -1:
            win = -1
        else:
            win = 0
    if board[0][2] == board[1][1] and board[1][1] == board [2][0]:
        #右上到左下
        if board[0][2] == 1:
            win = 1
        elif board[0][2] == -1:
            win = -1
        else:
            win = 0
    return win
