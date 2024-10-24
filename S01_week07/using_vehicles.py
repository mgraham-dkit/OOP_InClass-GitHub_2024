from vehicles import Vehicle


vroom = Vehicle("Honda", "Red", 7)
vroom_vroom = Vehicle("Honda", "Red", 7)

if vroom == vroom_vroom:
    print("The same!!")
else:
    print("What happened???")
