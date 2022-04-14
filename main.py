import tkinter as tk
import random
window = tk.Tk()

window.title("Minesweeper by unknown")
window.geometry("+200+200")

def newgame():
    global new_frame, lbl_error, lbl_error_2
    new_frame = tk.Frame()
    new_frame.pack()

    lbl_diff = tk.Label(master = new_frame, text = "Choose a difficulty: ")
    lbl_diff.grid(row = 0, column = 0, sticky = "w")

    # e = easy, i = intermediate, h = hard, c = custom

    radio = tk.IntVar()

    rbtn_e = tk.Radiobutton(master = new_frame, text = "Easy", value = 1, variable = radio, command = easy)
    lbl_e = tk.Label(master = new_frame, text = "5 x 5 grid 8 mines")
    rbtn_e.grid(row = 1, column = 0, sticky = "w")
    lbl_e.grid(row = 2, column = 0, sticky = "w")

    rbtn_i = tk.Radiobutton(master = new_frame, text = "Intermediate", value = 2, variable = radio, command = intermediate)
    lbl_i = tk.Label(master = new_frame, text = "10 x 10 grid 40 mines")
    rbtn_i.grid(row = 3, column = 0, sticky = "w")
    lbl_i.grid(row = 4, column = 0, sticky = "w")

    rbtn_h = tk.Radiobutton(master = new_frame, text = "Hard", value = 3, variable = radio, command = hard)
    lbl_h = tk.Label(master = new_frame, text = "16 x 16 grid 100 mines")
    rbtn_h.grid(row = 5, column = 0, sticky = "w")
    lbl_h.grid(row = 6, column = 0, sticky = "w")

    global entry_c_h, entry_c_w, entry_c_m
    rbtn_c = tk.Radiobutton(master = new_frame, text = "Custom", value = 4, variable = radio)
    lbl_c_h = tk.Label(master = new_frame, text = "Height: ")
    entry_c_h = tk.Entry(master = new_frame, width = 3)
    lbl_c_w = tk.Label(master = new_frame, text = "Width: ")
    entry_c_w = tk.Entry(master = new_frame, width = 3)
    lbl_c_m = tk.Label(master = new_frame, text = "Mines: ")
    entry_c_m = tk.Entry(master = new_frame, width=3)
    btn_c = tk.Button(master = new_frame, text = "Confirm", command = custom)
    lbl_error = tk.Label(master = new_frame, text = "")
    lbl_error_2 = tk.Label(master = new_frame, text = "")

    # btn_c["command"] = lambda arg1 = entry_c_h.get(), arg2 = entry_c_w.get(), arg3 = entry_c_m.get() : custom(arg1, arg2, arg3)

    rbtn_c.grid(row = 1, column = 1, sticky = "W")
    lbl_c_h.grid(row = 2, column = 1, sticky = "W")
    entry_c_h.grid(row = 2, column = 2, sticky = "W")
    lbl_c_w.grid(row=3, column=1, sticky = "W")
    entry_c_w.grid(row=3, column=2, sticky = "W")
    lbl_c_m.grid(row=4, column=1, sticky = "W")
    entry_c_m.grid(row=4, column=2, sticky = "W")
    btn_c.grid(row = 5, column = 1, sticky = "W")
    lbl_error.grid(row = 6, column = 1, sticky = "w")
    lbl_error_2.grid(row = 7, column = 1, sticky = "w")

    btn_ok = tk.Button(master = new_frame, text = "OK", command = ok_new)
    btn_quit = tk.Button(master = new_frame, text = "Quit", command = close)
    btn_ok.grid(row = 7, column = 0, sticky = "NSEW")
    btn_quit.grid(row = 8, column = 0, sticky = "NSEW")

    window.mainloop()

def display():
    global frame, r, c, mines, arr, create_frame_1, btn_arr, clicked, first_time, create_frame, first_clicked_m

    first_time = True
    first_clicked_m = True
    r = row
    c = column

    arr = [["E" for c in range(c)] for r in range(r)]
    btn_arr = [[0 for c in range(c)] for r in range(r)]

    mines = m
    clicked = 0

    for k in range(mines):
        placed = False
        while not placed:
            place = random.randint(0, r * c - 1)

            # finding place for i and j
            found_i = False
            i = 0
            while not found_i:
                if i * c < place:
                    i += 1
                if i * c > place:
                    i -= 1
                    found_i = True
                if i * c == place:
                    found_i = True
            j = place - (i * c)

            if arr[i][j] == "E":
                arr[i][j] = "M"
                placed = True
    def create_frame():
        global arr, btn_arr, frame
        for i in range(r):
            for j in range(c):
                count = 0
                if arr[i][j][0] == "E":
                    for i_check in range(-1,2):
                        for j_check in range(-1,2):
                            if i+i_check >= 0 and i + i_check < r and j + j_check >= 0 and j + j_check < c:
                                if arr[i+i_check][j+j_check] == "M":
                                    count += 1
                    if arr[i][j] == "E":
                        arr[i][j] += str(count)
                    else:
                        arr[i][j] = "E" + str(count)
        frame = tk.Frame()
        frame.pack()
        for i in range(r):
            for j in range(c):
                if arr[i][j] == "M":
                    btn_arr[i][j] = tk.Button(master=frame, text = "", width = 4, height = 2, command = pressed_m)
                    btn_arr[i][j]["command"] = lambda arg1 = i, arg2 = j : pressed_m(arg1, arg2)
                else:
                    btn_arr[i][j] = tk.Button(master=frame, text = "", width = 4, height = 2, command = pressed_e_1)
                    btn_arr[i][j]["command"] = lambda arg1 = i, arg2 = j : pressed_e_1(arg1, arg2)
                btn_arr[i][j].grid(row=i, column=j)
    def create_frame_1():
        global frame_1, lbl
        frame_1 = tk.Frame()
        frame_1.pack()
        btn_reset = tk.Button(master=frame_1, text="New Game", command=reset).pack()
        btn_restart = tk.Button(master = frame_1, text = "Restart", command = restart).pack()
        btn_close = tk.Button(master=frame_1, text="Quit", command=close).pack()
        lbl = tk.Label(master = frame_1, text = "")
        lbl.pack()
    create_frame()
    create_frame_1()
    window.mainloop()

