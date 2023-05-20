package main

/*
Space	: O(n)
Time	: O(n^2)
*/

func calcEquation(equations [][]string, values []float64, queries [][]string) []float64 {
	var ans []float64
	graph := map[string]map[string]float64{}

	for i, eq := range equations {
		if _, ok := graph[eq[0]]; ok {
			graph[eq[0]][eq[1]] = values[i]
		} else {
			graph[eq[0]] = map[string]float64{eq[1]: values[i]}
		}

		if _, ok := graph[eq[1]]; ok {
			graph[eq[1]][eq[0]] = 1 / values[i]
		} else {
			graph[eq[1]] = map[string]float64{eq[0]: 1 / values[i]}
		}
	}

	type queueHelper struct {
		str string
		flt float64
	}

	for _, q := range queries {
		a, b := q[0], q[1]
		queue := []queueHelper{}
		visited := map[string]int{}
		curr := float64(-1)

		if _, ok := graph[a]; ok {
			queue = append(queue, queueHelper{str: a, flt: float64(1)})
			visited[a] = 1
		}

		for len(queue) > 0 {
			poppedQ := queue[0]
			queue = queue[1:]
			u, uval := poppedQ.str, poppedQ.flt
			if u == b {
				curr = uval
				break
			}
			for v, vval := range graph[u] {
				if _, ok := visited[v]; !ok {
					queue = append(queue, queueHelper{str: v, flt: uval * vval})
					visited[v] = 1
				}
			}
		}
		ans = append(ans, float64(curr))
	}

	return ans
}
