class vehicle :
    def __init__(self,name,maximumspeed,mileage):
        self.name = name
        self.maximumspeed = maximumspeed
        self.mileage = mileage
class bus(vehicle):
    pass
school_bus = bus("schoolvolvo",216,783)
print("schoolbus name is ",school_bus.name)
print("maximum speed of the schoolbus is ",school_bus.maximumspeed)
print("mileage of the schoolbus is ",school_bus.mileage)



