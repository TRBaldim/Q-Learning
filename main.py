from map import Map
from default_object import Objects
from elements import Wall, Cheese, Mouse, Cat

obj = Objects()
b_obj = Objects()
obj.put_stack(b_obj)

map = Map(10, 5)

m = Mouse()

map.set_element(Wall(), 2, 3)
map.set_element(Cheese(), 1, 3)
map.set_element(m, 2, 1)
map.set_element(Cheese(), 1, 3)
map.set_element(Cat(), 0, 4)
# todo: fix the possible move, the return is none. Should be debugged.
print map.possible_move(*m.position)

print map
