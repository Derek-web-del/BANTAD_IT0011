class Item:
    def __init__(self, item_id, name, description, price):
        if not isinstance(item_id, int):
            raise ValueError("ID must be an integer")
        if not isinstance(name, str) or not name.strip():
            raise ValueError("Name must be a non-empty string")
        if not isinstance(description, str) or not description.strip():
            raise ValueError("Description must be a non-empty string")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a positive number")

        self.id = item_id
        self.name = name.strip()
        self.description = description.strip()
        self.price = price

class ItemManager:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        if not isinstance(item, Item):
            raise ValueError("Item is Invalid")
        if any(existing_item.id == item.id for existing_item in self.items):
            raise ValueError("Item ID already exists")
        self.items.append(item)

    def delete_item(self, item_id):
        for item in self.items:
            if item.id == item_id:
                self.items.remove(item)
                return
        raise ValueError("Item not found")

    def update_item(self, item_id, new_name=None, new_description=None, new_price=None):
        for item in self.items:
            if item.id == item_id:
                if new_name:
                    item.name = new_name.strip()
                if new_description:
                    item.description = new_description.strip()
                if new_price is not None:
                    if not isinstance(new_price, (int, float)) or new_price < 0:
                        raise ValueError("The price is Invalid")
                    item.price = new_price
                return
        raise ValueError("Item not found")

    def get_item_by_id(self, item_id):
        for item in self.items:
            if item.id == item_id:
                return item
        raise ValueError("Item not found")

    def list_items(self):
        return self.items

if __name__ == "__main__":
    manager = ItemManager()
    try:
        item1 = Item(1, "Laptop", "Acer Helios 18H", 78000.00)
        manager.add_item(item1)
        print("Item added successfully.")
    except ValueError as e:
        print("Error:", e)
    try:
        item = manager.get_item_by_id(1)
        print(f"Retrieved: {item.name} - {item.description} - P{item.price}")
    except ValueError as e:
        print("Error:", e)
