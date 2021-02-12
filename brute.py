#-------------------------------------------------------------------------------
# Name:        sudokubrute
# Purpose:     Enumeration of all possible values and finally solving
#
# Author:      nikolas.heise
#
# Created:     10/02/2021
# Copyright:   (c) nikolas.heise 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import tkinter as tk

root = tk.Tk()

ui_grid = []
debug_btn = None


def print_spacer():
    print("------------------------------------------------------------")

def get_value(row, col):
    return ui_grid[row - 1][col - 1].get()

def clear_value(row, col):
    ui_grid[row - 1][col - 1].delete(0, len(get_value(row, col)))

def set_value(row, col, value):
    clear_value(row, col)
    ui_grid[row - 1][col - 1].insert(0, value)

def print_values():
    print_spacer()
    for i in ui_grid:
        out_row = []
        for j in i:
            out_row.append(j.get())
        print(out_row)
    print_spacer()

def get_row(row_index):
    result = []
    for cell in ui_grid[row_index - 1]:
        result.append(cell.get())
    return result

def get_column(col_index):
    result = []
    for row in ui_grid:
        result.append(row[col_index - 1].get())
    return result




def is_value_possible(row, col, value):
    if get_row(row).count(value) > 0:
        return False
    if get_column(col).count(value) > 0:
        return False
    return True

def calculate_possible_values():
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if is_value_possible(i+1, j+1, str(k+1)):
                    print(str(i+1) + " " + str(j+1) + " ;" + str(k) + " possible: " + str(is_value_possible(i+1, j+1, str(k+1))))








def debug_cmd():
    calculate_possible_values()

def load_cmd():
    file = open(file="save.txt")
    line = file.readline()
    x = 1
    y = 1

    while not line == "":
        line = line.replace("\n", "")
        print(len(line))
        print(line[1])
        #len(line)
        for char in line:
            print(str(x) + " " + char)
            #print(y)
            #print(x)
            #print(line(x))
            if line[x -1] == "x":
                set_value(row=y, col=x, value="")
            else:
                set_value(row=y, col=x,  value=line[x - 1])
            x += 1
        y += 1
        line = file.readline()
    pass

def save_cmd():
    file = open(file="save.txt", mode="w")
    for i in ui_grid:
        for j in i:
            if (not j.get() == ""):
                file.write(j.get())
            else:
                file.write("x")
        file.write("\n")
    file.close()
    pass

def create_ui(root: tk.Tk):
    for r in range(9):
        row = []
        for c in range(9):
            row.append(tk.Entry(root, width=3))
            row[c].grid(row=r,column=c)
        ui_grid.append(row)
    debug_btn = tk.Button(root, text="Debug", command=debug_cmd)
    debug_btn.place(x=200, y=3)

    load_btn = tk.Button(root, text="Load", command=load_cmd)
    load_btn.place(x=200, y=33)

    load_btn = tk.Button(root, text="Save", command=save_cmd)
    load_btn.place(x=200, y=63)




def main():
    create_ui(root=root)
    root.geometry("300x250")
    root.mainloop()


if __name__ == '__main__':
    main()
