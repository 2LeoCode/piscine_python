from time import perf_counter, sleep
from random import randint
from os import environ as env

def log(func):
    def wrapper(*args, **kwargs):
        start_s = perf_counter()
        ret = func(*args, **kwargs)
        delta_s = perf_counter() - start_s
        prefix = f"({env['USER']})Running: "
        func_name = ' '.join(func.__name__.split('_')).title()
        suffix = f"[ exec-time = " + (f"{delta_s * 1000:.3f} ms ]" if delta_s < 1 else f"{delta_s:.3f} s ]") + '\n'
        with open("machine.log", "a") as f:
            f.write(prefix + "{:<19}".format(func_name) + suffix)
        return ret
    return wrapper


class CoffeeMachine():
    water_level = 100

    @log
    def start_machine(self):
        if self.water_level <= 20:
            print("Please add water!")
            return False
        return True

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            print(self.boil_water())
            for _ in range(20):
                sleep(0.1)
                self.water_level -= 1
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.add_water(70)
    machine.make_coffee()
