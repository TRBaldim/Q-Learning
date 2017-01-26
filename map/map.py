from default_object import Objects

class Map:
    def __init__(self, x, y):
        self.map_image = []
        for i in range(y):
            self.map_image.append([Objects() for i in range(x)])

    def __str__(self):
        return_str = ''
        for row in self.map_image:
            for elem in row:
                return_str += str(elem) + ' '
            return_str += '\n'
        return return_str

    def set_element(self, elem, x, y):
        self.map_image[y][x].put_stack(elem)
