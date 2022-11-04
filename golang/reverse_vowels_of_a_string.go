package main

/*
Space	: O(n)
Time	: O(n)
*/

func reverseVowels(s string) string {
	a := []byte(s)
	vowels := map[byte]int{
		byte('a'): 1,
		byte('e'): 1,
		byte('i'): 1,
		byte('o'): 1,
		byte('u'): 1,
		byte('A'): 1,
		byte('E'): 1,
		byte('I'): 1,
		byte('O'): 1,
		byte('U'): 1,
	}

	head, tail := 0, len(s)-1
	head_found, tail_found := false, false
	for head < tail {

		if !head_found {
			if _, ok := vowels[s[head]]; ok {
				head_found = true
			} else {
				head++
			}
		}

		if !tail_found {
			if _, ok := vowels[s[tail]]; ok {
				tail_found = true
			} else {
				tail--
			}
		}

		if head_found && tail_found {
			a[head], a[tail] = a[tail], a[head]
			head_found, tail_found = false, false
			head++
			tail--
		}

	}

	return string(a)
}
