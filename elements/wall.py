from default_object import Objects


class Wall(Objects):

    def set_hierarchy(self):
        self.hierarchy_level = 10

    def __str__(self):
        return '#'

    def __repr__(self):
        return '#'

    def interact(self, obj):
        return False