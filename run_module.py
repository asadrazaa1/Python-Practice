import modules
from modules import fib
from modules import *

import math

money=200

def mon_update():
	global money
	money = money + 1
	print(money)
print(money)
mon_update()
print(money)


modules.print_function("asad")
new_variable = modules.fib(3)
print(new_variable)

print(dir(math))