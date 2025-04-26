import tkinter as tk 

window = tk.Tk()
window.title("Wordle")

frame1 = tk.Frame()
frame1.pack()

frame1.rowconfigure([0,1,2,3,4,5,6,7], minsize = 50)
frame1.columnconfigure([0,1,2,3,4,5,6], minsize = 50)






        
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




frame2 = tk.Frame()
frame2.pack()

frame2.rowconfigure([0,1], minsize = 5)
frame2.columnconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize = 5)

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
        global current_col,current_row
        if current_col >= len(label_grid[0]):
            current_col=0
            current_row +=1
        if current_row >= len(label_grid):
            current_row=0
            current_col=0
            
             
def letter_1():
    if current_row < len(label_grid) and current_col < len(label_grid[0]):
        label= label_grid[current_row][current_col]
        label["text"] = label["text"] + "Q"

        next_index()

     
def letter_2():
    label1["text"]=label1["text"]+"W"
def letter_3():
    label1["text"]=label1["text"]+"E"
def letter_4():
    label1["text"]=label1["text"]+"R"
def letter_5():
    label1["text"]=label1["text"]+"T"
def letter_6():
    label1["text"]=label1["text"]+"Y"
def letter_7():
    label1["text"]=label1["text"]+"U"
def letter_8():
    label1["text"]=label1["text"]+"I"
def letter_9():
    label1["text"]=label1["text"]+"O"    
def letter_10():
    label1["text"]=label1["text"]+"P"

def letter_11():
    label1["text"]=label1["text"]+"S"
def letter_12():
    label1["text"]=label1["text"]+"D"
def letter_13():
    label1["text"]=label1["text"]+"F"
def letter_14():
    label1["text"]=label1["text"]+"G"
def letter_15():
    label1["text"]=label1["text"]+"H"
def letter_16():
    label1["text"]=label1["text"]+"J"
def letter_17():
    label1["text"]=label1["text"]+"K"
def letter_18():
    label1["text"]=label1["text"]+"L"
   
def letter_20():
    label1["text"]=label1["text"]+"Z"

def letter_21():
    label1["text"]=label1["text"]+"X"
def letter_22():
    label1["text"]=label1["text"]+"C"
def letter_23():
    label1["text"]=label1["text"]+"V"
def letter_24():
    label1["text"]=label1["text"]+"B"
def letter_25():
    label1["text"]=label1["text"]+"N"
def letter_26():
    label1["text"]=label1["text"]+"M"

def letter_28():
    label1["text"]=label1["text"]+"P"

def handle_keypress(event):
    if event.char.isalpha():
        label4["text"]=label4["text"]+event.char



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

frame3 = tk.Frame()
frame3.pack()

frame3.rowconfigure([0,1], minsize = 5)
frame3.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize = 5)

button10 = tk.Button(master = frame3,text= "A", bg = "light gray", width=5, height=5)
button10.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
button11 = tk.Button(master = frame3,text= "S", bg = "light gray", width=5, height=5)
button11.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
button12 = tk.Button(master = frame3,text= "D", bg = "light gray", width=5, height=5)
button12.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
button13 = tk.Button(master = frame3,text= "F", bg = "light gray", width=5, height=5)
button13.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
button14 = tk.Button(master = frame3,text= "G", bg = "light gray", width=5, height=5)
button14.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)
button15 = tk.Button(master = frame3,text= "H", bg = "light gray", width=5, height=5)
button15.grid (row = 0, column = 5, sticky = "nsew", padx = 5, pady = 5)
button16 = tk.Button(master = frame3,text= "J", bg = "light gray", width=5, height=5)
button16.grid (row = 0, column = 6, sticky = "nsew", padx = 5, pady = 5)
button17 = tk.Button(master = frame3,text= "K", bg = "light gray", width=5, height=5)
button17.grid (row = 0, column = 7, sticky = "nsew", padx = 5, pady = 5)
button18= tk.Button(master = frame3, text= "L",bg = "light gray", width=5, height=5)
button18.grid (row = 0, column = 8, sticky = "nsew", padx = 5, pady = 5)

frame4 = tk.Frame()
frame4.pack()

frame4.rowconfigure([0,1], minsize = 5)
frame4.columnconfigure([0,1,2,3,4,5,6,7,8,9], minsize = 5)

button19= tk.Button(master = frame4, text= "ENTER",bg = "light gray", width=5, height=5)
button19.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
button20 = tk.Button(master = frame4,text= "Z", bg = "light gray", width=5, height=5)
button20.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
button21 = tk.Button(master = frame4,text= "X", bg = "light gray", width=5, height=5)
button21.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
button22 = tk.Button(master = frame4,text= "C", bg = "light gray", width=5, height=5)
button22.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
button23 = tk.Button(master = frame4,text= "V", bg = "light gray", width=5, height=5)
button23.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)
button24 = tk.Button(master = frame4,text= "B", bg = "light gray", width=5, height=5)
button24.grid (row = 0, column = 5, sticky = "nsew", padx = 5, pady = 5)
button25 = tk.Button(master = frame4,text= "N", bg = "light gray", width=5, height=5)
button25.grid (row = 0, column = 6, sticky = "nsew", padx = 5, pady = 5)
button26 = tk.Button(master = frame4,text= "M", bg = "light gray", width=5, height=5)
button26.grid (row = 0, column = 7, sticky = "nsew", padx = 5, pady = 5)
button27 = tk.Button(master = frame4,text= "<X]", bg = "light gray", width=5, height=5)
button27.grid (row = 0, column = 8, sticky = "nsew", padx = 5, pady = 5)






window.mainloop()
