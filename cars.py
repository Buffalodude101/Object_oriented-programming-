# import
from Vehicle import Vehicle

bug_object = Vehicle("Beetle","yellow", 4, 1) # object of vehicle clss -- instance of vehicle class
turtle_bot = Vehicle("Turtle bot", "Green", 2, 5)
rover_object = Vehicle("Rover", "Purple", 4, 25)

bug_object.print_details()
# turtle_bot.print_details()
# rover_object.print_details()

bug_object.paint_vehicle("blue")

bug_object.print_details()