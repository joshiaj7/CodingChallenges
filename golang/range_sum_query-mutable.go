package main

// Space : O(n)
// Time  : O(n)

type NumArray struct {
    Arr []int
}


func SumQueryConstructor(nums []int) NumArray {
    return NumArray{
        Arr: nums,   
    }
}


func (this *NumArray) Update(index int, val int)  {
    this.Arr[index] = val
}


func (this *NumArray) SumRange(left int, right int) int {
    ans := 0
    for i := left; i <= right; i++ {
        ans += this.Arr[i]
    } 
    return ans
}


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */