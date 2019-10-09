from collections import OrderedDict
class LRUCache(OrderedDict):
    def __init__(self, capacity: int):
        self.capacity = capacity
        
    def get(self, key: int) -> int:
        if key in self:
            value = self[key]
            self.move_to_end(key)
            return value
        else:
            return -1
    
    def put(self, key: int, value: int) -> None:
        if key not in self:
            if len(self) == self.capacity:
                del self[next(iter(self))]
        self[key] = value
        self.move_to_end(key)
