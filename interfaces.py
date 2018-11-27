from tkinter import *
from grid import *

class Interface(Frame):
    
    def __init__(self, window, row_configured=6, column_configured=6):
        
        self.game = Grid(row_configured, column_configured)
        self.clickCpt = 0

        self.window = window

        self.cellsWidth = 10
        self.cellsHeight = 5


        Frame.__init__(self)

        #Creation du damier 
        self.cells = list()
        for rowCpt in range(row_configured):
            self.cells.append(list())
            for columnCpt in range(column_configured):
                self.cells[rowCpt].append(Button(self.window, width=self.cellsWidth, height=self.cellsHeight, \
                #self.cells[rowCpt].append(Radiobutton(self.window, indicatoron=0, width=self.cellsWidth, height=self.cellsHeight, \
                    command=lambda rowClicked=rowCpt, columnClicked=columnCpt: self.click(rowClicked, columnClicked)))
                self.cells[rowCpt][columnCpt].grid(row=rowCpt, column=columnCpt)

    def click(self, rowClicked, columnClicked):
        if self.clickCpt%2 ==0:
            [rowChanged, columnChanged]=self.game.new_move(rowClicked, columnClicked,'A')
            if [rowChanged, columnChanged] != [-1, -1]:
                self.clickCpt = self.clickCpt+1
                self.cells[rowChanged][columnChanged]['highlightbackground']='yellow'
                #self.cells[rowClicked][columnClicked]['bg']='green'
                if self.game.win_move('A')==True:
                    print('Victoire joueur 1')
        else :
            [rowChanged, columnChanged]=self.game.new_move(rowClicked, columnClicked,'B')
            if [rowChanged, columnChanged] != [-1, -1]:
                self.clickCpt = self.clickCpt+1
                self.cells[rowChanged][columnChanged]['highlightbackground']='red'
                #self.cells[rowClicked][columnClicked]['bg']='red'
                if self.game.win_move('B')==True:
                    print('Victoire joueur 2')

        print(self.game.game)

