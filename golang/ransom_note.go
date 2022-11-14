package main

/*
Space	: O(26)
Time	: O(n)
*/

func canConstruct(ransomNote string, magazine string) bool {
	tmp := make([]int, 26)

	for _, v := range magazine {
		tmp[v-'a']++
	}
	for _, v := range ransomNote {
		tmp[v-'a']--
		if tmp[v-'a'] < 0 {
			return false
		}
	}

	return true
}
