class User:
    def __init__(self, first_name, last_name, email, is_rewards_member, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = gold_card_points
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

tony = User("tony", "oliveraz", "someemail.com", False, 0)

addie = User("addie", "oliveraz", "someemail.com", False, 0)
kay = User("addie", "oliveraz", "someemail.com", False, 0)

tony.display_info().enroll().spend_points(50)

addie.display_info().enroll().spend_points(120)