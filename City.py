class City:
    def __init__(self, name, country):
        self.name = name
        self.country = country
        self.buildings = []

    def add_building(self, building):
        self.buildings.append(building)

    def remove_building(self, building):
        self.buildings.remove(building)

    def get_buildings(self):
        print(f'{self.buildings}')

    def get_building_count(self):
        return len(self.buildings)

