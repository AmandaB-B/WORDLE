import tkinter as tk 

window = tk.Tk()
window.title("Wordle")



frame1 = tk.Frame()
frame1.pack()

frame1.rowconfigure([0,1,2,3,4,5,6,7], minsize = 150)
frame1.columnconfigure([0,1,2,3,4,5,6], minsize = 150)


        
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



label21 = tk.Frame(master = frame1)
label21.grid (row = 4, column = 0, sticky = "nsew", padx = 5, pady = 5)
label22 = tk.Frame(master = frame1)
label22.grid (row = 4, column = 1, sticky = "nsew", padx = 5, pady = 5)
label23 = tk.Frame(master = frame1)
label23.grid (row = 4, column = 2, sticky = "nsew", padx = 5, pady = 5)
label24 = tk.Frame(master = frame1)
label24.grid (row = 4, column = 3, sticky = "nsew", padx = 5, pady = 5)
label25 = tk.Frame(master = frame1)
label25.grid (row = 4, column = 4, sticky = "nsew", padx = 5, pady = 5)


label26 = tk.Frame(master = frame1)
label26.grid (row = 5, column = 0, sticky = "nsew")
label27 = tk.Frame(master = frame1)
label27.grid (row = 5, column = 1, sticky = "nsew")
label28 = tk.Frame(master = frame1)
label28.grid (row = 5, column = 2, sticky = "nsew")
label29 = tk.Frame(master = frame1)
label29.grid (row = 5, column = 3, sticky = "nsew")
label30 = tk.Frame(master = frame1)
label30.grid (row = 5, column = 4, sticky = "nsew")







window.mainloop()




window.mainloop()
