package golang

// Space	: O(n)
// Time		: O(n)

import (
	"strings"
)

func simplifyPath(path string) string {
	s := strings.Split(path, "/")
	newPath := []string{}

	for i := 0; i < len(s); i++ {
		if s[i] == "" || s[i] == "." {
			continue
		} else if s[i] == ".." {
			if len(newPath) > 0 {
				newPath = newPath[:len(newPath)-1]
			}
		} else {
			newPath = append(newPath, s[i])
		}
	}

	ans := ""
	for _, v := range newPath {
		ans += "/" + v
	}

	if ans == "" {
		ans += "/"
	}

	return ans
}
