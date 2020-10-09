import datetime
import pytz


class Account:
  """ Simple account class with balance """

  @staticmethod
  def _currentTime():
    utcTime = datetime.datetime.now()
    return pytz.utc.localize(utcTime)

  def __init__(self, name, balance):
    self._name = name
    self._balance = balance
    self._transactionList = [(Account._currentTime(), balance)]
    print('Account created for ' + self._name)
    self.showBalance()

  def deposit(self, amount):
    if amount > 0:
      self.balance += amount
      self.showBalance()
      self._transactionList.append((Account._currentTime(), amount))

  def withdraw(self, amount):
    if 0 < amount <= self.balance:
      self.balance -= amount
      self._transactionList.append((Account._currentTime(), -amount))
      self.showBalance()
    else:
      print('The amount must be greater than zero and no more than your account balance')
  
  def showBalance(self):
    print('Balance is {}'.format(self._balance))
  
  def showTransactions(self):
    for date, amount in self._transactionList:
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

  steph = Account('Steph', 800)
  steph.deposit(100)
  steph.withdraw(200)
  steph.showTransactions()
