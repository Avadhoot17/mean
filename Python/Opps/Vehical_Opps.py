from datetime import datetime

# Base Class: Vehicle
class Vehicle:
    def _init_(self, vehicle_id, brand, model, rental_price, vehicle_type):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.model = model
        self.rental_price = rental_price
        self.vehicle_type = vehicle_type
        self.is_available = True

    def _str_(self):
        return f"{self.vehicle_type}: {self.brand} {self.model} (ID: {self.vehicle_id}) - ${self.rental_price}/day"

# Derived Classes: Car, Bike, Truck
class Car(Vehicle):
    def _init_(self, vehicle_id, brand, model, rental_price, seating_capacity):
        super()._init_(vehicle_id, brand, model, rental_price, "Car")
        self.seating_capacity = seating_capacity

class Bike(Vehicle):
    def _init_(self, vehicle_id, brand, model, rental_price, engine_capacity):
        super()._init_(vehicle_id, brand, model, rental_price, "Bike")
        self.engine_capacity = engine_capacity

class Truck(Vehicle):
    def _init_(self, vehicle_id, brand, model, rental_price, load_capacity):
        super()._init_(vehicle_id, brand, model, rental_price, "Truck")
        self.load_capacity = load_capacity

# Class: Customer
class Customer:
    def _init_(self, name, driver_license):
        self.name = name
        self.driver_license = driver_license
        self.rented_vehicles = []  # List of (vehicle, rental_start_date)

    def _str_(self):
        return f"Customer: {self.name} (License: {self.driver_license})"

# Class: RentalService
class RentalService:
    def _init_(self):
        self.fleet = []
        self.rental_history = {}

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)

    def view_available_vehicles(self):
        print("\nAvailable Vehicles:")
        for vehicle in self.fleet:
            if vehicle.is_available:
                print(vehicle)
        print()

    def rent_vehicle(self, customer, vehicle_id):
        for vehicle in self.fleet:
            if vehicle.vehicle_id == vehicle_id and vehicle.is_available:
                vehicle.is_available = False
                customer.rented_vehicles.append((vehicle, datetime.now()))
                if customer.name not in self.rental_history:
                    self.rental_history[customer.name] = []
                self.rental_history[customer.name].append(vehicle)
                print(f"\n{customer.name} successfully rented {vehicle.brand} {vehicle.model}.")
                return
        print(f"\nVehicle ID {vehicle_id} is either not available or does not exist.")

    def return_vehicle(self, customer, vehicle_id):
        for rented_vehicle, rental_start in customer.rented_vehicles:
            if rented_vehicle.vehicle_id == vehicle_id:
                rental_days = (datetime.now() - rental_start).days + 1
                rental_cost = rental_days * rented_vehicle.rental_price
                rented_vehicle.is_available = True
                customer.rented_vehicles.remove((rented_vehicle, rental_start))
                print(f"\n{customer.name} returned {rented_vehicle.brand} {rented_vehicle.model}. Total cost: ${rental_cost:.2f}")
                return
        print(f"\n{customer.name} does not have vehicle ID {vehicle_id} rented.")

    def view_rental_history(self, customer_name):
        print(f"\nRental History for {customer_name}:")
        if customer_name in self.rental_history:
            for vehicle in self.rental_history[customer_name]:
                print(vehicle)
        else:
            print("No rental history found.")