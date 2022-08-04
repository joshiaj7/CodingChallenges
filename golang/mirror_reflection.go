package main

/*
Space	: O(1)
TIme	: O(log(pq))
*/

func mirrorReflection(p int, q int) int {
	g := gcd(p, q)
	m, n := q/g, p/g

	if n%2 == 0 {
		return 2
	}

	return m % 2
}

func gcd(temp1 int, temp2 int) int {
	var gcdnum int
	for i := 1; i <= temp1 && i <= temp2; i++ {
		if temp1%i == 0 && temp2%i == 0 {
			gcdnum = i
		}
	}
	return gcdnum
}
