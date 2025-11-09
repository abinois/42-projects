import time
from random import randint
from getpass import getuser

def log(func):
    def wrap(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        exec_time = time.time() - start
        with open('machine.log', 'a') as fd:
            line = '(' + getuser() + ')Running: ' + func.__name__.replace('_', ' ').title() + '\t' + \
                '[ exec-time = ' + '{:0.3f}'.format(exec_time) + (' s  ]', ' ms ]')[exec_time >= 0 and exec_time < 1]
            fd.write(line + '\n')
        return res
    return wrap

class CoffeeMachine():

    water_level = 100

    @log
    def start_machine(self):
      if self.water_level > 20:
          return True
      else:
          print("Please add water!")
          return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()

    machine.make_coffee()
    machine.add_water(70)