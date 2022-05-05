package main

type MyStack struct {
	Q []int
}

func MyStackConstructor() MyStack {
	return MyStack{
		Q: []int{},
	}
}

func (this *MyStack) Push(x int) {
	this.Q = append([]int{x}, this.Q...)
}

func (this *MyStack) Pop() int {
	n := this.Q[0]
	this.Q = this.Q[1:]
	return n
}

func (this *MyStack) Top() int {
	return this.Q[0]
}

func (this *MyStack) Empty() bool {
	return len(this.Q) == 0
}

/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */
