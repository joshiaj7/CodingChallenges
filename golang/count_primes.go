package main

// Space   : O(n)
// Time    : O(n log n)

func countPrimes(n int) int {
	isPrime := []bool{}

	for a := 0; a < n; a++ {
		if a <= 1 {
			isPrime = append(isPrime, false)
		} else {
			isPrime = append(isPrime, true)
		}
	}

	for i := 0; i*i < n; i++ {
		if isPrime[i] == false {
			continue
		}
		for j := i * i; j < n; j += i {
			isPrime[j] = false
		}
	}

	count := 0
	for i := 0; i < n; i++ {
		if isPrime[i] == true {
			count++
		}
	}

	return count
}
