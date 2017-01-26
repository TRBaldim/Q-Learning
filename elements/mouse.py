from default_object import Objects
from cat import Cat


class Mouse(Objects):

    def set_hierarchy(self):
        self.hierarchy_level = 5

    def __str__(self):
        return 'M'

    def __repr__(self):
        return 'M'

    def set_depth(self):
        self.depth = 1

    def interact(self, obj):
        if isinstance(obj, Cat):
            obj.interact(self)
            self.destroy()
            return True
        else:
            return False

