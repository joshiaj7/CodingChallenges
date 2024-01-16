package main

import "math/rand"

/*
Space	: O(n)
Time	: O(1)
*/

type RandomizedSet struct {
	Hashmap map[int]int
	Values  []int
}

func RandomizedSetConstructor() RandomizedSet {
	return RandomizedSet{
		Hashmap: make(map[int]int, 0),
		Values:  make([]int, 0),
	}
}

func (this *RandomizedSet) Insert(val int) bool {
	if _, ok := this.Hashmap[val]; ok {
		return false
	}
	this.Values = append(this.Values, val)
	this.Hashmap[val] = len(this.Values) - 1
	return true
}

func (this *RandomizedSet) Remove(val int) bool {
	if _, ok := this.Hashmap[val]; !ok {
		return false
	}

	valIndex := this.Hashmap[val]
	lastElem := this.Values[len(this.Values)-1]
	this.Hashmap[lastElem] = valIndex
	this.Values[len(this.Values)-1] = this.Values[valIndex]
	this.Values[valIndex] = lastElem
	this.Values = this.Values[:len(this.Values)-1]
	delete(this.Hashmap, val)
	return true
}

func (this *RandomizedSet) GetRandom() int {
	k := rand.Intn(len(this.Values))
	return this.Values[k]
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * obj := Constructor();
 * param_1 := obj.Insert(val);
 * param_2 := obj.Remove(val);
 * param_3 := obj.GetRandom();
 */
