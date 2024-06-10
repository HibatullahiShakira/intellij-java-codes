import unittest
from Task import Task

class TestTask(unittest.TestCase):
    def test_that_the_function_length(self):
        task1 = Task("shakira")
        self.assertEqual(8, task1.length_return([2,3,4,5,6,7,8,58]))