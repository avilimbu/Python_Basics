# override the __len__() method on vector of problem 6 to display the dimension of the vector.

class vecotr:
    def __init__(self,l):
        self.l = l

    def __len__(self):
        return(len(self.l))

v1 = vecotr([2,4,7])
print(len(v1))