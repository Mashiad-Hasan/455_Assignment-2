class TT():
    def __init__(self):
        self.table={}

    def store(self, code, result):
        self.table[code]=result

    def lookup(self, code):
        return self.table.get(code)
