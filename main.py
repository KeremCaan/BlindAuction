bidding = True
biddings = {}
while bidding:
    bidder = input('What is your name ?: ')
    current_bid = int(input('What is your bid? :$ '))
    biddings[current_bid] = bidder
    answer = input("do you want to continue ? 'y' or 'n' ")
    if answer == 'n':
        bidding = False
bids = []
bidders =[]
for bid in biddings.keys():
    bids.append(bid)
for n in biddings.values():
    bidders.append(n)
winning_bid = max(bids)
winning_person = biddings[winning_bid]
print (f'Congrats, {winning_person} won with ${winning_bid} bid!')