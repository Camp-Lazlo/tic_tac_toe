from tkinter import *


window = Tk()
window.title("Tic-Tac-Toe")
window.config(padx=50, pady=50)


canvas = Canvas(width=336, height=50)
player_text = canvas.create_text(168, 25, text="X", font=("Times", 15, "bold"), fill="gray")
canvas.grid(row=0, column=0, columnspan=3)

x_img = PhotoImage(file="black_o.png")
o_img = PhotoImage(file="black_x.png")
pixel = PhotoImage(width=1, height=1)

first_turn = True
x_buttons = []
o_buttons = []

def flip_tile(btn):
    global first_turn
    global x_buttons
    global o_buttons


    if first_turn and btn not in x_buttons and btn not in o_buttons:
        btn.configure(image=x_img)
        x_buttons.append(btn)
        canvas.itemconfig(player_text, text="O")
        first_turn = False
    elif not first_turn and btn not in x_buttons and btn not in o_buttons: 
        btn.configure(image=o_img)
        o_buttons.append(btn)
        canvas.itemconfig(player_text, text="X")
        first_turn = True

    if any(all(buttons[i] in x_buttons for i in indices) for indices in ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                                                                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                                                         [0, 4, 8], [2, 4, 6])):
        x_buttons = buttons
        canvas.itemconfig(player_text, text="X Wins")

    elif any(all(buttons[i] in o_buttons for i in indices) for indices in ([0, 1, 2], [3, 4, 5], [6, 7, 8],
                                                                         [0, 3, 6], [1, 4, 7], [2, 5, 8],
                                                                         [0, 4, 8], [2, 4, 6])):
        o_buttons = buttons
        canvas.itemconfig(player_text, text="O Wins")
    
    elif all(button in x_buttons + o_buttons for button in buttons):
        canvas.itemconfig(player_text, text="Tie")

buttons = []

for i in range(1,4):
    for j in range(0,3):
        btn = Button(image=pixel, height=112, width=112)
        btn.configure(command=lambda current_btn=btn: flip_tile(current_btn))
        buttons.append(btn)
        btn.grid(row=i, column=j)


window.mainloop()


