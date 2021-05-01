from tkinter import *
from tkinter import messagebox
import random


def _change_player():
    '''
    This method is for changing the turn and giving the selection
    power to the other player
    '''

    global player
    if(player == 'O'):
        player = 'X'
    else:
        player = 'O'

def _button(root):
    '''This method returns the Button object which will be ppended to the board'''
    return Button(root,bg="#8AFFF3", text=' ', bd=12, width=3, font=('arial', 60, 'bold'), relief="sunken")

def _check():
    '''This method is for checking whether game has reached to a possible result(Either one player has won or match is tied) or not'''

    global player
    for i in range(3):
        if(board[i][0]['text']==board[i][1]['text']==board[i][2]['text']==player or board[0][i]['text']==board[1][i]['text']==board[2][i]['text']==player):
            messagebox.showinfo("Congratulations!!", "player "+player+" has won!!")
            reset()
    if(board[0][0]['text']==board[1][1]['text']==board[2][2]['text']==player or board[0][2]['text']==board[1][1]['text']==board[2][0]['text']==player):
        messagebox.showinfo("Congratulations!!", "player " + player + " has won!!")
        reset()
    elif(board[0][0]["state"]==board[0][1]["state"]==board[0][2]["state"]==board[1][0]["state"]==board[1][1]["state"]==board[1][2]["state"]==board[2][0]["state"]==board[2][1]["state"]==board[2][2]["state"]==DISABLED):
        messagebox.showinfo("Match tied","Thank God!!, You both are still friends!!")
        reset()

def reset():
    '''This method is for resetting the board'''
    global player
    for i in range(3):
        for j in range(3):
            board[i][j]["text"] = " "
            board[i][j]["state"] = NORMAL
    player = random.choice(['O', 'X'])

def click(row,col):
    '''This method diables the button and the text is set to the player's name whose turn was to push the button'''
    board[row][col].config(state=DISABLED,text=player, disabledforeground=player_color[player])
    _check()
    _change_player()
    label.config(text=player+"'s chance", font=('arial', 20, 'bold'))


root = Tk()
root.title("Tic-Tac-Toe")
player = random.choice(['O','X'])
player_color = {'O': '#C29B60', 'X': '#FE6EB0'}
board = [[], [], []]

for i in range(3):
    for j in range(3):
        board[i].append(_button(root))
        board[i][j].config(command=lambda row=i, col=j: click(row, col))
        board[i][j].grid(row=i, column=j)

label = Label(text= player + "'s Chance", font=('arial', 20, 'bold'))
label.grid(row=3, column=0, columnspan=3)
root.mainloop()
