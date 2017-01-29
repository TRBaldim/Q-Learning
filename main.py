from map import Map
from default_object import Objects
from elements import Wall, Cheese, Mouse, Cat
from reinforcement import directions

import numpy as np

obj = Objects()
b_obj = Objects()
obj.put_stack(b_obj)

map = Map(10, 5)

m = Mouse()

map.set_element(Wall(), 2, 3)
map.set_element(Cheese(), 1, 3)
map.set_element(m, 1, 3)
map.set_element(Cheese(), 4, 3)
map.set_element(Cat(), 0, 4)

print map

for _ in range(10):
    pos = map.possible_move(*m.position)
    print directions((m.position[0], m.position[1]), pos)
    p = pos[np.random.randint(0, len(pos))]
    print p
    map.move_object(m, *p)
    print map

print map
