class Vehicle:
    pass

bug_object = Vehicle() # object of vehicle clss -- instance of vehicle class
turtle_bot = Vehicle()
rover_object = Vehicle()

bug_object.color = "yellow"
bug_object.num_wheels = 4
bug_object.speed = 1

turtle_bot.color = "green"
turtle_bot.num_wheels = 2
turtle_bot.speed = 5

rover_object.color = "purple"
rover_object.num_wheels = 4
rover_object.speed = 25

print("This vehicle is",bug_object.color, "and is able to drive", bug_object.speed, "MPH")
print("This vehicle is", turtle_bot.color, "and is able to drive", turtle_bot.speed, "MPH")
print("Thia vehicle is", rover_object.color, "and is able to drive",rover_object.speed, "MPH")