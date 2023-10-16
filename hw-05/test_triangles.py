import unittest
from classify_triangle import classify_triangle

class TestTriangles(unittest.TestCase):
    
    def test_right_triangle_a(self):
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def test_right_triangle_b(self):
        self.assertEqual(classify_triangle(4, 3, 5), 'Right', '4,3,5 is a Right triangle')

    def test_equilateral_triangle_a(self):
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def test_equilateral_triangle_b(self):
        self.assertEqual(classify_triangle(10, 10, 10), 'Equilateral','10,10,10 is an Equilateral')

    def test_not_a_triangle_a(self):
        self.assertEqual(classify_triangle(10, 15, 30), 'Not a triangle', 'is not a triangle')

    def test_scalene_triangle(self):
        self.assertEqual(classify_triangle(20, 15, 30), 'Scalene','20,15,30 is a Scalene triangle')

    def test_neg_inputs(self):
        self.assertNotEqual(classify_triangle(-10, 15, 30), 'Scalene', 'Input cannot be negative')

    def test_all_neg_inputs(self):
        self.assertNotEqual(classify_triangle(-10, -10, -10), 'Right', 'Input cannot be negative')

    def test_zero_input(self):
        self.assertEqual(classify_triangle(0, 1, 1), 'Not a triangle', 'Side is zero')



if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
