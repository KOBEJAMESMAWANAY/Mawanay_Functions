#Introduction message for the user, note that all data options are purposedly turned comedy for entertainment-creativity purposes only.
print("Welcome to Mawanay's Binangkal Comedic Restaurant!")

# Menu Items with Comedic Descriptions and Prices
menu = {
    1: {"name": "Pak Ganern Platter", "price": 565, "description": "Pinakbet with bagnet that’s as crunchy as your tita’s chismis."},
    2: {"name": "Pataw-Taw Bites", "price": 365, "description": "Crispy pork served with garlic rice, an extra crispy comedic punch."},
    3: {"name": "Pamatay na Lumpia", "price": 250, "description": "Lumpia filled with a combination of ground pork, shrimp, and a fiery chili pepper."},
    4: {"name": "Bistek Hanggang Umaga", "price": 350, "description": "Beefsteak so tender it’ll keep you coming back. chos baka matigas ahh"},
    5: {"name": "Sinigang na Hindi Ako Mahal", "price": 565, "description": "Tamarind-based pork or beef soup, as sour as your ex."},
    6: {"name": "Funny Bun Trio", "price": 250, "description": "Siopao, Sisiw, at Sabaw (Funny Bun Trio) - classic siopao with a mini egg roll (sisiw) and a side of chicken broth."},
    7: {"name": "Bagoong Biniro", "price": 250, "description": "A small, spicy bowl of bagoong, but with a comic surprise element on the plate!"},
    8: {"name": "Sago't Gulaman mo naman ako uwu", "price": 115, "description": "Bottomless classic Filipino coolers, giving you that cold treatment"},
    9: {"name": "Tubig", "price": 35, "description": "Wala. Tubig lang talaga siya bes. (350mL bottled water)"}
}

#Display Menu
def display_menu():
    """Displays the menu with item numbers, names, prices, and descriptions."""
    print("\nMenu:")
    for item_id, item in menu.items():
        print(f"{item_id}. {item['name']} - ₱{item['price']:.2f}") #This prints the name of the item name and price
        print(f"   {item['description']}")  # This prints the description below the item name and price

#Order Selection and Calculate Total
def get_order():
    """
    This process allows users to select multiple items from the menu.
    The user can specify the quantity for each item.
    Returns a list of selected items and their quantities.
    """
    order = []
    total_cost = 0
    while True:
        try:
            choice = int(input("Select a menu-item by its number (or input 0 to finish): "))
            if choice == 0:  # This will finish the ordering system
                break
            elif choice in menu:
                quantity = int(input(f"How many {menu[choice]['name']}(s) would you like? "))
                if quantity > 0:
                    order.append({"item": menu[choice], "quantity": quantity})
                    total_cost += menu[choice]["price"] * quantity
                    print(f"Current Total: ₱{total_cost:.2f}")
                else:
                    print("Please enter a valid quantity (greater than 0).")
            else:
                print("Invalid selection. Please choose a valid menu item.")
        except ValueError:
            print("I'm sorry, please enter a valid number.")
    
    return order, total_cost

#Payment Processing
def process_payment(total_cost):
    """
    This processes the payment of the user by prompting the cash rendered.
    Ensures the cash amount is sufficient and calculates change if necessary.
    """
    while True:
        try:
            cash = float(input(f"Total is ₱{total_cost:.2f}. Enter cash rendered: $"))
            if cash >= total_cost:
                change = cash - total_cost
                print(f"Payment successful! Your change is ₱{change:.2f}.")
                return
            else:
                print(f"Insufficient payment. You need ₱{total_cost - cash:.2f} more.")
        except ValueError:
            print("I'm sorry, please enter a valid amount.")

#Direct execution of the main function
def main():
    """Main function to run the ordering system."""
    display_menu()
    order, total_cost = get_order()
    
    if not order:
        print("Unfortunately, you didn't order anything. Goodbye!")
        return
    
    print("\nOrder Summary:")
    for item in order:
        print(f"{item['quantity']} x {item['item']['name']} @ ${item['item']['price']:.2f} each")
    print(f"Total Cost: ₱{total_cost:.2f}")
    
    process_payment(total_cost)
main()