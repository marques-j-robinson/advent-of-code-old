class DataTranslations:

    def translate(self):
        pass

    def split_by_empty_line(self):
        self.data = [l.replace('\n', ' ').split(' ') for l in self.data.split('\n\n')]

    def split_by_new_line(self):
        self.data = self.data.split('\n')

    def int_list(self):
        self.data = [int(i) for i in self.data]
