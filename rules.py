#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:47:08 2018

@author: theostelmaszyk
"""
import numpy as np

class Rules(object):

	def __init__(self):
		self.difficulty = 4
		self.game = np.shape([])

	def move_possible(self,row,column):
		try:
			if self.game[row,column]==0:
				return True
		except IndexError: #IndexError en dehors de la matrice
			return False
		return False

	def win_move(self,player):
		(row,column)=self.game.shape

		for currentColumn in range (0,column):
			if self.win_move_row_column(self.game[:,currentColumn],player) is True:
				return True
		for currentRow in range (0,row):
			if self.win_move_row_column(self.game[currentRow,:],player) is True:
				return True
		for currentRow in range (0,row):
			for currentColumn in range (0,column):
				if self.win_move_diagonal_from_one_cell(player,currentRow,currentColumn) is True:
					return True
		return False

	def win_move_diagonal_from_one_cell(self,player,rowTested,columnTested, bestLeft=0, bestRight=0): #Voir pour passer autre chose ()
		"""
		Cette méthode test dans une diagonale si il y a un coup gagnant
		"""
		
		(rowSize,columnSize)=self.game.shape
		
		if player=='A' or player=='a':
			playerNumber = 1
		if player=='B' or player=='b':
			playerNumber=-1


		if (bestLeft>=self.difficulty) or (bestRight>=self.difficulty):
			return True
		if (columnTested<0) or (columnTested>=columnSize) or (rowTested>=rowSize):
			return False
		
		if self.game[rowTested,columnTested]==0 or self.game[rowTested,columnTested]==playerNumber*-1:
			return self.win_move_diagonal_from_one_cell(player,rowTested+1,columnTested+1,0,0) \
				or self.win_move_diagonal_from_one_cell(player,rowTested+1,columnTested-1,0,0)
		if self.game[rowTested,columnTested]==playerNumber:
			return self.win_move_diagonal_from_one_cell(player,rowTested+1,columnTested+1,bestLeft,bestRight+1) \
				or self.win_move_diagonal_from_one_cell(player,rowTested+1,columnTested-1,bestLeft+1,bestRight)
		
		return False


	def win_move_row_column(self,toTest,player, best=0,increment=0):
		"""
		Cette méthode test dans une ligne il y a un coup gagnant
		"""
		if player=='A' or player=='a':
			playerNumber = 1

		if player=='B' or player=='b':
			playerNumber=-1


		if best>=self.difficulty:
			return True
		if increment>=toTest.size:
			return False
		
		if toTest[increment]==0 or toTest[increment]==playerNumber*-1:
			return self.win_move_row_column(toTest,player,0,increment+1)
		if toTest[increment]==playerNumber:
			return self.win_move_row_column(toTest,player,best+1,increment+1)
		return False



