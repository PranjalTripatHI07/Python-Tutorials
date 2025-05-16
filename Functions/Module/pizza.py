import Module1
import Module1 as M
from Module1 import make_pizza


Module1.make_pizza("large", "cheese", "peperoni","garlic-paste", "mushroom")
Module1.make_pizza("medium", "peperoni", "mushroom")

make_pizza("large", "cheese", "peperoni","garlic-paste", "mushroom")
make_pizza("medium", "peperoni", "mushroom")

M.make_pizza("medium", "peperoni", "mushroom")
M.make_pizza("large", "cheese", "peperoni","garlic-paste", "mushroom")