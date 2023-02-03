package main

// Space	: O(n)
// Time		: O(n)

func convert(s string, numRows int) string {
	ans := ""
	d := map[int]string{}

	if numRows == 1 {
		return s
	}

	count := 1
	direction := "+"

	for _, c := range s {
		if _, ok := d[count]; !ok {
			d[count] = string(c)
		} else {
			d[count] += string(c)
		}

		if direction == "+" && count == numRows {
			direction = "-"
		}
		if direction == "-" && count == 1 {
			direction = "+"
		}

		if direction == "+" {
			count++
		} else if direction == "-" {
			count--
		}
	}

	for i := 1; i <= numRows; i++ {
		ans += d[i]
	}

	return ans
}
