package main

// Space : O(1)
// Time  : O(n log n)

func maxArea(h int, w int, horizontalCuts []int, verticalCuts []int) int {
    horizontalCuts = append(horizontalCuts, 0)
    horizontalCuts = append(horizontalCuts, h)
    verticalCuts = append(verticalCuts, 0)
    verticalCuts = append(verticalCuts, w)
    
    sort.Ints(horizontalCuts)
    sort.Ints(verticalCuts)
    
    mh := 0
    for i := 1; i < len(horizontalCuts); i++ {
        mh = Max(mh, horizontalCuts[i] - horizontalCuts[i-1])
    }
    
    mv := 0
    for j := 1; j < len(verticalCuts); j++ {
        mv = Max(mv, verticalCuts[j] - verticalCuts[j-1])
    }
    
    return (mh * mv) % (int(math.Pow(10, 9)) + 7)