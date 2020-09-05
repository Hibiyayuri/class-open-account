#銀行開戶class練習
class Customer():
    def __init__(self,ID,birthday,address): #id的返回值是物件的記憶體地址，保險起見就大寫
        self.ID=ID
        self.birthday=birthday
        self.address=address
        self.haveAccount=Account()
    
class Account():
    def __init__(self,accNO,date,balance):
        self.accNO=accNO
        self.date=date
        self.balance=balance
        self.canTransaction=Transaction()

class SavingAcc(Account):
    def __init__(self,accNO,date,balance,lowerBound):
        Account.__init__(self,accNO,date,balance)
        self.lowerBound=lowerBound
        
class CheckingAcc(Account):
    def __init__(self,accNO,date,balance,checkNum):
        Account.__init__(self,accNO,date,balance)
        self.checkNum=checkNum
        
class FixedAcc():
    def __init__(self,accNO,date,balance,interest,period):
        Account.__init__(self,accNO,date,balance)
        self.interest=interest
        self.period=period
        
class Transaction():
    def __init__(self,tid,tDate):
        self.tid=tid
        self.tDate=tDate
        self.account=Account

class Deposit(Transaction):
    def __init__(self,tid,tDate,dAmount):
        Transaction.__init__(self,tid,tDate)
        self.dAmount=dAmount
        
class Withdraw(Transaction):
    def __init__(self,tid,tDate,wAmount):
        Transaction.__init__(self,tid,tDate)
        self.wAmount=wAmount
        
class Transfer(Transaction):
    def __init__(self,tid,tDate,tAmount,bankNo,account):
        Transaction.__init__(self,tid,tDate)
        self.tAmount=tAmount
        self.bankNo=bankNo
        self.account=account
