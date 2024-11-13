import art

print(art.logo)


# Create a function to Compare bids in dictionary
def find_highest_bidder(bidding_dict):
    max_price = 0
    winner = ""
    for bidder in bidding_dict:
        current_price = bidding_dict[bidder]

        # Check if current price is higher than max price
        if current_price > max_price:
            max_price = current_price
            winner = name

    # Print winner
    print(f"The winner of the bid is {winner} "
          f"with an auction price of ${max_price}")


restart = True
auction_dict = {}
while restart:
    # Ask the user for input
    name = input("What is your name: ")
    price = int(input("How much do you want to pay for this item? $"))

    # Save data into dictionary {name: price}
    auction_dict[name] = price

    # Whether if new bids need to be added
    add_new_bids = input('Do you want to make a new bid? Type "yes" or '
                         '"no":\n')

    if add_new_bids == "yes":
        print(20 * "\n")
    else:
        restart = False
        find_highest_bidder(auction_dict)
