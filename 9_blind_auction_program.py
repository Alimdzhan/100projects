from art1 import logo
print(logo)
print("Welcome to the Blind Auction Program!")

def find_highest_bider(bidding_dictionary):
    highest_bid = 0
    winner = ""
    for bidder in bidding_dictionary:
        bid_amount = bidding_dictionary[bidder]
        bid_amount > highest_bid
        highest_bid = bid_amount
        winner = bidder

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bids = False
while not continue_bids:
    name = input("What is your name?: ")
    price = int(input("What is your bid: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if should_continue == "no":
        find_highest_bider(bids)
        continue_bids = True
    elif should_continue == "yes":
        print("\n" * 100)


