#DATE - 25/2/2025

#Dice
from random import randint, choice, sample


class Dice:
    def __init__(self, sides = 6):
        self.sides = sides


    def roll_dice(self):
        return randint(1,6)


class Ten_sided_dice(Dice):
    def __init__(self, sides = 10):
        super().__init__(sides)


    def roll_dice(self):
        return randint(1,10)


test = Dice()

print(test.roll_dice())

test = Ten_sided_dice()
print(test.roll_dice())





#Lottery

from random import sample
class Lottery:
    def __init__(self):
        self.ticket = [1,2,3,4,5,6,7,"A","B","C","E","F",8,9,10]
        self.person_ticket = sample(self.ticket, 4)
        self.wining_ticket = sample(self.ticket, 4)

    def generate_wining_ticket(self):
        return f"\n Today wining ticket last 4 digit is {self.wining_ticket}"

    def check_match_ticket(self):
        print(f"\n Wining Ticket last 4 digit = {self.wining_ticket} | Person Ticket last 4 digit {self.person_ticket}")

        if set(self.wining_ticket) == set(self.person_ticket):
            return f"\n Congratulations you have won the lottery"
        elif set(self.wining_ticket) != set(self.person_ticket):
            return f"\n Sorry Better luck next time"



test = Lottery()
print(test.generate_wining_ticket())
print(test.check_match_ticket())