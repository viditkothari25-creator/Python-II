class bank:
    def __init__(self,account_number,balance):
        self.account_number = account_number
        self.balance = 1000

    def deposit(self,amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")

my_account = bank("123456789", 0)
my_account.deposit(500)
my_account.withdraw(200)

class library:
    def __init__(self,book_name,author):
        self.book_name = book_name
        self.author = author
    
    def availability(self,book_name):
        print(f"The book '{book_name}' is available in the library.")

my_book = library("Rich dad poor dad", "Robert kiyosaki")
my_book.availability("Rich dad poor dad")