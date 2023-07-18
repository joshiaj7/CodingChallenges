package main

import "golang/model"

type LRUCache struct {
	Capacity int
	Hashmap  map[int]*model.LRUNode
	Head     *model.LRUNode
	Tail     *model.LRUNode
}

func LRUCacheConstructor(capacity int) LRUCache {
	lru := LRUCache{
		Capacity: capacity,
		Hashmap:  map[int]*model.LRUNode{},
		Head:     model.NewLRUNode(0, 0),
		Tail:     model.NewLRUNode(0, 0),
	}

	lru.Head.Next = lru.Tail
	lru.Tail.Prev = lru.Head

	return lru
}

func (obj *LRUCache) Get(key int) int {
	if _, ok := obj.Hashmap[key]; ok {
		n := obj.Hashmap[key]
		obj.remove(n)
		obj.add(n)
		return n.Val
	}

	return -1
}

func (obj *LRUCache) Put(key int, value int) {
	if _, ok := obj.Hashmap[key]; ok {
		obj.remove(obj.Hashmap[key])
	}

	n := model.NewLRUNode(key, value)
	obj.add(n)
	obj.Hashmap[key] = n
	if len(obj.Hashmap) > obj.Capacity {
		hn := obj.Head.Next
		obj.remove(hn)
		delete(obj.Hashmap, hn.Key)
	}
}

func (obj *LRUCache) remove(node *model.LRUNode) {
	p := node.Prev
	n := node.Next
	p.Next = n
	n.Prev = p
}

func (obj *LRUCache) add(node *model.LRUNode) {
	p := obj.Tail.Prev
	p.Next = node
	obj.Tail.Prev = node
	node.Prev = p
	node.Next = obj.Tail
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */
