from collections import OrderedDict

class LRUCache:
    def __init__(self,capacity):
        self.capacity = capacity
        self._map = OrderedDict()

    def get(self,key):
        if key in self._map:
            value = self._map.pop(key)
            self._map[key] =value
            return value
        return -1

    def put(self,key,value):
        if key in self._map:
            self._map.pop(key)
        elif len(self._map)==self.capacity:
            self._map.popitem(last=False) #FIFO
        self._map[key] = value


