from menu_item import MenuItem
from menu_manager import MenuManager


def show_user_menu():
    print("\n========== MENU EDITOR ==========")
    print("V - View an Item")
    print("A - Add an Item")
    print("D - Delete an Item")
    print("U - Update an Item")
    print("S - Show the Menu")
    print("Q - Quit")
    choice = input("Enter your choice: ").strip().upper()

    if choice == 'V':
        view_item()
    elif choice == 'A':
        add_item()
    elif choice == 'D':
        delete_item()
    elif choice == 'U':
        update_item()
    elif choice == 'S':
        show_menu()
    elif choice == 'Q':
        print("Exiting the menu editor.")
    else:
        print("Invalid choice. Please try again.")


def view_item():
    item_name = input("Enter the name of the item you want to view: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        print("Item found: ", item.item_name, item.item_price)
    else:
        print("Item not found.")


def add_item():
    item_name = input("Enter the name of the new item: ")
    item_price = int(input("Enter the price of the new item: "))
    new_item = MenuItem(item_name, item_price)
    new_item.save()
    print("Item added successfully!")


def delete_item():
    item_name = input("Enter the name of the item you want to delete: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        item.delete()
        print("Item deleted successfully!")
    else:
        print("Item not found.")


def update_item():
    item_name = input("Enter the name of the item you want to update: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        new_item_name = input("Enter the new name of the item: ")
        new_item_price = int(input("Enter the new price of the item: "))
        item.update(new_item_name, new_item_price)
        print("Item updated successfully!")
    else:
        print("Item not found.")


def show_menu():
    items = MenuManager.all_items()
    if items:
        print("\n========== MENU ==========")
        for item in items:
            print(item.item_name, item.item_price)
    else:
        print("No items found in the menu.")


def add_item_to_menu():
    item_name = input("Enter the name of the new item: ")
    item_price = int(input("Enter the price of the new item: "))
    new_item = MenuItem(item_name, item_price)
    new_item.save()

    print("Item added successfully!")


def remove_item_from_menu():
    item_name = input("Enter the name of the item you want to remove from the menu: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        item.delete()
        print("Item removed successfully!")
    else:
        print("Item not found.")


def update_item_from_menu():
    item_name = input("Enter the name of the item you want to update: ")
    item = MenuManager.get_by_name(item_name)
    if item:
        new_item_name = input("Enter the new name of the item: ")
        new_item_price = int(input("Enter the new price of the item: "))
        item.update(new_item_name, new_item_price)
        print("Item updated successfully!")
    else:
        print("Item not found.")


def show_restaurant_menu():
    items = MenuManager.all_items()
    if items:
        print("\n========== RESTAURANT MENU ==========")
        for item in items:
            print(item.item_name, item.item_price)
    else:
        print("No items found in the restaurant menu.")


if __name__ == "__main__":
    while True:
        show_user_menu()
        choice = input("Do you want to continue? (Y/N): ").strip().upper()
        if choice != 'Y':
            show_restaurant_menu()
            print("Exiting...")
            break
