from default_object import Objects


class Cat(Objects):
    def set_hierarchy(self):
        self.hierarchy_level = 7

    def __str__(self):
        return 'C'

    def __repr__(self):
        return 'C'

    def interact(self, obj):
        if isinstance(obj, Mouse):
            obj.destroy()
            return True
        else:
            return False


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
            return True
        else:
            return False