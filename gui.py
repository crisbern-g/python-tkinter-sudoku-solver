import tkinter as tk
from tkinter.constants import CENTER
from tkinter.font import Font
from tkinter import messagebox
import solver

board = [
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
    [0,0,0,0,0,0,0,0,0], 
]

fgColors = [
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
    ['black','black','black','black','black','black','black','black','black'], 
]


class EntryBox(tk.Entry):
    def __init__(self, root, row, column, number, bgColor, fgColor):
        self.row = row
        self.column = column
        self.number = number
        self.bgColor = bgColor
        self.fgColor = fgColor
        tk.Entry.__init__(self, root)
        self.grid(row=self.row, column=self.column)
        self.config(
            width=4, 
            background=self.bgColor,
            font=Font(family='Impact', size=20), 
            justify=CENTER, 
            relief='solid',
            foreground=self.fgColor
            )
        self.insert(0, self.number)
        self.bind('<KeyRelease>', self.getGridContent)

    def getGridContent(self, event):
        gridInfo = self.grid_info()
        row = gridInfo['row']
        column = gridInfo['column']
        
        try:
            if len(self.get()) > 1 or self.get() == '0':
                messagebox.showerror(title='Invalid Value', message='You entered an invalid value')
                self.delete(0, 'end')
            else:
                board[row][column] = int(self.get())
        except ValueError:
            if self.get() != '':
                messagebox.showerror(title='Invalid Value', message='You entered an invalid value')
            self.delete(0, 'end')
            board[row][column] = 0

def createGrid():
    for row in range(9):
        for column in range(9):
            box_row = row // 3
            box_column = column //3

            if (box_row == 0 and box_column == 0) or (box_row == 0 and box_column == 2) or (box_row == 1 and box_column == 1) or (box_row == 2 and box_column == 0) or (box_row == 2 and box_column == 2):
                color= 'gray90'
            else:
                color = 'white'

            number = board[row][column]
            if number == 0:
                number = ''
                fgColors[row][column] = 'black'
            
            EntryBox(boardPanel, row, column, number, color, fgColors[row][column])

def clearGrid():
    for row in range(9):
        for column in range(9):
            board[row][column] = 0
            fgColors[row][column] = 'black'
    
    createGrid()


def solvePuzzle():
    puzzleValidity = True

    for row in range (0, 9):
        for column in range(0,9):
            value = board[row][column]

            if value != 0:
                if not solver.isValid(board, value, (row, column)):
                    puzzleValidity = False

    if puzzleValidity:
        for row in range (0, 9):
            for column in range(0,9):
                if board[row][column] == 0:
                    fgColors[row][column] = 'green4'
                else:
                    fgColors[row][column] = 'black'

        solver.solve(board)
        createGrid()
    else:
        messagebox.showerror(message='Invalid Puzzle')
        
root = tk.Tk()
root.resizable(False, False)
root.title('Sudoku Solver')

boardPanel = tk.PanedWindow(root, relief='solid')
boardPanel.grid(column=0, row=0, rowspan=1, columnspan=1)

buttonPanel = tk.PanedWindow(root, relief='solid')
buttonPanel.grid(column=0, row=1)

createGrid()

solveButton = tk.Button(buttonPanel, width=15, text='Solve', background='yellow', relief='flat' ,command=solvePuzzle)
solveButton.grid(row=0, column=0,sticky='W', rowspan=1)

clearButton = tk.Button(buttonPanel, width=15, text='Clear', background='red', relief='flat' ,command=clearGrid)
clearButton.grid(row=0, column=1,sticky='W', rowspan=1)

root.mainloop()