def reset():
    frame.destroy()
    frame_1.destroy()
    lbl.destroy()
    newgame()

def restart():
    global frame, clicked, first_time
    clicked = 0
    first_time = False
    frame.destroy()
    frame_1.destroy()
    restart_arr = arr

    frame = tk.Frame()
    frame.pack()
    for i in range(r):
        for j in range(c):
            if restart_arr[i][j] == "M":
                btn_arr[i][j] = tk.Button(master=frame, text = "", width = 4, height = 2, command = pressed_m)
                btn_arr[i][j]["command"] = lambda arg1 = i, arg2 = j : pressed_m(arg1, arg2)
            else:
                btn_arr[i][j] = tk.Button(master=frame, text = "", width = 4, height = 2, command = pressed_e_1)
                btn_arr[i][j]["command"] = lambda arg1 = i, arg2 = j : pressed_e_1(arg1, arg2)
            btn_arr[i][j].grid(row = i, column = j)
    create_frame_1()

def close():
    window.destroy()

# if press "M"
def pressed_m(i,j):
    global arr, first_clicked_m
    placed = False
    count = 0
    if clicked == 0 and first_time == True and first_clicked_m == True:
        temp_i = i
        temp_j = j
        for i_check in range(-1, 2):
            for j_check in range(-1, 2):
                if i + i_check >= 0 and i + i_check < r and j + j_check >= 0 and j + j_check < c:
                    if arr[i + i_check][j + j_check] == "M":
                        count += 1

        while not placed:
            for i in range(r):
                for j in range(c):
                    if arr[i][j] != "M":
                        arr[i][j] = "M"
                        placed = True
                        break
                if placed:
                    break
        arr[temp_i][temp_j] = "E" + str(count)
        first_clicked_m = False
        frame.destroy()
        frame_1.destroy()
        create_frame()
        create_frame_1()
    else:
        for i in range(r):
            for j in range(c):
                if arr[i][j] == "M":
                    btn_arr[i][j]["text"] = "M"
        for i in range(r):
            for j in range(c):
                if arr[i][j][0] ==  "E":
                    btn_arr[i][j]["command"] = ""
        lbl["text"] = "You lose!"

def pressed_e_1(i,j):
    global clicked
    if clicked <  r * c - mines:
        btn_arr[i][j]["text"] = arr[i][j][1]
        # btn_arr[i][j] = tk.Label(master = frame, width = 4, height = 2, relief = tk.SUNKEN, text = arr[i][j][1])
        # btn_arr[i][j].grid(row = i, column = j)
        btn_arr[i][j]["command"] = ""
        clicked += 1
    if clicked == r * c - mines:
        for i in range(r):
            for j in range(c):
                if arr[i][j] == "M":
                    btn_arr[i][j]["command"] = '"'
        lbl["text"] = "You win!"

def ok_new():
    if satisfied:
        new_frame.destroy()
        display()

def easy():
    global row, column , m, satisfied
    row = 5
    column = 5
    m = 8
    satisfied = True

def intermediate():
    global row, column , m, satisfied
    row = 10
    column = 10
    m = 40
    satisfied = True

def hard():
    global row, column , m, satisfied
    row = 16
    column = 16
    m = 100
    satisfied = True

def custom():
    global row, column , m, satisfied
    satisfied = True
    row = int(entry_c_h.get())
    column = int(entry_c_w.get())
    m = int(entry_c_m.get())
    if m < 0:
        lbl_error["text"] = "Negative mines??"
        satisfied = False
    elif m == 0:
        lbl_error["text"] = "Zero mines??"
        satisfied = False
    elif m > row * column and (row < 20 or column < 20 or row <= 0 or column <= 0):
        lbl_error["text"] = "There are only " + str(row * column) + " boxes"
        satisfied = False
    else:
        lbl_error["text"] = ""

    if row > 20 or column > 20:
        lbl_error_2["text"] = "Maximum height/width is 20\nWhy? idk"
        satisfied = False
    if row < 0 or column < 0:
        lbl_error_2["text"] = "Negative height/width??"
        satisfied = False
    if row == 0 or column == 0:
        lbl_error_2["text"] = "Zero height/width??"
        satisfied = False

newgame()
