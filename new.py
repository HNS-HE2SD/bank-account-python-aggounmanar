
class Client:
    def init(self, cin, firstName, lastName, tel=""):
        self.__CIN = cin
        self.__firstName = firstName
        self.__lastName = lastName
        self.__tel = tel
        
    def get_CIN ( self ) :
      return self . __CIN
    def get_firstName ( self ) :
      return self . __firstName
    def get_lastNAME ( self ) :
      return self . __lastName
    def get_tel ( self ) :
      return self . __tel

    def set_CIN ( self , CIN ) :
      self . __CIN = CIN
    def set_firstName ( self , firstName ) :
      self . __firstName = firstName
    def set_lastName ( self , lastName ) :
      self . __lastName = lastName
    def set_tel ( self , tel) :
      self . __tel = tel

   

    def display(self):
        print(f"CIN: {self.CIN}, Name: {self.firstName} {self.lastName}, Tel: {self.tel}")

class Account:
    __nbAccounts = 0  # static variable for sequential codes

    def init(self, owner):
        Account.__nbAccounts += 1
        self.code = Account.nbAccounts
        self.__balance = 0.0
        self.__owner = owner

    def get_code(self):
        return self.__code
    def get_balance(self):
        return self.__balance
    def get_owner(self): 
        return self.__owner

    def credit(self, amount, account=None):
        if account is None:
            self.__balance += amount
        else:
            self.__balance += amount
            account.debit(amount)

    def debit(self, amount, account=None):
        if self.__balance >= amount:
            self.__balance -= amount
            if account is not None:
                account.credit(amount)
        else:
            print("Insufficient balance.")

    def display(self):
        print(f"Account Code: {self.__code}")
        print(f"Owner: {self.owner.get_firstName()} {self.owner.get_lastName()}")
        print(f"Balance: {self.__balance} DA")

    @staticmethod
    def displayNbAccounts():
        print("Total accounts created:", Account.__nbAccounts)



class Client(Client): #extended client class to support multiple accounts
    def init(self, cin, firstName, lastName, tel=""):
        super().init(cin, firstName, lastName, tel)
        self.accounts = []  #list of accounts

    def listAccounts(self):
        if not self.accounts:
            print(f"{self.get_firstName()} {self.get_lastName()} has no accounts.")
        else:
            print(f"Accounts of {self.get_firstName()} {self.get_lastName()}:")
            for account in self.accounts:
                print(f"  - Account {account.get_code()} : {account.get_balance()} DA")



class Account(Account):#extended account class with transaction history and validation
    def init(self, owner):
        super().init(owner)
        self.__transactions = [] #transaction history
        owner.accounts.append(self)  
    
    def credit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive for credit.")
            return
        self._Account__balance += amount
        self.__transactions.append(f"CREDIT: +{amount} DA")
        print(f"Credited {amount} DA to Account {self.get_code()}.")

    
    def debit(self, amount):
        if amount <= 0:
            print("Error: Amount must be positive for debit.")
            return
        if self._Account__balance >= amount:
            self._Account__balance -= amount
            self.__transactions.append(f"DEBIT: -{amount} DA")
            print(f"Debited {amount} DA from Account {self.get_code()}.")
        else:
            print("Error: Insufficient balance for debit.")

    def transfer(self, amount, target_account):
        if amount <= 0:
            print("Error: Amount must be positive for transfer.")
            return
        if self._Account__balance >= amount:
            self._Account__balance -= amount
            target_account._Account__balance += amount
            self.__transactions.append(f"TRANSFER OUT: -{amount} DA to Account {target_account.get_code()}")
            target_account.__transactions.append(f"TRANSFER IN: +{amount} DA from Account {self.get_code()}")
            print(f"Transferred {amount} DA from Account {self.get_code()} to Account {target_account.get_code()}.")
        else:
            print("Error: Insufficient balance for transfer.")

    def displayTransactions(self):
        if not self.__transactions:
            print(f"No transactions for Account {self.get_code()}.")
        else:
            print(f"Transaction History for Account {self.get_code()}:")
            for t in self.__transactions:
                print("  ", t)

class SavingsAccount(Account): #savingAccount class
    def init(self, owner, interestRate):
        super().init(owner)
        self.__interestRate = interestRate 

    
    def addInterest(self):#interest rate
        interest = self.get_balance() * self.__interestRate / 100
        self.credit(interest)
        print(f"Added interest {interest} DA to Account {self.get_code()}.")