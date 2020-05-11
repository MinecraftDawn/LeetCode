class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        self.dict = {}
        self.list = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.list)
            self.list.append(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dict:
            index = self.dict[val]
            tail = self.list[-1]
            self.dict[tail] = index
            self.list[index] = tail
            self.list.pop()
            self.dict.pop(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        import random
        return random.choice(self.list)