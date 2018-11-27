#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:49:19 2018

@author: theostelmaszyk
"""

import unittest
import numpy as np
from rules import *

class RulesTest(unittest.TestCase):

    def test_move_possible(self):
        r=Rules()
        r.game = np.zeros((4,6),dtype=int)
        r.game[3,4] = 1

        #un coup  impossible est détecté
        self.assertFalse(r.move_possible(3,4))
        self.assertFalse(r.move_possible(3,7))

         #un coup possible est détecté
        self.assertTrue(r.move_possible(1,1))

    def test_win_move_row(self):
        """
        Test un mouvement sur une même ligne"
        """
        r=Rules()
        gameCreated = np.zeros((4,6),dtype=int)
        gameCreated[2,[1,2,3]] = 1
        self.assertFalse(r.win_move_row_column(gameCreated[2,:],'A'))
        self.assertFalse(r.win_move_row_column(gameCreated[2,:],'B'))
        gameCreated[2,0] = 1
        self.assertTrue(r.win_move_row_column(gameCreated[2,:],'A'))
        self.assertFalse(r.win_move_row_column(gameCreated[2,:],'B'))

    def test_win_move_column(self):
        """
        Test un mouvement sur une même colonne
        """        
        r=Rules()
        gameCreated = np.zeros((4,6),dtype=int)
        gameCreated[[1,2,3],2] = 1
        self.assertFalse(r.win_move_row_column(gameCreated[:,2],'A'))
        self.assertFalse(r.win_move_row_column(gameCreated[2,:],'B'))
        gameCreated[0,2] = 1
        self.assertTrue(r.win_move_row_column(gameCreated[:,2],'A'))
        self.assertFalse(r.win_move_row_column(gameCreated[2,:],'B'))

    def test_win_move_diagonal_from_one_cell_Right(self):
        """
        Test le tableau entier pour un coup gagnant joueur A
        """        
        r=Rules()
        r.game = np.zeros((4,6),dtype=int)
        r.game[0,0] = 1
        r.game[1,1] = 1
        r.game[2,2] = 1
        self.assertFalse(r.win_move_diagonal_from_one_cell('A',0,0))
        self.assertFalse(r.win_move_diagonal_from_one_cell('B',0,0))
        r.game[3,3] = 1
        self.assertTrue(r.win_move_diagonal_from_one_cell('A',0,0))
        self.assertFalse(r.win_move_diagonal_from_one_cell('B',0,0))

    def test_win_move_diagonal_from_one_cell_Left(self):
        """
        Test le tableau entier pour un coup gagnant joueur A
        """        
        r=Rules()
        r.game = np.zeros((4,6),dtype=int)
        r.game[3,0] = 1
        r.game[2,1] = 1
        r.game[1,2] = 1
        self.assertFalse(r.win_move_diagonal_from_one_cell('A',0,3))
        self.assertFalse(r.win_move_diagonal_from_one_cell('B',0,3))
        r.game[0,3] = 1
        self.assertTrue(r.win_move_diagonal_from_one_cell('A',0,3))
        self.assertFalse(r.win_move_diagonal_from_one_cell('B',0,3))

    def test_win_move_A(self):
        """
        Test le tableau entier pour un coup gagnant joueur A
        """        
        r=Rules()
        r.game = np.zeros((4,6),dtype=int)
        r.game[[1,2,3],2] = 1
        self.assertFalse(r.win_move('A'))
        self.assertFalse(r.win_move('B'))
        r.game[0,2] = 1
        self.assertTrue(r.win_move('A'))
        self.assertFalse(r.win_move('B'))

    def test_win_move_B(self):
        """
        Test le tableau entier pour un coup gagnant joueur B
        """        
        r=Rules()
        r.game = np.zeros((4,6),dtype=int)
        r.game[[1,2,3],2] = -1
        self.assertFalse(r.win_move('A'))
        self.assertFalse(r.win_move('B'))
        r.game[0,2] = -1
        self.assertFalse(r.win_move('A'))
        self.assertTrue(r.win_move('B'))

        
if __name__ == '__main__':
    unittest.main()
