class BankAccount:
    all_accounts = []

    @classmethod
    def display_account(cls,):
        for account in cls.all_accounts:
            account.display_account_info()
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        print("you are depositing " + str(amount) + " dollars into your account")
        self.balance += self.balance + amount
        print("your balance is now " + str(self.balance))
        return self
    def withdraw(self, amount):
        print("You are taking out " + str(amount) + " from your account")
        if self.balance < amount:
            print("You do not have enough to do this, we are charging your account $5")
            self.balance -= 5
            print(self.balance)
        elif self.balance > amount:
            self.balance = self.balance - amount
        print("Your balance is now " + str(self.balance))
        return self
    def display_account_info(self):
        print(self.int_rate, self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.int_rate * self.balance)
            print(self.balance)
            return self

class User:
    def __init__(self, first_name, last_name, email, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
        self.savings = BankAccount(.5, 100)
        self.checking = BankAccount(int_rate=.1, balance=100)
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.is_rewards_member, self.gold_card_points)
        return self
    def enroll(self):
        if(self.is_rewards_member == False):
            print("Oh it seems you are not a member yet! We can change that!")
            self.is_rewards_member = True
            print("There you GO! Here are some coins for you!")
            self.gold_card_points += 200
            print(self.gold_card_points)
            return self
    def spend_points(self, amount):
        print(self.gold_card_points)
        self.gold_card_points = self.gold_card_points - amount
        print(self.gold_card_points) 
        return self
    def make_deposit(self, amount):
        print("You are going to make a deposit " + str(amount) + " into your account")
        self.checking.balance += self.checking.balance + amount
        print(self.checking.balance)
        return self
    def make_withdraw(self, amount):
        print("You are going to make a withdrawl " + str(amount) + " into your account")
        self.checking.balance = self.checking.balance - amount
        print(self.checking.balance)
        return self
    def user_account_balance(self):
        print("---------------")
        print("User: " + self.first_name + " Checking Balance: " + str(self.checking.balance))
        print("User: " + self.first_name + " Savings Balance: " + str(self.savings.balance))
        return self
    def move_money(self, amount, other_user):
        print("You are cool for sending some money to a friend!")
        print("You are moving " + str(amount) + " to your " + str(other_user.first_name) + " friend's account!")
        self.checking.balance = self.checking.balance - amount
        other_user.checking.balance += other_user.checking.balance + amount
        print(user1.checking.balance)
        print(user2.checking.balance)
user1 = User("tony", "o", "email.com", False, 0)

user2 = User("Ogre", "Ogre", "email.com", False, 0)

user1.make_deposit(100)

user1.make_withdraw(200)

user1.user_account_balance()

user1.move_money(10, user2)