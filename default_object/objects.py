from classic_algorithms import insert_sorted


class Objects:
    def __init__(self):
        self.stack_object = [self]
        self.hierarchy_level = None
        self.set_hierarchy()
        self.head = str(self)
        self.parent = None
        self.position = None
        self.depth = None
        self.set_depth()

    def __str__(self):
        if len(self.stack_object) == 1:
            return '_'
        else:
            self.head = self.stack_object[0]
            return str(self.head)

    def __repr__(self):
        return '_'

    def __lt__(self, other):
        if isinstance(other, Objects):
            return self.hierarchy_level < other.hierarchy_level
        else:
            raise AssertionError('The comparison should be with Objects classes')

    def __le__(self, other):
        if isinstance(other, Objects):
            return self.hierarchy_level <= other.hierarchy_level
        else:
            raise AssertionError('The comparison should be with Objects classes')

    def __gt__(self, other):
        if isinstance(other, Objects):
            return self.hierarchy_level > other.hierarchy_level
        else:
            raise AssertionError('The comparison should be with Objects classes')

    def __ge__(self, other):
        if isinstance(other, Objects):
            return self.hierarchy_level >= other.hierarchy_level
        else:
            raise AssertionError('The comparison should be with Objects classes')

    def __eq__(self, other):
        if isinstance(other, Objects):
            return self.hierarchy_level == other.hierarchy_level
        else:
            raise AssertionError('The comparison should be with Objects classes')

    def __ne__(self, other):
        if isinstance(other, Objects):
            return self.hierarchy_level != other.hierarchy_level
        else:
            raise AssertionError('The comparison should be with Objects classes')

    def get_stack_of_types(self):
        return [type(i) for i in self.stack_object]

    def set_hierarchy(self):
        self.hierarchy_level = 0

    def parent_stack(self, parent_obj):
        self.parent = parent_obj

    def put_stack(self, obj):
        if isinstance(obj, Objects) and self.stack_object[0].interact(obj):
            self.stack_object = insert_sorted(obj, self.stack_object)
            obj.parent_stack(self)

    def pop_stack(self, obj):
        self.parent.stack_object.remove(obj)

    def destroy(self):
        self.pop_stack(self)

    def set_position(self, x, y):
        self.position = (x, y, self.depth)

    def set_depth(self):
        self.depth = 0

    def interact(self, obj):
        if obj not in self.stack_object:
            return True
        else:
            return False
