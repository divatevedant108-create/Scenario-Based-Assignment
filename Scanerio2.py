class Vehicle:
    def __init__(self, vehicle_number, brand, price):
        self.vehicle_number = vehicle_number
        self.brand = brand
        self.price = price

        # Categorize vehicle
        if price >= 1000000:
            self.category = "Luxury"
        else:
            self.category = "Economy"


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_vehicles(self):
        print("\n--- Vehicle Showroom Records ---")
        for vehicle in self.vehicles:
            print("Vehicle Number:", vehicle.vehicle_number)
            print("Brand:", vehicle.brand)
            print("Price: ₹", vehicle.price)
            print("Category:", vehicle.category)
            print("-----------------------------")


# Create showroom
showroom = Showroom()

# Add vehicles
v1 = Vehicle("MH12AB1234", "BMW", 2500000)
v2 = Vehicle("MH14CD5678", "Maruti", 700000)
v3 = Vehicle("MH12EF9012", "Mercedes", 4500000)
v4 = Vehicle("MH14GH3456", "Tata", 850000)

showroom.add_vehicle(v1)
showroom.add_vehicle(v2)
showroom.add_vehicle(v3)
showroom.add_vehicle(v4)

# Display all vehicles
showroom.display_vehicles()
