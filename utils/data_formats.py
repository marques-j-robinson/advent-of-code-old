def int_list(a):
    return [int(i) for i in a]


def combine(a, b):
    return len(a + list(set(b) - set(a)))


def parse_coord(coord):
    return [int(i) for i in coord.split(',')]


class DataFormats:

    def format_data(self):
        pass

    def split_by_empty_line(self):
        self.data = [l.replace('\n', ' ').split(' ') for l in self.data.split('\n\n')]

    def split_by_new_line(self):
        self.data = self.data.split('\n')

    def int_list(self):
        self.data = int_list(self.data)
