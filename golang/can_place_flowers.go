package main

func canPlaceFlowers(flowerbed []int, n int) bool {
	if n == 0 {
		return true
	}

	f := len(flowerbed)

	begin, allZero := flowerbed[0] == 0, true
	count, place := 0, 0

	for i := 0; i < f; i++ {
		if flowerbed[i] == 0 {
			count++
		} else {
			allZero = false
			if begin {
				place += count / 2
				begin = false
			} else if count > 0 {
				place += (count - 1) / 2
			}
			count = 0
		}

	}

	// if all items 0
	if allZero {
		return (f+1)/2 >= n
	}

	// if end exists
	if count > 0 {
		place += count / 2
	}

	if n <= place {
		return true
	}

	return false
}
