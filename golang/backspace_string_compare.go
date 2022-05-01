package main

/*
Space	: O(n)
Time	: O(n)

method:
Stack
*/

func processBackspace(S string) string {
	a := ""
	ls := len(S)
	for i := 0; i < ls; i++ {
		if string(S[i]) == "#" {
			if len(a) > 0 {
				a = a[:len(a)-1]
			}
		} else {
			a += string(S[i])
		}
	}
	return a
}

func backspaceCompare(S string, T string) bool {
	return processBackspace(S) == processBackspace(T)
}
