from map import Map
from default_object import Objects
from elements import Wall, Cheese, Mouse, Cat

obj = Objects()
b_obj = Objects()
obj.put_stack(b_obj)

map = Map(10, 5)

map.set_element(Wall(), 2, 3)
map.set_element(Cheese(), 1, 3)
map.set_element(Mouse(), 1, 3)
map.set_element(Cheese(), 1, 3)
map.set_element(Cat(), 0, 4)

print map

map.set_element(Cat(), 1, 3)

print map
