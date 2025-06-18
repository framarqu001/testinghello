"""
Test module for calculator.py
"""
import unittest
from calculator import add

class TestCalculator(unittest.TestCase):
    """Test cases for calculator functions."""
    
    def test_add_integers(self):
        """Test adding two integers."""
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        
    def test_add_floats(self):
        """Test adding two floating point numbers."""
        self.assertAlmostEqual(add(1.5, 2.5), 4.0)
        self.assertAlmostEqual(add(-1.5, 1.5), 0.0)
        
    def test_add_mixed(self):
        """Test adding integer and float."""
        self.assertAlmostEqual(add(1, 2.5), 3.5)

if __name__ == "__main__":
    unittest.main()