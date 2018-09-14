class Lines:
    def __init__(self, fn):
        self.fn = fn
        self.array = []

        
    def setFn(self, fn):
        self.fn = fn

        
    def append(self, p1, p2):
        self.array.append((p1, p2))


    def update(self, pos, p1, p2):
        self.array[pos] = (p1, p2)

        
    def clear(self):
        self.array = []
