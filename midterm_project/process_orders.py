import json
import argparse

# Load orders from JSON file
def load_orders(filename):
    """Read orders from a JSON file."""
    with open(filename, "r") as file:
        return json.load(file)

# Generate customer dictionary
def build_customers(orders):
    """Create phone -> customer name dictionary."""
    customers = {}

    for order in orders:
        customers[order["phone"]] = order["name"]

    return customers


def build_items(orders):
    """Create item statistics dictionary."""
    items = {}

    for order in orders:

        for item in order["items"]:

            item_name = item["name"]
            item_price = item["price"]

            if item_name not in items:
                items[item_name] = {
                    "price": item_price,
                    "orders": 0
                }

            items[item_name]["orders"] += 1

    return items


def write_json(filename, data):
    """Write dictionary to a JSON file."""
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


def main():
    parser = argparse.ArgumentParser(
        description="Process Dosa restaurant orders"
    )

    parser.add_argument(
        "filename",
        help="JSON orders file"
    )

    args = parser.parse_args()

    orders = load_orders(args.filename)

    customers = build_customers(orders)
    items = build_items(orders)

    write_json("customers.json", customers)
    write_json("items.json", items)

    print("customers.json created successfully")
    print("items.json created successfully")
    print("Order processing complete.")


if __name__ == "__main__":
    main()
