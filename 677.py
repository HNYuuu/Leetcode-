class MapSum:
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cache = {}
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.cache[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        length = len(prefix)
        temp = 0
        for key in self.cache.keys():
            if len(key) >= length and key[:length] == prefix:
                temp += self.cache[key]
        return temp


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('apple',3)
param_2 = obj.sum('ap')
print(param_2)