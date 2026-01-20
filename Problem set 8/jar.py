class Jar:
    def __init__(self, capacity=12): #size is not param cause the user will not modify the size
        if capacity < 0:
            raise ValueError
        self._capacity = capacity #._ is for protecting
        self._size = 0
    
    def __str__(self):
        cookie = "" #return "🍪" * self._size اختصار
        for i in range(self.size):
            cookie = cookie + '🍪'
        return cookie 
    
    def deposit(self, n):
        if n + self.size > self.capacity:
            raise ValueError
        
        self._size = n+self._size #no return cause when .deposit no output
    
    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
    
# jar = Jar(5) 1- Check if capacity is valid 2- Store capacity in _capacity 
# 3- Initialize _size = 0
# jar.deposit(3) 1- Calls it with self = jar and n = 3
# print(jar)        🍪🍪🍪#Python looks for __str__ because print wants a string
# jar.withdraw(1)
# print(jar.size)  # 2