from default_object import Objects

class Cheese(Objects):

    def set_hierarchy(self):
        self.hierarchy_level = 1

    def __str__(self):
        return 'Q'

    def __repr__(self):
        return 'Q'

    def interact(self, obj):