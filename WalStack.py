class stack(list):
    def push(self, foo):
        self.append(foo)
        
    def pop(self):
        e=self[-1]
        del self[-1]
        return e

    def pass
