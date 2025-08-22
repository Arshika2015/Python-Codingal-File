class BMW:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The BMW {self.model} engine starts with a smooth purr."

    def accelerate(self):
        return f"The BMW {self.model} accelerates with refined power."

    def stop_engine(self):
        return f"The BMW {self.model} engine shuts down quietly."
class FERRARI:
    def __init__(self, model):
        self.model = model

    def start_engine(self):
        return f"The FERRARI {self.model} engine roars to life!"

    def accelerate(self):
        return f"The FERRARI {self.model} surges forward with immense force."

    def stop_engine(self):
        return f"The FERRARI {self.model} engine powers down with a final growl."
def car_actions(car):
    """
    This function demonstrates polymorphism by calling common methods
    on different car objects.
    """
    print(car.start_engine())
    print(car.accelerate())
    print(car.stop_engine())
    print("-" * 30)
bmw_m3 = BMW("M3")
ferrari_488 = FERRARI("488 GTB")
car_actions(bmw_m3)
car_actions(ferrari_488)