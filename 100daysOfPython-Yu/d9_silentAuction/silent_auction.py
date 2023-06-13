from replit import clear


logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("Welcome to the secret auction program.")

bidders = {} 
other_bidders = "yes"

while (other_bidders == "yes"):
  name = input("What is your name? ")
  bid_amount = input("What's your bid? : $")
  bidders = {name: bid_amount}
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no' ")
  if (other_bidders == "yes"):
    clear()
  else:
    #iterate over dict values
    #compare values until highes found
    #retrieve key and value
    #print highest key and value "The winner is [key] with a bid of $[value]."
    for key in bidders:
      highest_key = key
      highest_value = bidders[key]
#If the other bidder increases the bid amount as asked by the auctioneer, he will be declared the winner. But if not, the first bidder will acquire the product or service.
      if highest_value == bidders[key]:
        second_bid = input(f"{key}, your bid is not the highest, do you want to increase         your bid? Enter 'yes' or 'no'. ")
        if second_bid == "no":
          continue
        else:
          alternative_bid = int(input(" "))
          if highest_value < alternative_bid:
            bidders[key] = alternative_bid
            
      elif highest_value < bidders[key]:
        highest_key = key
        highest_value = bidders[key]
    print(highest_key + " " + highest_value)



#for key in a_dict:
#...     print(key, '->', a_dict[key])