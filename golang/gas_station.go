package main

/*
Space   : O(n)
Time    : O(n)
*/

func canCompleteCircuit(gas []int, cost []int) int {
	ans := -1
	temp := []int{}
	n := len(gas)
	s := 0

	for i := 0; i < n; i++ {
		temp = append(temp, gas[i]-cost[i])
		s += gas[i] - cost[i]
	}

	if s < 0 {
		return -1
	}

	cur := 0
	for i, v := range temp {
		cur += v
		if cur >= 0 && ans == -1 {
			ans = i
		}
		if cur < 0 {
			ans = -1
		}
		cur = Max(cur, 0)
	}
	return ans
}
