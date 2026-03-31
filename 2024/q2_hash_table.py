class HashTable:
    """Task 2.1: Hash Table implementation"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size
        self.count = 0
    
    def HashFunction(self, key):
        """Task 2.1: Simple hash function"""
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.size
    
    def IsEmpty(self, index):
        """Task 2.1: Check if slot is empty"""
        return self.table[index] is None
    
    def IsFull(self):
        """Task 2.1: Check if table is full"""
        return self.count == self.size
    
    def Insert(self, key, value):
        """Task 2.2: Insert key-value pair using linear probing"""
        if self.IsFull():
            print("Hash table is full")
            return False
        
        index = self.HashFunction(key)
        original_index = index
        probes = 0
        
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                print(f"Updated existing key '{key}'")
                return True
            
            probes += 1
            index = (original_index + probes) % self.size
            
            if index == original_index:
                print("Hash table is full")
                return False
        
        self.table[index] = (key, value)
        self.count += 1
        print(f"Inserted '{key}' at index {index} (probes: {probes})")
        return True
    
    def Search(self, key):
        """Task 2.2: Search for key using linear probing"""
        index = self.HashFunction(key)
        original_index = index
        probes = 0
        
        while self.table[index] is not None:
            probes += 1
            if self.table[index][0] == key:
                return self.table[index][1], probes
            
            index = (original_index + probes) % self.size
            
            if index == original_index:
                break
        
        return None, probes
    
    def Delete(self, key):
        """Task 2.3: Delete key from hash table"""
        index = self.HashFunction(key)
        original_index = index
        probes = 0
        
        while self.table[index] is not None:
            probes += 1
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                print(f"Deleted '{key}' from index {index} (probes: {probes})")
                
                next_index = (index + 1) % self.size
                while self.table[next_index] is not None:
                    key_to_rehash = self.table[next_index][0]
                    value_to_rehash = self.table[next_index][1]
                    self.table[next_index] = None
                    self.count -= 1
                    self.Insert(key_to_rehash, value_to_rehash)
                    next_index = (next_index + 1) % self.size
                
                return True
            
            index = (original_index + probes) % self.size
            
            if index == original_index:
                break
        
        print(f"Key '{key}' not found")
        return False
    
    def Display(self):
        """Task 2.2: Display hash table contents"""
        print("\nHash Table Contents:")
        for i in range(self.size):
            if self.table[i] is None:
                print(f"  [{i}]: Empty")
            else:
                key, value = self.table[i]
                print(f"  [{i}]: {key} -> {value}")
        
        print(f"\nTotal items: {self.count}/{self.size}")
        print(f"Load factor: {self.count/self.size:.2f}")
    
    def Rehash(self, new_size):
        """Task 2.4: Rehash to a larger table"""
        old_table = self.table
        self.size = new_size
        self.table = [None] * new_size
        self.count = 0
        
        for item in old_table:
            if item is not None:
                self.Insert(item[0], item[1])
        
        print(f"Rehashed to new size: {new_size}")


class HashTableChaining:
    """Task 2.4: Hash Table with Chaining (using linked lists)"""
    
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0
    
    def HashFunction(self, key):
        total = 0
        for char in str(key):
            total += ord(char)
        return total % self.size
    
    def Insert(self, key, value):
        """Insert using chaining"""
        index = self.HashFunction(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                print(f"Updated existing key '{key}'")
                return True
        
        self.table[index].append((key, value))
        self.count += 1
        print(f"Inserted '{key}' at index {index}")
        return True
    
    def Search(self, key):
        """Search using chaining"""
        index = self.HashFunction(key)
        
        for k, v in self.table[index]:
            if k == key:
                return v
        
        return None
    
    def Delete(self, key):
        """Delete using chaining"""
        index = self.HashFunction(key)
        
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                self.count -= 1
                print(f"Deleted '{key}'")
                return True
        
        print(f"Key '{key}' not found")
        return False
    
    def Display(self):
        """Display hash table with chaining"""
        print("\nHash Table (Chaining) Contents:")
        for i in range(self.size):
            if self.table[i]:
                items = ", ".join([f"{k}:{v}" for k, v in self.table[i]])
                print(f"  [{i}]: {items}")
            else:
                print(f"  [{i}]: Empty")
        
        print(f"\nTotal items: {self.count}")


def CompareProbingStrategies():
    """Task 2.4: Compare linear vs quadratic probing"""
    print("=" * 80)
    print("Comparing Probing Strategies")
    print("=" * 80)
    
    test_keys = ["apple", "banana", "cherry", "date", "elderberry", 
                 "fig", "grape", "kiwi", "lemon", "mango"]
    
    print(f"\nInserting keys: {test_keys}")
    
    print("\n--- Linear Probing ---")
    ht_linear = HashTable(10)
    for key in test_keys:
        ht_linear.Insert(key, f"value_{key}")
    ht_linear.Display()
    
    print("\n--- Searching ---")
    for key in ["cherry", "kiwi", "orange"]:
        result, probes = ht_linear.Search(key)
        if result:
            print(f"Found '{key}' with {probes} probes")
        else:
            print(f"'{key}' not found after {probes} probes")


if __name__ == "__main__":
    ht = HashTable(10)
    
    print("=" * 80)
    print("Task 2.1 & 2.2: Hash Table Implementation")
    print("=" * 80)
    
    test_items = [
        ("apple", "red fruit"),
        ("banana", "yellow fruit"),
        ("cherry", "small red fruit"),
        ("date", "sweet fruit"),
        ("elderberry", "small dark fruit"),
        ("fig", "soft fruit"),
    ]
    
    for key, value in test_items:
        ht.Insert(key, value)
    
    print("\n" + "=" * 80)
    print("Display Hash Table")
    print("=" * 80)
    ht.Display()
    
    print("\n" + "=" * 80)
    print("Task 2.2: Search")
    print("=" * 80)
    for key in ["cherry", "date", "mango"]:
        result, probes = ht.Search(key)
        if result:
            print(f"'{key}' found: {result} (probes: {probes})")
        else:
            print(f"'{key}' not found (probes: {probes})")
    
    print("\n" + "=" * 80)
    print("Task 2.3: Delete")
    print("=" * 80)
    ht.Delete("banana")
    ht.Delete("cherry")
    ht.Display()
    
    print("\n" + "=" * 80)
    print("Task 2.4: Comparison")
    print("=" * 80)
    CompareProbingStrategies()
