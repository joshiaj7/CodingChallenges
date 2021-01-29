package golang

// Max compare 2 int and return the highest value
func Max(a int, b int) int {
	if a > b {
		return a
	}
	return b
}

// Min compare 2 int and return the lowest value
func Min(a int, b int) int {
    if a > b {
        return b
    }
    return a
}
