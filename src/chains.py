import random

def longest_linked_chain(keys, buckets, loops=10):
    for i in range(loops):
        key_counts = {}
        for i in range(buckets):
            key_counts[i] = 0
        for i in range(keys):
            random_key = str(random.random())
            hash_index = hash(random_key) % buckets
            key_counts[hash_index] += 1

        largest_n = 0
        for key in key_counts:
            if key_counts[key] > largest_n:
                largest_n = key_counts[key]

        print(f"longest linked list chain for {keys} keys in {buckets} buckets")
        print(f"Load factor: {keys/buckets:.2f}")


longest_linked_chain(5, 100, 5)