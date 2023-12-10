class Property:
    def __init__(self, name, location, price):
        self.name = name
        self.location = location
        self.price = price

    def display_info(self):
        print(f"Property: {self.name}")
        print(f"Location: {self.location}")
        print(f"Price: ${self.price} per night")


class BookingSystem:
    def __init__(self):
        self.properties = []

    def add_property(self, property):
        self.properties.append(property)

    def list_properties(self):
        for property in self.properties:
            property.display_info()


def main():
    airbnb = BookingSystem()

    # Adding sample properties
    property1 = Property("Cozy Apartment", "City Center", 100)
    property2 = Property("Luxury Villa", "Seaside", 500)

    airbnb.add_property(property1)
    airbnb.add_property(property2)

    # Listing available properties
    airbnb.list_properties()


if __name__ == "__main__":
    main()
