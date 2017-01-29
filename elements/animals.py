import numpy as np
import sqlite3
from default_object import Objects
from reinforcement import directions

class Reinforce:
    def __init__(self, obj):
        self.object_dict = {'Cat': self.reinforce_cat,
                            'Mouse': self.reinforce_mouse}
        self.object = obj
        self.conn = None
        self.reinforcement_table()

    def get_reinforce(self, object_to_learn):
        return self.object_dict[self.object.__class__.__name__](object_to_learn)

    @staticmethod
    def reinforce_cat(obj_return):
        if isinstance(obj_return, Mouse):
            return 50
        elif isinstance(obj_return, Cheese):
            return 0
        elif isinstance(obj_return, Objects):
            return 0
        else:
            return -10

    @staticmethod
    def reinforce_mouse(obj_return):
        if isinstance(obj_return, Cat):
            return -50
        elif isinstance(obj_return, Cheese):
            return 50
        elif isinstance(obj_return, Objects):
            return 0
        else:
            return -10

    def reinforcement_table(self):
        obj_class_name = self.object.__class__.__name__
        self.conn = sqlite3.connect(obj_class_name + '.db')
        c = self.conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS ' +
                  obj_class_name +
                  ' (direction text, idx real, times_executed integer)')
        self.conn.commit()
        tables = c.execute('''SELECT count(1) FROM ''' + obj_class_name)
        if tables.fetchall()[0][0] == 0:
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('N', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('S', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('E', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('W', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('NE', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('NW', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('SE', 0.0, 0)''')
            c.execute('''INSERT INTO ''' + obj_class_name + ''' VALUES ('SW', 0.0, 0)''')
        self.conn.commit()

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
    def learn(self, obj_directions):
        epsilon = 0.99
        reinforce = Reinforce(self)
        cursor = reinforce.conn.cursor()
        obj_direct_list = directions((self.position[0], self.position[1]), obj_directions).items()
        if epsilon > np.random.random():
            choice = obj_direct_list[np.random.randint(0, len(obj_direct_list))]
            query_list = cursor.execute('''SELECT * FROM ''' +
                                        self.__class__.__name__ +
                                        '''WHERE direction = '%s' ''' % choice[0])
            elems = query_list.fetchall()[0]
            # todo: Need to get the return of reinforce from object to make the calculus sum_of_return / times
            cursor.execute('''UPDATE ''' +
                           self.__class__.__name__ +
                           ''' SET (direction, idx, times_executed) = ('%s', %f, %f)''' % (choice[0], ))
        else:
            l_ob = cursor.execute('''SELECT * FROM ''' +
                                  self.__class__.__name__ +
                                  ''' ORDER BY index DESC''')
            for row in l_ob.fetchall():
                try:
                    choice = obj_directions[str(row[0])]
                    break
                except:
                    pass
        print choice
    def choose_action(self, map):
        possible_moves = map.possible_move(*self.position)
        my_directions = directions((self.position[0], self.position[1]), possible_moves)

