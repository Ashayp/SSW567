# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')
    
    def testNegativeInput(self):
        self.assertEqual(classifyTriangle(5,-3,4),'InvalidInput','length cannot be negative')

    def testZeroInput(self):
        self.assertEqual(classifyTriangle(5,0,4),'InvalidInput','length cannot be zero')

    def testScaleneInputA(self):
        self.assertEqual(classifyTriangle(5,6,4),'Scalene','5,6,4 is a Scalene triangle')

    def testIsocelesInput(self):
        self.assertEqual(classifyTriangle(5,4,4),'Isoceles','5,4,4 is an Isoceles triangle')

    def testScaleneInputB(self):
        self.assertEqual(classifyTriangle(15,6,4),'NotATriangle','15,6,4 is not a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

