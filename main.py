from helpers import clear_screen
from art import logo
print(logo)

auction_bids = {}
biddingComplete = False

def determineHighestBidder(recordBid):
    highest_bid = 0
    champion = ""

    for bidder in recordBid:
        bid_amount = recordBid[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            champion = bidder
    print(f"The winner is {champion} with a bid of ${highest_bid}")

while biddingComplete is False:
    name = input("What is your name? ")
    price = int(input("What is the bid? $"))
    auction_bids[name] = price

    proceed = input("Are there any other bidders? Click 'yes' or 'no'. \n").lower()

    if proceed == "yes":
        clear_screen()
        print("\n" * 100)
    elif proceed == "no":
        biddingComplete = True
        determineHighestBidder(auction_bids)


