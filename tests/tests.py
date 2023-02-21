import unittest
# imort the algorithms to test and the boards to use in the tests
from src.algorithm.algorithm import (a_star, beam_search, breadth_first_search,
                                     depth_first_search)
from src.model.board import Board

""" test ideas: 
- test algorithms against predetermined boards and compare the my solved board to the algorithms
- test move works? on boards with just 1 vehicle test different sizes and orientations?
- 

"""
class TestRushHour(unittest.TestCase):
        def test(self):
            return