# Solves the continous median problem

class ContinousMedianList:
    def __init__(self):
        self.list = []

    # O(n) time
    def insert(self, num):
        for i in range(len(self.list))[::-1]:
            if self.list[i] < num:
                self.list.insert(i+1, num)
                return
        
        self.list.insert(0, num)


    # O(1) time
    def get_median(self):
        length = len(self.list)
        
        if length%2:
            return self.list[length//2]
        
        else:
            return (self.list[length//2 - 1] + self.list[length//2]) / 2


if __name__ == "__main__":
    cm = ContinousMedianList()
    cm.insert(5)
    cm.insert(10)
    med = cm.get_median()
    assert med == 7.5, med
    cm.insert(100)
    med = cm.get_median()
    assert med == 10, med
    print("You're all set!")