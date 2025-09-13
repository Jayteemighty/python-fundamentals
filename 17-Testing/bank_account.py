import unittest

class BankAccount:
  def __init__(self, initial_balance=0):
    self.balance = initial_balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError('Deposit amount must be positive')
    self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError('Withdrawal amount must be positive')
    if amount > self.balance:
      raise ValueError('Insufficient funds')
    self.balance -= amount

MyAccount = BankAccount()
MyAccount.initial_balance = 100

class TestBankAcccount(unittest.TestCase):
    def setUp(self):
        self.account = BankAccount(100)
    
    def tearDown(self):
        self.account = None
    
    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 100)
    
    def test_deposit_positive_amount(self):
        self.account.deposit(50)
        self.assertEqual(self.account.balance, 150)
    
    def test_deposit_zero_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit(0)

if __name__ == '__main__':
    unittest.main()
