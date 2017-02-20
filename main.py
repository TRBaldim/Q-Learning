from map import Map
from default_object import Objects
from elements import Wall, Cheese, Mouse, Cat
from reinforcement import directions

import numpy as np

obj = Objects()
b_obj = Objects()
obj.put_stack(b_obj)

map = Map(10, 6)

m = Mouse()

#[map.set_element(Wall(), np.random.randint(0, 9), np.random.randint(0, 5)) for _ in range(5)]
map.set_element(Cheese(), 1, 0)
map.set_element(m, 9, 5)
map.set_element(Wall(), 9, 4)
map.set_element(Wall(), 8, 4)
map.set_element(Wall(), 7, 4)
map.set_element(Wall(), 5, 4)
map.set_element(Wall(), 4, 4)
map.set_element(Wall(), 3, 4)
map.set_element(Wall(), 2, 4)
map.set_element(Wall(), 1, 4)
map.set_element(Wall(), 0, 4)
map.set_element(Wall(), 5, 5)
map.set_element(Wall(), 5, 3)
map.set_element(Wall(), 5, 2)
map.set_element(Wall(), 6, 2)
map.set_element(Wall(), 7, 2)
map.set_element(Wall(), 9, 3)
map.set_element(Wall(), 9, 2)
map.set_element(Wall(), 9, 1)
map.set_element(Wall(), 9, 0)
map.set_element(Wall(), 8, 0)
map.set_element(Wall(), 7, 0)
map.set_element(Wall(), 6, 0)
map.set_element(Wall(), 5, 0)
map.set_element(Wall(), 4, 0)
map.set_element(Wall(), 3, 0)
map.set_element(Wall(), 3, 1)
map.set_element(Wall(), 3, 2)
map.set_element(Wall(), 0, 0)
map.set_element(Wall(), 0, 1)
map.set_element(Wall(), 0, 2)
map.set_element(Wall(), 0, 3)
map.set_element(Wall(), 2, 0)
map.set_element(Wall(), 2, 1)
map.set_element(Wall(), 2, 2)
#map.set_element(Cheese(), 4, 3)
#map.set_element(Cat(), 0, 4)

print map

for _ in range(1000):
    pos = map.possible_move(*m.position)
    p = m.learn(map)
    #print directions((m.position[0], m.position[1]), pos)
    #p = pos[np.random.randint(0, len(pos))]
    #print p
    map.move_object(m, *p)
    print map
# TODO: Build a Labirinth to teach the mouse to solve
