# Dylan Fields
# M03 Lab - Case Study: Lists, Functions, and Classes


class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

def main():
    print("Enter information for a car:")
    vehicle_type = "car"
    year = input("Year: ")
    make = input("Make: ")
    model = input("Model: ")
    doors = input("Number of doors (2 or 4): ")
    roof = input("Type of roof (solid or sun roof): ")

    if doors not in ("2", "4"):
        print("Invalid number of doors. Please enter 2 or 4.")
        return

    if roof not in ("solid", "sun roof"):
        print("Invalid type of roof. Please enter solid or sun roof.")
        return

    car = Automobile(vehicle_type, year, make, model, doors, roof)

    print("\nCar Information:")
    car.display_info()

if __name__ == "__main__":
    main()
