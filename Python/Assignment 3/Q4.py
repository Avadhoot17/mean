class Vehicle:
    def __init__(self, vehicle_id, brand, model, rental_price):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.is_available = True

    def rent(self):
        if self.is_available:
            self.is_available = False
            return True
        return False

    def return_vehicle(self):
        self.is_available = True

    def __str__(self):
        return f"{self.brand} {self.model} (ID: {self.vehicle_id}) - {'Available' if self.is_available else 'Rented'}"


class Car(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, num_doors):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.num_doors = num_doors


class Bike(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, type_of_bike):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.type_of_bike = type_of_bike


class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, model, rental_price, load_capacity):
        super().__init__(vehicle_id, brand, model, rental_price)
        self.load_capacity = load_capacity


class Customer:
    def __init__(self, name, license_number):
        self.name = name
        self.license_number = license_number
        self.rented_vehicles = []

    def rent_vehicle(self, vehicle):
        if vehicle.rent():
            self.rented_vehicles.append(vehicle)
            return True
        return False

    def return_vehicle(self, vehicle):
        if vehicle in self.rented_vehicles:
            vehicle.return_vehicle()
            self.rented_vehicles.remove(vehicle)
            return True
        return False

    def view_rental_history(self):
        return [str(vehicle) for vehicle in self.rented_vehicles]


class RentalService:
    def __init__(self):
        self.fleet = []

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)

    def view_available_vehicles(self):
        return [str(vehicle) for vehicle in self.fleet if vehicle.is_available]

    def rent_vehicle_to_customer(self, customer, vehicle_id):
        for vehicle in self.fleet:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                return customer.rent_vehicle(vehicle)
        return False

    def return_vehicle_from_customer(self, customer, vehicle_id):
        for vehicle in customer.rented_vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return customer.return_vehicle(vehicle)
        return False


# Example usage
if __name__ == "__main__":
    rental_service = RentalService()
    
    # Adding vehicles
    rental_service.add_vehicle(Car("C001", "Toyota", "Camry", 50, 4))
    rental_service.add_vehicle(Bike("B001", "Yamaha", "R1", 30, "Sport"))
    rental_service.add_vehicle(Truck("T001", "Ford", "F-150", 70, 1000))

    # Creating a customer
    customer = Customer("John Doe", "DL123456")

    # Viewing available vehicles
    print("Available Vehicles:")
    print(rental_service.view_available_vehicles())

    # Renting a vehicle
    if rental_service.rent_vehicle_to_customer(customer, "C001"):
        print(f"{customer.name} rented a vehicle.")
    else:
        print("Vehicle not available for rent.")

    # Viewing rental history
    print("Rental History:")
    print(customer.view_rental_history())

    # Returning the vehicle
    if rental_service.return_vehicle_from_customer(customer, "C001"):
        print(f"{customer.name} returned a vehicle.")
    else:
        print("Vehicle not rented by customer.")

    # Viewing available vehicles after return
    print("Available Vehicles after return:")
    print(rental_service.view_available_vehicles())
