package main

/*
Space	: O(n)
Time	: O(n^2)
*/

func isBipartite(graph [][]int) bool {
	n := len(graph)
	colored := map[int]int{}

	for i := 0; i < n; i++ {
		_, ok := colored[i]
		if !ok && len(graph[i]) > 0 {
			colored[i] = 1
			q := []int{i}
			for len(q) > 0 {
				cur := q[0]
				q = q[1:]
				for _, nb := range graph[cur] {
					if _, ok := colored[nb]; !ok {
						colored[nb] = -colored[cur]
						q = append(q, nb)
					} else if colored[nb] == colored[cur] {
						return false
					}
				}
			}
		}
	}

	return true
}
