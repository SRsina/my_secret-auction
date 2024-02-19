from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program.")
bidders = []
def add_bidder(name, bid):
  new_bidder = {"name": name, "bid": bid}
  bidders.append(new_bidder)

new_bidder = True

while new_bidder:
  name = input("What is your name?: ")
  bid = float(input("What's your bid?: $"))
  add_bidder(name, bid)
  new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  clear()
  if new_bidder == "no":
    new_bidder = False
max_bid = 0.0
max_bidder = ""
for bidder in bidders:
  if bidder['bid'] > max_bid:
    max_bid = bidder['bid']
    max_bidder = bidder['name']
print(f"The winner is {max_bidder} with a bid of ${max_bid}")
print(logo)
print("Sold! Thank you for using the secret auction program.")
  