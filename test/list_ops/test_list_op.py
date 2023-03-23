import unittest
from pathlib import Path
import sys
import os
from oop.calculator import Calc as c


class TestCalc(unittest.TestCase):
    @classmethod
    def setUp(cls) -> None:
        print("Setup called...!")
        for path in sys.path:
            if('python-for-dummies' in  path and '.venv' not in path):
                print(path)
        
    
    
    def test_add(self):
        num1 = 10
        num2 = 20
        
        sum = c.add(num1= num1, num2= num2)
        self.assertEqual(30,30)
        
        # print(f"env {os.environ['PATH']}")
        

if __name__ == "__main__":
     unittest.main()