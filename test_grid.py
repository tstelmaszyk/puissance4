#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:49:19 2018

@author: theostelmaszyk
"""

import unittest
import numpy as np
from grid import *

class GridTest(unittest.TestCase):

    def test_emptyGrid (self):
        gameCreated = Grid(6,5)
        self.assertEqual(np.linalg.norm(gameCreated.game),0)
        self.assertEqual(gameCreated.game.shape,(6,5))

    def test_reset_grid(self):
        gameCreated = Grid(6,5)
        gameCreated.game[3,3] = 1 
        gameCreated.reset_grid()
        self.assertEqual(np.linalg.norm(gameCreated.game),0)
        self.assertEqual(gameCreated.game.shape,(6,5))


    def test_change_cell_value (self):
        """Par le joueur A"""
        gameCreated = Grid(6,5)
        gameCreated.change_cell_value(3,3,'A')
        self.assertEqual(gameCreated.game[3,3],1) 
        self.assertEqual(np.linalg.norm(gameCreated.game),1)
        
        """Par le joueur B"""
        Grid.__init__(gameCreated,6,5)
        gameCreated.change_cell_value(3,3,'B')
        self.assertEqual(gameCreated.game[3,3],-1)
        self.assertEqual(np.linalg.norm(gameCreated.game),1)

    def test_give_row_from_column (self):
        gameCreated = Grid(6,5)
        gameCreated.game[[4,5],0] = 1
        gameCreated.game[3,0] = -1
        self.assertEqual(gameCreated.give_row_from_column(0),2)

    def test_new_move (self):
        gameCreated = Grid(6,5)
        gameCreated.game[[4,5],0] = 1
        gameCreated.game[3,0] = -1
        self.assertEqual(gameCreated.new_move(0,0,'A'),[2,0])
        self.assertEqual(gameCreated.game[2,0],1)


if __name__ == '__main__':
    unittest.main()
