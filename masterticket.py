TICKET_PRICE = 25
SERVICE_CHARGE = 3
tickets_remaining = 100 


def calculate_price(quantity):
    return ((quantity*TICKET_PRICE)+SERVICE_CHARGE)

while tickets_remaining !=0:
    print("Welcome to Canada's Wonderland Online Ticket Booth!")
    print("There are {} tickets remaining.".format(tickets_remaining))
    user_name=input("Please enter your name: ")
    quantity=input("Welcome {}, how many tickets would you like to purchase? ".format(user_name))
    #Expect a ValueError
    try:
        quantity=int(quantity)
        #Raise a ValueError if the request is for more tickets than are available
        if quantity>tickets_remaining:
            raise ValueError("There are only {} tickets remaining!".format(tickets_remaining))
    except ValueError as err:
        #Include an error text in the output
        print("oh no, we ran into an issue. {}. Please try again".format(err))
    else:
        price = calculate_price(quantity)
        print("Excellent! The price for",quantity,"tickets is ${}.".format(price))
        choice=input("Would you like to proceed? (enter 'Y' to continue or 'N' to exit)> :")
        choice=choice.upper()
        if choice =="Y":
            print("SOLD!")
            tickets_remaining-=quantity
        else:
            print("Thank you for visiting {}! Have a pleasant day!".format(user_name))
print("Sorry, all tickets have now been sold out!")
