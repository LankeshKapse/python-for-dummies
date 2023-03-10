import unittest
from pathlib import Path
import sys
from oop.calculator import Calc as c


class TestCalc(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        print("Setup called...!")
        pass
    
    
    def test_add(self):
        num1 = 10
        num2 = 20
        sum = c.add(num1= num1, num2= num2)
        self.assertEqual(sum,30)
        

if __name__ == "__main__":
     unittest.main()