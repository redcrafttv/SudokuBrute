#-------------------------------------------------------------------------------
# Name:        sudokubrute
# Purpose:
#
# Author:      nikolas.heise
#
# Created:     12/05/2021
# Copyright:   (c) nikolas.heise 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

class Cell:
    def __init__(self, x, y, v):
        self.x = x
        self.y = y
        self.value = v
        if (v == "x"):
            self.possibles = ["1","2","3","4","5","6","7","8","9"]
        else:
            self.possibles = []

field = []


def load_field():
    file = open(file="examplepuzzle.txt", mode="r")
    line = file.readline()
    y = 1
    while not line == "":
        line = line[:-1]
        for i in range(len(line)):
            field.append(Cell(i + 1, y, line[i]))
        y += 1
        line = file.readline()

def main():
    load_field()
    changes = True

    while changes:
        changes = False

        # Update possible values

        # Collumns
        for x in range(9): # für alle neun spalten
            for cell in field: # überprüfe jede cell im field
                if cell.x == x+1 and cell.value != "x": # und wenn sie kein value hat und zur spalte gehört
                    for column_member in field: # suche alle cellen
                        if column_member.x == x+1: # filter nach spaltenmitglieder
                            if (column_member.possibles.count(cell.value)):
                                column_member.possibles.remove(cell.value) # entferne impossible values


        # Rows
        for y in range(9): # für alle neun spalten
            for cell in field: # überprüfe jede cell im field
                if cell.y == y+1 and cell.value != "x": # und wenn sie kein value hat und zur spalte gehört
                    for row_member in field: # suche alle cellen
                        if row_member.y == y+1: # filter nach spaltenmitglieder
                            if (row_member.possibles.count(cell.value)):
                                row_member.possibles.remove(cell.value) # entferne impossible values

        # check possible values of every cell
        for cell in field:
            if(len(cell.possibles) == 1):
                cell.value = cell.possibles[0]
                cell.possibles = []
                changes = True
        continue


    # print result
    for y in range(9):
        result_row = []
        for cell in field:
            if cell.y == y+1:
                result_row.append(cell.value)
        print(result_row)


if __name__ == '__main__':
    main()
