"""Functions to manage a users shopping cart items."""
from collections import OrderedDict


def add_item(current_cart: dict, items_to_add: iter):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """
    for item in items_to_add:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """
    current_cart: dict = {}

    for item in notes:
        current_cart[item] = current_cart.get(item, 0) + 1

    return current_cart


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """
    for key, value in recipe_updates:
        print(key, value)
        ideas[key] = value
    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """
    return dict(sorted(cart.items()))


def send_to_store(cart: dict, aisle_mapping: dict) -> dict:
    """Combine users order to aisle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param aisle_mapping: dict - aisle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    compiled_list: dict = dict()
    for key, value in cart.items():
        aisle_info = aisle_mapping.get(key, ["", False])
        compiled_list[key] = [value, aisle_info[0], aisle_info[1]]

    compiled_list = dict((sorted(compiled_list.items(), reverse=True)))
    return compiled_list


print(
    send_to_store(
        {"Banana": 3, "Apple": 2, "Orange": 1, "Milk": 2},
        {
            "Banana": ["Aisle 5", False],
            "Apple": ["Aisle 4", False],
            "Orange": ["Aisle 4", False],
            "Milk": ["Aisle 2", True],
        },
    )
)


def update_store_inventory(fulfillment_cart: dict, store_inventory: dict):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """
    for key, value in store_inventory.items():
        if key in fulfillment_cart:
            new_quantity = value[0] - fulfillment_cart[key][0]
            store_inventory[key][0] = (
                new_quantity if new_quantity > 0 else "Out of Stock"
            )
    return store_inventory
