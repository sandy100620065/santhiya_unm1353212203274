class BankAccount:
  def __init__(self,accountnumber,accountholdername,initialbalance=0.0):
    self.__accountnumber=accountnumber
    self.__accountholdername=accountholdername
    self.__accountbalance=initialbalance
  def deposit(self,amount):
    if amount>0:
      self.__accountbalance+=amount
      print("Deposited rupees{}.New balance:rupees{}".format(amount,self.__accountbalance))
    else:
      print("Invalid deposit amount..")
  def withdraw(self,amount):
    if amount>0 and amount<=self.__accountbalance:
      self.__accountbalance-=amount
      print("withdrawal amount:",amount)
    else:
      print("Invalid withdrawal amount or insufficient balance:")
  def displaybalance(self):
    print("Account balance for {} (Account   #{}):rupees{}".format(self.__accountholdername,self.__accountnumber,self.__accountbalance))

account=BankAccount(accountnumber="212347689",
                   accountholdername="Vedha",
                   initialbalance=1000.0)

account.displaybalance()
account.deposit(500.0)
account.withdraw(200.0)
account.displaybalance()