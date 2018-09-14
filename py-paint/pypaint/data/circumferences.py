class Circumferences:
    def __init__(self, fn):
        self.fn = fn
        self.array = []

        
    def setFn(self, fn):
        self.fn = fn

        
    def append(self, center, radius):
        self.array.append((center, radius))


    def update(self, pos, center, radius):
        self.array[pos] = (center, radius)

        
    def clear(self):
        self.array = []
