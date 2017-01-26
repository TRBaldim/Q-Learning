from default_object import Objects
from elements import *

class Cat(Objects):
    def set_hierarchy(self):
        self.hierarchy_level = 7

    def __str__(self):
        return 'C'

    def __repr__(self):
        return 'C'

    def interact(self, obj):
        if isinstance(obj, Mouse):
            return obj.interact(self)
        else:
            return False