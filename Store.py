from Building import Building


class Store(Building):
    def __init__(self, store_name):
        Building.__init__(self, store_name)
        self.inventory = {}

    def add_item(self, item, quantity):
        if type(item) == str and type(quantity) == int and quantity >= 0:
            self.inventory[item] = quantity

    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]

    def update_item_quantity(self, item, quantity):
        if item in self.inventory and type(quantity) == int and quantity >= 0:
            self.inventory[item] = quantity

    def get_inventory(self):
        return self.inventory

    def show_info(self):
        return f"Store Name: {self.name}, Inventory: {self.inventory}"