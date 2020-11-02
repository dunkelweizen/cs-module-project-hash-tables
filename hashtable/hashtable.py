class HashTableEntry:
    """
    Linked List hash table key/value pair
    """

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.load = 0

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.storage)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        full_buckets = sum([1 for x in self.storage if x])
        if full_buckets == 0:
            return 0
        return self.capacity / full_buckets

    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        pass
        # Your code here

    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        hashed = 5381
        for char in key:
            hashed = (hashed * 33) + ord(char)
        return hashed

    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        new_entry = HashTableEntry(key,value)
        if self.storage[hashed_index]:
            new_next = self.storage[hashed_index]
            self.storage[hashed_index] = new_entry
            self.storage[hashed_index].next = new_next
        else:
            self.storage[hashed_index] = new_entry
        if self.get_load_factor() > 0.7:
            new_capacity = self.capacity * 2
            self.resize(new_capacity)

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        key_found = False
        if self.storage[hashed_index] is not None:
            pointer = self.storage[hashed_index]
            if pointer.key == key:
                key_found = True
                pointer.key = None
                return
            if pointer.next:
                if pointer.next.key == key:
                    key_found = True
                    pointer.next.key = None
                    return
                while pointer.next.next:
                    if pointer.next.key == key:
                        key_found = True
                        if pointer.next.next:
                            new_next = pointer.next.next
                            pointer.next = new_next
                        else:
                            pointer.next = None
                        break
                    pointer = self.storage[hashed_index].next
        if not key_found:
            print("That key is not in the table!")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        hashed_index = self.hash_index(key)
        if self.storage[hashed_index] is not None:
            pointer = self.storage[hashed_index]
            if pointer.key == key:
                return pointer.value
            while pointer.next:
                if pointer.key == key:
                    return pointer.value
                else:
                    pointer = pointer.next
            if pointer.key == key:
                return pointer.value
        return None

    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        new_storage = [None] * new_capacity
        for entry in self.storage:
            if entry is not None:
                if entry.next is not None:
                    pointer = entry
                    while pointer.next:
                        new_index = self.djb2(pointer.key) % new_capacity
                        if new_storage[new_index] is not None:
                            new_next = new_storage[new_index]
                            new_storage[new_index] = HashTableEntry(pointer.key, pointer.value)
                            new_storage[new_index].next = new_next
                        else:
                            new_storage[new_index] = HashTableEntry(pointer.key, pointer.value)
                        pointer = pointer.next
                    new_index = self.djb2(pointer.key) % new_capacity
                    if new_storage[new_index] is not None:
                        new_next = new_storage[new_index]
                        new_storage[new_index] = HashTableEntry(pointer.key, pointer.value)
                        new_storage[new_index].next = new_next
                    else:
                        new_storage[new_index] = HashTableEntry(pointer.key, pointer.value)

                else:
                    new_index = self.djb2(entry.key) % new_capacity
                    if new_storage[new_index] is not None:
                        new_next = new_storage[new_index]
                        new_storage[new_index] = HashTableEntry(pointer.key, pointer.value)
                        new_storage[new_index].next = new_next
                    else:
                        new_storage[new_index] = HashTableEntry(entry.key, entry.value)
        self.storage = new_storage

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
