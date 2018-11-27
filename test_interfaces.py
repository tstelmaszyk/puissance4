#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 12:49:19 2018

@author: theostelmaszyk
"""

import unittest
import numpy as np
from interfaces import *

class InterfacesTest(unittest.TestCase):

    def test_click(self):
    	fenetre = Tk()
    	i = Interface(fenetre)
    	self.assertEqual(i.game.move_possible(0, 1),True)
    	i.click(0, 1)
    	self.assertEqual(i.game.move_possible(0, 1),True)