from default_object import Objects
from mouse import Mouse

class Cheese(Objects):

    def set_hierarchy(self):
        self.hierarchy_level = 1

    def __str__(self):
        return 'Q'

    def __repr__(self):
        return 'Q'

    def interact(self, obj):
        if isinstance(obj, Mouse):
            obj.interact(self)
            self.destroy()
            return True
        else:
            return False
