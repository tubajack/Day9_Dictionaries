from replit import clear
from art import logo
print(logo)

auction_bids = {}
biddingComplete = False

while biddingComplete is False:
    name = input("What is your name? ")
    price = int(input("What is the bid? "))
    auction_bids[name] = price

    proceed = input("Are there any other bidders? Click 'yes' or 'no'. \n")

    if proceed == "yes":
        clear()
