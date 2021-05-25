package main

func validMountainArray(arr []int) bool {
	n := len(arr)

	if n < 3 {
		return false
	}

	peak := 0
	ind := "+"

	for i := 1; i < n; i++ {
		if (arr[i]-arr[i-1] > 0) && ind == "-" {
			return false
		} else if arr[i]-arr[i-1] == 0 {
			return false
		} else if arr[i]-arr[i-1] < 0 {
			ind = "-"
		}

		if i > 1 {
			if (arr[i]-arr[i-1] < 0) && (arr[i-1]-arr[i-2] > 0) {
				peak++
			}
		}

	}

	if peak == 1 {
		return true
	}

	return false
}
