import tkinter as tk 

window = tk.Tk()
window.title("Wordle")



frame1 = tk.Frame()
frame1.pack()

frame1.rowconfigure([0,1,2,3,4,5,6,7], minsize = 50)
frame1.columnconfigure([0,1,2,3,4,5,6], minsize = 50)


        
label1 = tk.Frame(master = frame1, bg = "gray")
label1.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
label2 = tk.Frame(master = frame1, bg = "gray")
label2.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
label3 = tk.Frame(master = frame1, bg = "gray")
label3.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
label4 = tk.Frame(master = frame1, bg = "gray")
label4.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
label5 = tk.Frame(master = frame1, bg = "gray")
label5.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)


label6 = tk.Frame(master = frame1, bg = "gray")
label6.grid (row = 1, column = 0, sticky = "nsew", padx = 5, pady = 5)
label7 = tk.Frame(master = frame1, bg = "gray")
label7.grid (row = 1, column = 1, sticky = "nsew", padx = 5, pady = 5)
label8 = tk.Frame(master = frame1, bg = "gray")
label8.grid (row = 1, column = 2, sticky = "nsew", padx = 5, pady = 5)
label9 = tk.Frame(master = frame1, bg = "gray")
label9.grid (row = 1, column = 3, sticky = "nsew", padx = 5, pady = 5)
label10 = tk.Frame(master = frame1, bg = "gray")
label10.grid (row = 1, column = 4, sticky = "nsew", padx = 5, pady = 5)



label11 = tk.Frame(master = frame1, bg = "gray")
label11.grid (row = 2, column = 0, sticky = "nsew", padx = 5, pady = 5)
label12 = tk.Frame(master = frame1, bg = "gray" )
label12.grid (row = 2, column = 1, sticky = "nsew", padx = 5, pady = 5)
label13 = tk.Frame(master = frame1, bg = "gray")
label13.grid (row = 2, column = 2, sticky = "nsew", padx = 5, pady = 5)
label14 = tk.Frame(master = frame1, bg = "gray")
label14.grid (row = 2, column = 3, sticky = "nsew", padx = 5, pady = 5)
label15 = tk.Frame(master = frame1,bg = "gray")
label15.grid (row = 2, column = 4, sticky = "nsew", padx = 5, pady = 5)


label16 = tk.Frame(master = frame1, bg = "gray")
label16.grid (row = 3, column = 0, sticky = "nsew", padx = 5, pady = 5)
label17 = tk.Frame(master = frame1, bg = "gray")
label17.grid (row = 3, column = 1, sticky = "nsew", padx = 5, pady = 5)
label18 = tk.Frame(master = frame1, bg = "gray")
label18.grid (row = 3, column = 2, sticky = "nsew", padx = 5, pady = 5)
label19 = tk.Frame(master = frame1, bg = "gray")
label19.grid (row = 3, column = 3, sticky = "nsew", padx = 5, pady = 5)
label20 = tk.Frame(master = frame1, bg = "gray")
label20.grid (row = 3, column = 4, sticky = "nsew", padx = 5, pady = 5)



label21 = tk.Frame(master = frame1, bg = "gray")
label21.grid (row = 4, column = 0, sticky = "nsew", padx = 5, pady = 5)
label22 = tk.Frame(master = frame1, bg = "gray")
label22.grid (row = 4, column = 1, sticky = "nsew", padx = 5, pady = 5)
label23 = tk.Frame(master = frame1, bg = "gray")
label23.grid (row = 4, column = 2, sticky = "nsew", padx = 5, pady = 5)
label24 = tk.Frame(master = frame1, bg = "gray")
label24.grid (row = 4, column = 3, sticky = "nsew", padx = 5, pady = 5)
label25 = tk.Frame(master = frame1, bg = "gray")
label25.grid (row = 4, column = 4, sticky = "nsew", padx = 5, pady = 5)


label26 = tk.Frame(master = frame1, bg = "gray")
label26.grid (row = 5, column = 0, sticky = "nsew", padx = 5, pady = 5)
label27 = tk.Frame(master = frame1, bg = "gray")
label27.grid (row = 5, column = 1, sticky = "nsew", padx = 5, pady = 5)
label28 = tk.Frame(master = frame1, bg = "gray")
label28.grid (row = 5, column = 2, sticky = "nsew", padx = 5, pady = 5)
label29 = tk.Frame(master = frame1, bg = "gray")
label29.grid (row = 5, column = 3, sticky = "nsew", padx = 5, pady = 5)
label30 = tk.Frame(master = frame1, bg = "gray")
label30.grid (row = 5, column = 4, sticky = "nsew", padx = 5, pady = 5)



frame2 = tk.Frame()
frame2.pack()

frame2.rowconfigure([0,1], minsize = 5)
frame2.columnconfigure([0,1,2,3,4,5,6,7,8,9,10], minsize = 5)

button1 = tk.Button(master = frame2, text= "Q", bg = "light gray", width = 5, height = 5)
button1.grid (row = 0, column = 0, sticky = "nsew", padx = 5, pady = 5)
button2 = tk.Button(master = frame2, text= "W", bg = "light gray", width=5, height=5)
button2.grid (row = 0, column = 1, sticky = "nsew", padx = 5, pady = 5)
button3 = tk.Button(master = frame2, text= "E", bg = "light gray", width=5, height=5)
button3.grid (row = 0, column = 2, sticky = "nsew", padx = 5, pady = 5)
button4 = tk.Button(master = frame2, text= "R", bg = "light gray", width=5, height=5)
button4.grid (row = 0, column = 3, sticky = "nsew", padx = 5, pady = 5)
button5 = tk.Button(master = frame2,text= "T", bg = "light gray", width=5, height=5)
button5.grid (row = 0, column = 4, sticky = "nsew", padx = 5, pady = 5)
button6 = tk.Button(master = frame2, text= "Y", bg = "light gray", width=5, height=5)
button6.grid (row = 0, column = 5, sticky = "nsew", padx = 5, pady = 5)
button7 = tk.Button(master = frame2,text= "U", bg = "light gray", width=5, height=5)
button7.grid (row = 0, column = 6, sticky = "nsew", padx = 5, pady = 5)
button8 = tk.Button(master = frame2,text= "I", bg = "light gray", width=5, height=5)
button8.grid (row = 0, column = 7, sticky = "nsew", padx = 5, pady = 5)
button9 = tk.Button(master = frame2,text= "O", bg = "light gray", width=5, height=5)
button9.grid (row = 0, column = 8, sticky = "nsew", padx = 5, pady = 5)
button28 = tk.Button(master = frame2,text= "P", bg = "light gray", width=5, height=5)
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
