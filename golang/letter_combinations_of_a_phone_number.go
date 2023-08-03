package main

/*
Space	: O(n)
Time	: O(n ^ 3)
*/

func letterCombinations(digits string) []string {
	ans := []string{}

	if digits == "" {
		return ans
	}

	n := len(digits)
	path := ""
	hashmap := map[string]string{
		"2": "abc",
		"3": "def",
		"4": "ghi",
		"5": "jkl",
		"6": "mno",
		"7": "pqrs",
		"8": "tuv",
		"9": "wxyz",
	}

	var getCombination func(i int)
	getCombination = func(i int) {
		if i == n {
			ans = append(ans, path)
			return
		}

		for _, v := range hashmap[string(digits[i])] {
			path += string(v)
			getCombination(i + 1)
			path = path[:len(path)-1]
		}
	}

	getCombination(0)
	return ans
}
