import tkinter as tk 
import random 


window = tk.Tk()
window.title("Wordle")

window.configure(padx=10, pady=10)
window.minsize(600, 700)

container = tk.Frame(master=window)
container.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

frame1 = tk.Frame(master=container, width=100, height=100)
frame1.pack(pady=(10,20))


frame1.rowconfigure([0,1,2,3,4,5], minsize =50)
frame1.columnconfigure([0,1,2,3,4], minsize = 50)

POTENTIAL_WORDS= ["SMART", "TULIP", "SCONE", "WATCH", "PLANT", "CATCH", "TREES", "GNOME"]

WORD=random.choice(POTENTIAL_WORDS)



 


        
label1 = tk.Label(master = frame1, text=" ", bg = "gray")
label1.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
label2 = tk.Label(master = frame1,text=" ", bg = "gray")
label2.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
label3 = tk.Label(master = frame1,text=" ", bg = "gray")
label3.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
label4 = tk.Label(master = frame1,text=" ", bg = "gray")
label4.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
label5 = tk.Label(master = frame1,text=" ", bg = "gray")
label5.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)


label6 = tk.Label(master = frame1,text=" ", bg = "gray")
label6.grid (row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
label7 = tk.Label(master = frame1,text=" ", bg = "gray")
label7.grid (row = 1, column = 1, sticky = "nsew", padx = 5, pady = 5)
label8 = tk.Label(master = frame1,text=" ", bg = "gray")
label8.grid (row = 1, column = 2, sticky = "nsew", padx = 5, pady = 5)
label9 = tk.Label(master = frame1,text=" ", bg = "gray")
label9.grid (row = 1, column = 3, sticky = "nsew", padx = 5, pady = 5)
label10 = tk.Label(master = frame1,text=" ", bg = "gray")
label10.grid (row = 1, column = 4, sticky = "nsew", padx = 5, pady = 5)



label11 = tk.Label(master = frame1,text=" ", bg = "gray")
label11.grid (row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)
label12 = tk.Label(master = frame1,text=" ", bg = "gray" )
label12.grid (row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)
label13 = tk.Label(master = frame1,text=" ", bg = "gray")
label13.grid (row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5)
label14 = tk.Label(master = frame1,text=" ", bg = "gray")
label14.grid (row = 2, column = 3, sticky = "nsew", padx = 5, pady = 5)
label15 = tk.Label(master = frame1,text=" ",bg = "gray")
label15.grid (row = 2, column = 4, sticky = "nsew", padx = 5, pady = 5)


label16 = tk.Label(master = frame1,text=" ", bg = "gray")
label16.grid (row = 3, column = 0, sticky = "nsew", padx = 5, pady = 5)
label17 = tk.Label(master = frame1,text=" ", bg = "gray")
label17.grid (row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)
label18 = tk.Label(master = frame1,text=" ", bg = "gray")
label18.grid (row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
label19 = tk.Label(master = frame1,text=" ", bg = "gray")
label19.grid (row = 3, column = 3, sticky = "nsew", padx = 5, pady = 5)
label20 = tk.Label(master = frame1,text=" ", bg = "gray")
label20.grid (row = 3, column = 4, sticky = "nsew", padx = 5, pady = 5)



label21 = tk.Label(master = frame1,text=" ", bg = "gray")
label21.grid (row = 4, column = 0, sticky = "nsew", padx = 5, pady = 5)
label22 = tk.Label(master = frame1,text=" ", bg = "gray")
label22.grid (row = 4, column = 1, sticky = "nsew", padx = 5, pady = 5)
label23 = tk.Label(master = frame1, text=" ",bg = "gray")
label23.grid (row = 4, column = 2, sticky = "nsew", padx = 5, pady = 5)
label24 = tk.Label(master = frame1,text=" ", bg = "gray")
label24.grid (row = 4, column = 3, sticky = "nsew", padx = 5, pady = 5)
label25 = tk.Label(master = frame1,text=" ", bg = "gray")
label25.grid (row = 4, column = 4, sticky = "nsew", padx = 5, pady = 5)


label26 = tk.Label(master = frame1,text=" ", bg = "gray")
label26.grid (row = 5, column = 0, sticky = "nsew", padx = 5, pady = 5)
label27 = tk.Label(master = frame1,text=" ", bg = "gray")
label27.grid (row = 5, column = 1, sticky = "nsew", padx = 5, pady = 5)
label28 = tk.Label(master = frame1,text=" ", bg = "gray")
label28.grid (row = 5, column = 2, sticky = "nsew", padx = 5, pady = 5)
label29 = tk.Label(master = frame1,text=" ", bg = "gray")
label29.grid (row = 5, column = 3, sticky = "nsew", padx = 5, pady = 5)
label30 = tk.Label(master = frame1,text=" ", bg = "gray")
label30.grid (row = 5, column = 4, sticky = "nsew", padx = 5, pady = 5)




frame2 = tk.Frame(master=container)
frame2.pack(pady=5)

frame2.rowconfigure([0], minsize = 5)
frame2.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize = 5)





label_grid = [
    [label1, label2, label3, label4, label5],
    [label6, label7, label8, label9, label10],
    [label11, label12, label13, label14, label15],
    [label16, label17, label18, label19, label20],
    [label21, label22, label23, label24, label25],
    [label26, label27, label28, label29, label30]
]
alphabet= ["A","B","C","D","E","F","G","H","I","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
 
current_col =0
current_row=0

def next_index():
    global current_col
    current_col += 1
    
    if current_col >= len(label_grid[0]):
        current_col = 5
        

command= ["S","M","A","R","T"]


def color_changer():
    global current_row, current_col
    ANSWER=WORD
    is_correct= True 
   
    for x in range(5):
        letter=label_grid[current_row][x]["text"]
        label=label_grid[current_row][x]

        if letter == ANSWER[x]:
            print("GREEN")
            label["bg"] = "green"
        elif letter in ANSWER:
            print("YELLOW")
            label["bg"] = "yellow"
        else:
            print("BLANK")
            is_correct=False
            pass
    if is_correct:
        winning_window()
    else:
        is_correct=False
    return is_correct

def winning_window():
    winning_window=tk.Tk()
    winning_window.title("Results")
    winning_window.minsize(300,300)
    Label = tk.Label(master = winning_window, text = "Congratulations!", bg = "green")
    Label.pack()

def losing_window():
    losing_window=tk.Tk()
    losing_window.minsize(300,300)
    losing_window.title("Results")
    Label1 = tk.Label(master = losing_window, text = "You lost :( Thanks for playing today!", bg = "red")
    Label1.pack()
    
    



def handler_enter(event=None):
    
    global current_row, current_col
    color_changer()
    
    current_row += 1
    current_col = 0
    if current_row == len(label_grid) and not color_changer is False:
        losing_window()
    


    


def delete_letter(event):
    global current_col, current_row
    if current_col > 0:
        current_col -= 1
        label = label_grid[current_row][current_col]
        label["text"] = " "




             
def letter_1():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "Q"

        next_index()
def letter_2():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "W"

        next_index()
def letter_3():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "E"

        next_index()
def letter_4():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "R"

        next_index()
def letter_5():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "T"

        next_index()
def letter_6():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "Y"

        next_index()
def letter_7():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "U"

        next_index()
def letter_8():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "I"

        next_index()
def letter_9():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "O"

        next_index()    
def letter_10():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "A"

        next_index()

def letter_11():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "S"

        next_index()
def letter_12():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "D"

        next_index()
def letter_13():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "F"

        next_index()
def letter_14():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "G"

        next_index()
def letter_15():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "H"

        next_index()
def letter_16():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "J"

        next_index()
def letter_17():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "K"

        next_index()
def letter_18():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "L"

        next_index()
   
def letter_20():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "Z"

        next_index()

def letter_21():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "X"

        next_index()
def letter_22():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "C"

        next_index()
def letter_23():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "V"

        next_index()
def letter_24():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "B"

        next_index()
def letter_25():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "N"

        next_index()
def letter_26():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "M"

        next_index()

def letter_28():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = "P"

        next_index()

def handle_keypress(event):
    global label, letter
    if event.char.isalpha():
        letter=label_grid[current_row][current_col]["text"]
        label=label_grid[current_row][current_col]
        label["text"]=event.char.upper()
        next_index()



button1 = tk.Button(master = frame2, text= "Q", bg = "light gray", width = 5, height = 5, command=letter_1)
button1.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
button2 = tk.Button(master = frame2, text= "W", bg = "light gray", width=5, height=5, command=letter_2)
button2.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
button3 = tk.Button(master = frame2, text= "E", bg = "light gray", width=5, height=5, command=letter_3)
button3.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
button4 = tk.Button(master = frame2, text= "R", bg = "light gray", width=5, height=5, command=letter_4)
button4.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
button5 = tk.Button(master = frame2,text= "T", bg = "light gray", width=5, height=5, command=letter_5)
button5.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)
button6 = tk.Button(master = frame2, text= "Y", bg = "light gray", width=5, height=5, command=letter_6)
button6.grid (row = 0, column = 5, sticky = "nsew", padx = 5, pady = 5)
button7 = tk.Button(master = frame2,text= "U", bg = "light gray", width=5, height=5, command=letter_7)
button7.grid (row = 0, column = 6, sticky = "nsew", padx = 5, pady = 5)
button8 = tk.Button(master = frame2,text= "I", bg = "light gray", width=5, height=5, command=letter_8)
button8.grid (row = 0, column = 7, sticky = "nsew", padx = 5, pady = 5)
button9 = tk.Button(master = frame2,text= "O", bg = "light gray", width=5, height=5, command=letter_9)
button9.grid (row = 0, column = 8, sticky = "nsew", padx = 5, pady = 5)
button28 = tk.Button(master = frame2,text= "P", bg = "light gray", width=5, height=5, command=letter_28)
button28.grid (row = 0, column = 9, sticky = "nsew", padx = 5, pady = 5)

frame3 = tk.Frame(master=container, width=50, height=50)
frame3.pack(pady=5)

frame3.rowconfigure([0], minsize = 5)
frame3.columnconfigure([0,1,2,3,4,5,6,7,8], minsize = 5)

button10 = tk.Button(master = frame3,text= "A", bg = "light gray", width=5, height=5, command=letter_10)
button10.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
button11 = tk.Button(master = frame3,text= "S", bg = "light gray", width=5, height=5, command=letter_11)
button11.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
button12 = tk.Button(master = frame3,text= "D", bg = "light gray", width=5, height=5, command=letter_12)
button12.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
button13 = tk.Button(master = frame3,text= "F", bg = "light gray", width=5, height=5, command=letter_13)
button13.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
button14 = tk.Button(master = frame3,text= "G", bg = "light gray", width=5, height=5, command=letter_14)
button14.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)
button15 = tk.Button(master = frame3,text= "H", bg = "light gray", width=5, height=5, command=letter_15)
button15.grid (row = 0, column = 5, sticky = "nsew", padx = 5, pady = 5)
button16 = tk.Button(master = frame3,text= "J", bg = "light gray", width=5, height=5, command=letter_16)
button16.grid (row = 0, column = 6, sticky = "nsew", padx = 5, pady = 5)
button17 = tk.Button(master = frame3,text= "K", bg = "light gray", width=5, height=5, command=letter_17)
button17.grid (row = 0, column = 7, sticky = "nsew", padx = 5, pady = 5)
button18= tk.Button(master = frame3, text= "L",bg = "light gray", width=5, height=5, command=letter_18)
button18.grid (row = 0, column = 8, sticky = "nsew", padx = 5, pady = 5)

