class main:
    def __init__(self):
        self.name = 'A'

    def method1(self):
        if self.name == 'A':
            self.name = 'F'
            return 1
        elif self.name == 'C':
            self.name = 'D'
            return 4
        elif self.name == 'G':
            self.name = 'H'
            return 9
        else:
            raise KeyError

    def method2(self):
        if self.name == 'A':
            self.name = 'B'
            return 0
        elif self.name == 'D':
            self.name = 'E'
            return 5
        elif self.name == 'G':
            self.name = 'B'
            return 10
        elif self.name == 'H':
            self.name = 'B'
            return 11
        else:
            raise KeyError

    def method3(self):
        if self.name == 'A':
            return 2
        elif self.name == 'B':
            self.name = 'C'
            return 3
        elif self.name == 'D':
            self.name = 'A'
            return 6
        elif self.name == 'E':
            self.name = 'F'
            return 7
        elif self.name == 'F':
            self.name = 'G'
            return 8
        else:
            raise KeyError
