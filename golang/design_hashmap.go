package golang

// MyHashMap is class model for this question
type MyHashMap struct {
	Values []int
}

// MyHashMapConstructor : value will always be non-negative.
func MyHashMapConstructor() MyHashMap {
	vals := make([]int, 1000001)
	for i := 0; i < len(vals); i++ {
		vals[i] = -1
	}

	return MyHashMap{
		Values: vals,
	}
}

// Put : value will always be non-negative.
func (obj *MyHashMap) Put(key int, value int) {
	obj.Values[key] = value
}

// Get : Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
func (obj *MyHashMap) Get(key int) int {
	return obj.Values[key]
}

// Remove : Removes the mapping of the specified value key if this map contains a mapping for the key 
func (obj *MyHashMap) Remove(key int) {
	obj.Values[key] = -1
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Put(key,value);
 * param_2 := obj.Get(key);
 * obj.Remove(key);
 */