class main:
    def __init__(self):
        self.name = 'A'

    def mass(self):
        if self.name == 'A':
            self.name = 'B'
            return 0
        elif self.name == 'D':
            self.name = 'E'
            return 4
        elif self.name == 'E':
            self.name = 'C'
            return 7
        elif self.name == 'F':
            self.name = 'A'
            return 8
        else:
            raise KeyError

    def trace(self):
        if self.name == 'B':
            self.name = 'B'
            return 2
        elif self.name == 'D':
            self.name = 'F'
            return 5
        else:
            raise KeyError

    def sit(self):
        if self.name == 'B':
            self.name = 'C'
            return 1
        elif self.name == 'C':
            self.name = 'D'
            return 3
        elif self.name == 'E':
            self.name == 'F'
            return 6
        else:
            raise KeyError
