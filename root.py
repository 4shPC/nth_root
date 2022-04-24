class Root_:
    def __init__(self, root_, num):
        self.root_ = root_
        self.num = num
        self.x1 = self.num/3
        self.x2 = (1/self.root_) * (((self.root_ - 1)*self.x1) + (self.num/(self.x1**(self.root_ - 1))))

    def func_root_(self):
        return (1/self.root_) * (((self.root_ - 1)*self.x2) + (self.num/(self.x2**(self.root_ - 1))))

    def root(self):
        for i in range(10):
            self.x2 = self.func_root_()
            
        return self.x2