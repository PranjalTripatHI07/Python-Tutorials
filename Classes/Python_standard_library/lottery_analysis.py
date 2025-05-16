from random import sample
class Lottery:
    def __init__(self, player_name):
        self.ticket_list = [1,2,3,4,5,6,7,8,9,10,"A","B","C","F","H"]
        self.player_name = player_name
        self.winning_ticket = sample(self.ticket_list, 4)
        self.player_ticket = sample(self.ticket_list, 4)

    def generate_winning_ticket(self):
        return f"\n Today winning ticket no is :- {self.winning_ticket}"

    def check_winning_ticket(self):
        if set(self.player_ticket) == set(self.winning_ticket):
            return f"\n Congratulation {self.player_name.title()} you won the lottery"
        else:
            return f"\n Sorry {self.player_name.title()} better luck next time and your ticket is:- {self.player_ticket}"


    def lottery_analysis(self):
        print("\n No of chances to get successful")

        chances = 0
        while True:
            chances += 1
            new_ticket = set(sample(self.ticket_list, 4))
            if new_ticket == set(self.winning_ticket):
                break
        return f"\n The no chances you have to win the lottery is:- {chances}"



test1 = Lottery("willie van")
print(test1.generate_winning_ticket())
print(test1.check_winning_ticket())
print(test1.lottery_analysis())



#Another

from random import sample


class Lottery:
    def __init__(self, player_name):
        self.ticket_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "A", "B", "C", "F", "H"]
        self.player_name = player_name
        self.winning_ticket = sample(self.ticket_list, 4)
        self.player_ticket = sample(self.ticket_list, 4)

    def generate_winning_ticket(self):
        return f"\nToday's winning ticket is: {self.winning_ticket}"

    def check_winning_ticket(self):
        # Decide if order matters - here using sets (order doesn't matter)
        if set(self.player_ticket) == set(self.winning_ticket):
            return f"\nCongratulations {self.player_name.title()}, you won the lottery!"
        else:
            return f"\nSorry {self.player_name.title()}, better luck next time. Your ticket was: {self.player_ticket}"

    def lottery_analysis(self):
        print("\nCalculating chances to win...")

        # For safety, limit the maximum iterations
        max_attempts = 1_000_000
        chances = 0

        while chances < max_attempts:
            chances += 1
            new_ticket = set(sample(self.ticket_list, 4))
            if new_ticket == set(self.winning_ticket):
                break

        if chances == max_attempts:
            return f"\nExceeded maximum attempts ({max_attempts}). Winning is extremely rare!"

        return f"\nYou would need approximately {chances} attempts to win the lottery with these odds."


# Test the class
test1 = Lottery("willie van")
print(test1.generate_winning_ticket())
print(test1.check_winning_ticket())
print(test1.lottery_analysis())