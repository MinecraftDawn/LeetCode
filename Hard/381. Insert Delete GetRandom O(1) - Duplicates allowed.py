class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if val in self.dict:
            self.dict[val].append(len(self.list))
            self.list.append(val)
            return True
        else:
            self.dict[val] = [len(self.list)]
            self.list.append(val)
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        import bisect
        if val in self.dict:
            index = self.dict[val][-1]
            tail = self.list[-1]
            self.dict[tail].pop()
            bisect.insort_left(self.dict[tail], index)
            self.list[index] = tail
            self.list.pop()
            if len(self.dict[val]) == 1:
                self.dict.pop(val)
            else:
                self.dict[val].pop()
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        import random
        return random.choice(self.list)
        


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()