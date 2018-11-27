#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:47:08 2018

@author: theostelmaszyk
"""

from rules import * 

class Grid(Rules):
	"""
	Hérite de la classe Rules
	"""

	def __init__(self,row=6,column=6):
		Rules.__init__(self)
		self.game = np.zeros((row,column),dtype=int)
		self.row = row
		self.column = column

	def reset_grid(self):
		self.game = np.zeros(self.game.shape ,dtype=int)

	def change_cell_value (self,row,column,joueur):
		"""
		Méthode qui change la valeure d'une cellule de la grille
		Si une cellule est à 0 elle n'a jamais été jouée
		Si une cellule est à 1, elle a été jouée par le joueur A
		Si une cellule est à -1, elle a été jouée par le joueur B
		"""
		if self.move_possible(row,column):
			if joueur == 'A':
				self.game[row,column]=1
				return True
			if joueur == 'B':
				self.game[row,column]=-1
				return True
			return False

	def give_row_from_column (self,targetColumn):

		currentRow = self.game.shape[0]-1

		while (self.game[currentRow,targetColumn]!=0) and (currentRow>0):
			currentRow = currentRow-1
		return currentRow

	def new_move(self,row,column,joueur):
		rowComputed = self.give_row_from_column(column)
		if (self.change_cell_value(rowComputed,column,joueur)):
			return [rowComputed,column]
		return [-1,-1]
