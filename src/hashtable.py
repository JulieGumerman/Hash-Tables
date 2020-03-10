# '''
# Linked List hash table key/value pair
# '''
import hashlib

class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.length = 0


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''

        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity



    def insert(self, key, value):
        
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''

        index = self._hash_mod(key)
        newNode = LinkedPair(key, value)


        if self.storage[index] is not None:
            if self.storage[index].key == key:
                self.storage[index].value = value
                return
            newNode.next = self.storage[index]
            self.storage[index] = newNode
        else:
            self.storage[index] = newNode
    
    

                    






    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)

        if self.storage[index] is not None:
            self.storage[index] = None
        else: 
            "not yet"
            #if you find it, delete it
            #if you don't delete it, return error message
        


    def retrieve(self, key):
        #fix
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        index =self._hash_mod(key)
        current = self.storage[index]

        if current != None:
            if current.key == key:
                return current.value
            else:
                while current != None:
                    if current.key == key:
                        return current.value
                    current = current.next
        else:
            return None

        # if current.key == key:
        #     return (current.key, current.value)
        # else:
        #     return "Sorry, bro. We're not handling collisions yet"

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        #you aren't done yet: hash the keys before resetting stuff
        oldstorage = self.storage
        self.capacity *= 2
        self.storage = [None] * self.capacity

        for bucket_item in oldstorage:
            self.insert(oldstorage[bucket_item].key, oldstorage[bucket_item].value)




if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
