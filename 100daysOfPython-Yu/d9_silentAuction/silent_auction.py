import os


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
next_bidder = "yes"
highest_value = 0

while (next_bidder == "yes"):
  name = input("What is your name? ")
  bid_amount = int(input("What's your bid? : $"))
  bidders = {name: bid_amount}
  next_bidder = input("Are there any other bidders? Type 'yes' or 'no' ")
  if (next_bidder == "yes"):
    os.system('cls')
  else:
    #iterate over dict values
    #compare values until highes found
    #retrieve key and value
    #print highest key and value "The winner is [key] with a bid of $[value]."
    for key in bidders:
      if highest_value < bidders[key]:
        highest_value = bidders[key]
        continue
      
      elif highest_value == bidders[key]:
        second_bid = input(f"{name}, your bid is not the highest, do you want to increase your bid? Enter 'yes' or 'no': ")
        if second_bid == "no":
            continue
        else:
            alternative_bid = int(input("Enter a higher bid $"))
            highest_value = alternative_bid
            continue
      elif highest_value < bidders[key]:
        highest_key = key
        highest_value = bidders[key]   
    print(f"The highest bidder is {highest_key} with a bid of ${highest_value}")

"""
If the other bidder increases the bid amount as asked by the auctioneer,
he will be declared the winner. But if not, the first bidder will acquire the product or service.
"""  
#for key in a_dict:
#...     print(key, '->', a_dict[key])