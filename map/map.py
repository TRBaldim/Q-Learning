from default_object import Objects


class Map:
    def __init__(self, x, y):
        self.map_image = []
        for i in range(y):
            self.map_image.append([Objects() for _ in range(x)])

    def __str__(self):
        return_str = ''
        for row in self.map_image:
            for elem in row:
                return_str += str(elem) + ' '
            return_str += '\n'
        return return_str

    def set_element(self, elem, x, y):
        elem.set_position(x, y)
        self.map_image[y][x].put_stack(elem)
    # todo: Implement  the movement, and the possible movement in the map
    def possible_move(self, x_orign, y_orgin, depth):
        if depth != 0:
            return [self.possible_move(x_orign + depth, y_orgin + depth, depth - 1),
                    self.possible_move(x_orign + depth, y_orgin - depth, depth -1),
                    self.possible_move(x_orign - depth, y_orgin + depth, depth - 1),
                    self.possible_move(x_orign - depth, y_orgin - depth, depth - 1)]
