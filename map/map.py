from default_object import Objects


class Map:
    def __init__(self, x, y):
        self.map_image = []
        self.x = x
        self.y = y
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

    def remove_inconcistency(self, elem):
        x = elem[0]
        y = elem[1]
        if x > self.x or x < 0:
            return False
        elif y > self.y or y < 0:
            return False
        else:
            return True

    @staticmethod
    def remove_from_list(l):
        ret = []
        for i in l:
            if isinstance(i, list):
                [ret.append(k) for k in i]
        return ret

    def possible_move(self, x_orign, y_orgin, depth):
        if depth != 0:
            step = filter(lambda x: x,
                          [self.possible_move(x_orign + depth, y_orgin, depth - 1),
                           self.possible_move(x_orign - depth, y_orgin, depth - 1),
                           self.possible_move(x_orign, y_orgin + depth, depth - 1),
                           self.possible_move(x_orign, y_orgin - depth, depth - 1),
                           self.possible_move(x_orign + depth, y_orgin + depth, depth - 1),
                           self.possible_move(x_orign + depth, y_orgin - depth, depth -1),
                           self.possible_move(x_orign - depth, y_orgin + depth, depth - 1),
                           self.possible_move(x_orign - depth, y_orgin - depth, depth - 1)])

            return list(set(filter(self.remove_inconcistency, sorted([(x_orign + depth, y_orgin),
                                                                      (x_orign - depth, y_orgin),
                                                                      (x_orign, y_orgin + depth),
                                                                      (x_orign, y_orgin - depth),
                                                                      (x_orign + depth, y_orgin + depth),
                                                                      (x_orign + depth, y_orgin - depth),
                                                                      (x_orign - depth, y_orgin + depth),
                                                                      (x_orign - depth, y_orgin - depth)] +
                                                                     self.remove_from_list(step)))))
