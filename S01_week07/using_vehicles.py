from vehicles import Vehicle
from vehicles import Bike


vroom = Vehicle("Honda", "Red", 7)
vroom_vroom = Vehicle("Honda", "Red", 7)

if vroom == vroom_vroom:
    print("The same!!")
else:
    print("What happened???")

bike1 = Bike("Carrera", "Red", 5, 12)
bike2 = Bike("Apollo", "Blue", 4, 10)

vehicles = [vroom, vroom_vroom, bike1, bike2]
for vehicle in vehicles:
    print(vehicle)
