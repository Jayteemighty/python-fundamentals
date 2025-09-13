import unittest # start by importing unittest

def add(a, b):
  return a + b

class TestAddition(unittest.TestCase): # Create TestCase instance
  # Define the first unit test
  def test_add(self): # test methods should be prefixed with "test_"
    result = add(3, 4)

    # Define the expected result
    expected_result = 7
    self.assertEqual(result, expected_result)

if __name__ == '__main__':
  unittest.main()