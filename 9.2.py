class main:
    def __init__(self):
        self.name = 'A'

    def play(self):
        if self.name == 'A':
            self.name = 'B'
            return 0
        elif self.name == 'B':
            self.name = 'C'
            return 1
        elif self.name == 'D':
            self.name = 'E'
            return 4
        elif self.name == 'E':
            self.name = 'F'
            return 7
        else:
            raise KeyError

    def scan(self):
        if self.name == 'D':
            self.name = 'A'
            return 6
        elif self.name == 'C':
            self.name = 'D'
            return 3
        elif self.name == 'E':
            self.name = 'C'
            return 8
        else:
            raise KeyError

    def place(self):
        if self.name == 'D':
            self.name = 'B'
            return 5
        elif self.name == 'B':
            self.name = 'F'
            return 2
        else:
            raise KeyError

