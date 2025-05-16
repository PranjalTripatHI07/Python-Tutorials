#DATE - 25/2/2025
from random import sample

class Lottery:
    def __init__(self):
        self.ticket = [1, 2, 3, 4, 5, 6, 7, "A", "B", "C", "E", "F", 8, 9, 10]
        self.person_ticket = sample(self.ticket, 4)
        self.winning_ticket = sample(self.ticket, 4)

    def generate_winning_ticket(self):
        return f"\nToday's winning ticket last 4 digits: {self.winning_ticket}"

    def check_match_ticket(self):
        print(f"\nWinning Ticket: {self.winning_ticket} | Your Ticket: {self.person_ticket}")

        if set(self.winning_ticket) == set(self.person_ticket):
            return "\nCongratulations! You have won the lottery!"
        else:
            return "\nSorry! Better luck next time."

    def lottery_analysis(self):
        """Simulates how many attempts it takes to match a winning ticket."""
        attempts = 0

        while True:
            attempts += 1
            new_ticket = sample(self.ticket, 4)  # Generate a new ticket
            if new_ticket == self.winning_ticket:  # Check for an exact match
                break

        return f"\nIt took {attempts} attempts to get a matching ticket."

# Testing the Lottery system
test = Lottery()
print(test.generate_winning_ticket())
print(test.check_match_ticket())

# Printing the result of lottery analysis
print(test.lottery_analysis())




#Anotther way
# Date: 2025-02-25
from random import sample

class Lottery:
    def __init__(self):
        self.ticket = [1, 2, 3, 4, 5, 6, 7, "A", "B", "C", "E", "F", 8, 9, 10]
        self.person_ticket = sample(self.ticket, 4)
        self.winning_ticket = sample(self.ticket, 4)

    def generate_winning_ticket(self):
        return f"\n🎉 Today's winning ticket (last 4 digits): {self.winning_ticket}"

    def check_match_ticket(self):
        print(f"\n🎟️ Winning Ticket: {self.winning_ticket} | Your Ticket: {self.person_ticket}")

        if set(self.winning_ticket) == set(self.person_ticket):
            return "\n🎊 Congratulations! You have won the lottery! 🎉"
        else:
            return "\n😢 Sorry, better luck next time!"

# Running the lottery
test = Lottery()
print(test.generate_winning_ticket())
print(test.check_match_ticket())




#Another

from random import sample

class Lottery:
    def __init__(self):
        self.ticket_pool = [1, 2, 3, 4, 5, 6, 7, "A", "B", "C", "E", "F", 8, 9, 10]
        self.person_ticket = sample(self.ticket_pool, 4)
        self.winning_ticket = sample(self.ticket_pool, 4)

    def generate_winning_ticket(self):
        return f"\nToday's winning ticket last 4 digits: {self.winning_ticket}"

    def check_match_ticket(self):
        print(f"\nWinning Ticket: {self.winning_ticket} | Your Ticket: {self.person_ticket}")

        if self.person_ticket == self.winning_ticket:  # Order matters
            return "\nCongratulations! You have won the lottery!"
        else:
            return "\nSorry! Better luck next time."

    def lottery_analysis(self):
        """Simulates how many tries it takes to match a winning ticket."""
        attempts = 0
        while True:
            attempts += 1
            new_ticket = sample(self.ticket_pool, 4)
            if new_ticket == self.winning_ticket:
                break  # Stop when a match is found
        return f"\nIt took {attempts} attempts to get a matching ticket."

# Testing the Lottery system
test = Lottery()
print(test.generate_winning_ticket())
print(test.check_match_ticket())

print(test.lottery_analysis())
