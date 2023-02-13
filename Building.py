class Building:
    def __init__(self, building_name):
        if type(building_name) == str:
            self.name = building_name
        else:
            self.name = ""
        self.occupants = []

    def get_name(self):
        return self.name

    def show_info(self):
        return f"Building Name: {self.name}"

    def add_occupant(self, occupant):
        self.occupants.append(occupant)

    def remove_occupant(self, occupant):
        self.occupants.remove(occupant)

    def get_occupants(self):
        return self.occupants




