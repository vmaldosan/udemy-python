import datetime
import pytz

class Account:
  """ Simple account class with balance """

  @staticmethod
  def _currentTime():
    utcTime = datetime.datetime.now()
    return pytz.utc.localize(utcTime)

  def __init__(self, name, balance):
    self.name = name
    self.balance = balance
    self.transactionList = []
    print('Account created for ' + self.name)

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      self.showBalance()
      self.transactionList.append((Account._currentTime(), amount))

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      self.transactionList.append((Account._currentTime(), -amount))
      self.showBalance()
    else:
      print('The amount must be greater than zero and no more than your account balance')
  
  def showBalance(self):
    print('Balance is {}'.format(self.balance))
  
  def showTransactions(self):
    for date, amount in self.transactionList:
      if amount > 0:
        tranType = 'deposit'
      else:
        tranType = 'withdrawal'
        amount *= -1
      print('{:6} {} on {} (local time was {})'.format(amount, tranType, date, date.astimezone()))


if __name__ == '__main__':
  tim = Account('Tim', 0)
  tim.showBalance()

  tim.deposit(1000)
  tim.withdraw(400)
  tim.withdraw(2000)

  tim.showTransactions()
