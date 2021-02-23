package golang

import (
	"strings"
)

// Space : O(n**2)
// Time	: O(n**2)
// where n = number of letters in S

// ascii
// 48 - 57 digits
// 65 - 90 capital letters
// 97 - 122 lower case letters

func letterCasePermutation(S string) []string {
	var ans []string
	var permute func(word string, path string)

	permute = func(word string, path string) {
		if len(word) == 0 {
			ans = append(ans, path)
		} else {
			if word[0] >= 65 && word[0] <= 122 {
				permute(word[1:], path+strings.ToLower(string(word[0])))
				permute(word[1:], path+strings.ToUpper(string(word[0])))
			} else {
				permute(word[1:], path+string(word[0]))
			}
		}
	}

	permute(S, "")

	return ans
}
