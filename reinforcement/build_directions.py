

def directions(actual_pos, list_of_pos):
    '''
    Build the directions to be choosen.
    :param actual_pos:JKJKJKJKJ
    :param list_of_pos:
    :return:
    '''
    default_dict = {'N': lambda act, dst: dst if dst[0] == act[0] and dst[1] > act[1] else None,
                    'S': lambda act, dst: dst if dst[0] == act[0] and dst[1] < act[1] else None,
                    'E': lambda act, dst: dst if dst[0] > act[0] and dst[1] == act[1] else None,
                    'W': lambda act, dst: dst if dst[0] < act[0] and dst[1] == act[1] else None,
                    'NE': lambda act, dst: dst if dst[0] > act[0] and dst[1] > act[1] else None,
                    'NW': lambda act, dst: dst if dst[0] < act[0] and dst[1] > act[1] else None,
                    'SE': lambda act, dst: dst if dst[0] > act[0] and dst[1] < act[1] else None,
                    'SW': lambda act, dst: dst if dst[0] < act[0] and dst[1] < act[1] else None}
    return_dict = {'N': None,
                   'S': None,
                   'E': None,
                   'W': None,
                   'NE': None,
                   'NW': None,
                   'SE': None,
                   'SW': None}
    for destination in list_of_pos:
        for dct in default_dict:
            return_dict[dct] = destination if default_dict[dct](actual_pos, destination) else return_dict[dct]
    return {k: v for k, v in return_dict.items() if v}


