import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lis=defaultdict(lambda:0)
        self.el=set()
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        s=self.lis
        if s[val]==1:
            return False
        else:
            s[val]=1
            self.el.add(val)
            return True
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        s=self.lis
        if s[val]==1:
            s[val]=0
            self.el.remove(val)
            return True
        else:
            return False
        

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return random.choice(tuple(self.el))
