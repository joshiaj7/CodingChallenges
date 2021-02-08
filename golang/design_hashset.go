package golang

// Space   : O(n)
// Time    : O(n)

import (
	"fmt"
)

// MyHashSet struct as object
type MyHashSet struct {
	hashmap map[int]int
}

// MyHashSetConstructor object constructor
func MyHashSetConstructor() MyHashSet {
	return MyHashSet{hashmap: make(map[int]int)}
}

// Add adding item to hashset
func (obj *MyHashSet) Add(key int) {
	if _, ok := obj.hashmap[key]; ok {
		fmt.Printf("Add: %d is exist\n", key)
	} else {
		obj.hashmap[key] = 1
	}
}

// Remove remove item from hashset
func (obj *MyHashSet) Remove(key int) {
	if _, ok := obj.hashmap[key]; ok {
		delete(obj.hashmap, key)
	} else {
		fmt.Printf("Remove: %d is not exist\n", key)
	}
}

// Contains returns true if this set contains the specified element
func (obj *MyHashSet) Contains(key int) bool {
	_, ok := obj.hashmap[key]
	return ok
}

/**
 * Your MyHashSet object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Add(key);
 * obj.Remove(key);
 * param_3 := obj.Contains(key);
 */
