package main

/*
Space	: O(1)
Time	: O(n)
*/

func countVowelPermutation(n int) int {
    a, e, i, o, u := 1, 1, 1, 1, 1
    mod := 1000000007
    for j := 1; j < n; j++ {
        newA := e % mod
        newE := (a + i) % mod
        newI := (a + e + o + u) % mod
        newO := (i + u) % mod
        newU := a % mod
        a, e, i, o, u = newA, newE, newI, newO, newU
    }
    return (a + e + i + o + u) % mod
}