frame4 = tk.Frame(master=container, width=50, height=50)
frame4.pack(pady=5)

frame4.rowconfigure([0], minsize = 5)
frame4.columnconfigure([0,1,2,3,4,5,6,7,8], minsize = 5)

button19= tk.Button(master = frame4, text= "ENTER",bg = "light gray", width=5, height=5, command=color_changer)
button19.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
button20 = tk.Button(master = frame4,text= "Z", bg = "light gray", width=5, height=5, command=letter_20)
button20.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
button21 = tk.Button(master = frame4,text= "X", bg = "light gray", width=5, height=5, command=letter_21)
button21.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
button22 = tk.Button(master = frame4,text= "C", bg = "light gray", width=5, height=5, command=letter_22)
button22.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
button23 = tk.Button(master = frame4,text= "V", bg = "light gray", width=5, height=5, command=letter_23)
button23.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)
button24 = tk.Button(master = frame4,text= "B", bg = "light gray", width=5, height=5, command=letter_24)
button24.grid (row = 0, column = 5, sticky = "nsew", padx = 5, pady = 5)
button25 = tk.Button(master = frame4,text= "N", bg = "light gray", width=5, height=5, command=letter_25)
button25.grid (row = 0, column = 6, sticky = "nsew", padx = 5, pady = 5)
button26 = tk.Button(master = frame4,text= "M", bg = "light gray", width=5, height=5, command=letter_26)
button26.grid (row = 0, column = 7, sticky = "nsew", padx = 5, pady = 5)
button27 = tk.Button(master = frame4,text= "<X]", bg = "light gray", width=5, height=5, command=delete_letter)
button27.grid (row = 0, column = 8, sticky = "nsew", padx = 5, pady = 5)




window.bind("<Key>", handle_keypress)
window.bind("<Return>", handler_enter)
window.bind("<BackSpace>", delete_letter)

window.mainloop()
