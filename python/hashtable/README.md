# Hashtables:

Implement a Hashtable with the following methods:

- ```add```: takes in both the key and value. This method should hash the key, and add the key and value pair to the table, handling collisions as needed.

- ```get```: takes in the key and returns the value from the table.

- ```contains```: takes in the key and returns a boolean, indicating if the key exists in the table already.

- ```hash```:: takes in an arbitrary key and returns an index in the collection.

## Challenge:

- Adding a key/value to your hashtable results in the value being in the data structure.

- Retrieving based on a key returns the value stored.

- Successfully returns null for a key that does not exist in the hashtable.

- Successfully handle a collision within the hashtable.

- Successfully retrieve a value from a bucket within the hashtable that has a collision.

- Successfully hash a key to an in-range value.

## Approach & Efficiency:

-  the space complexity of every reasonable hash table is O(n).
- Time complexity is O(1)

## API:

1. ```_hash(key)``` : takes in an arbitrary key and returns an index in the collection.

2. ```add(key, value)```: takes in both the key and value. add the key and value pair to the table.

3. ```get(requested_ket)```: takes in the key and returns the value from the table.

4. ```contains(requested_ket)```:takes in the requested_ket and returns a boolean.