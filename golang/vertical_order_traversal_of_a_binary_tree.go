package golang

import (
	"golang/model"
	"sort"
)

type pair struct {
    Node *model.TreeNode
    Pos int
}

func max(a int, b int) int {
    if a > b {
        return a
    }
    return b
}

func verticalTraversal(root *model.TreeNode) [][]int {
    m := make(map[int][]int)
    var ans [][]int
    var stack []pair
    minv, maxv := 0, 0
    stack = append(stack, pair{
        Node: root,
        Pos: 0,
    })
    
    for len(stack) > 0 {
        mtemp := make(map[int][]int)
        var atemp []pair
        
        for _, item := range stack {
            minv = min(minv, item.Pos)
            maxv = max(maxv, item.Pos)
            
            if _, ok := mtemp[item.Pos]; ok {
                mtemp[item.Pos] = append(mtemp[item.Pos], item.Node.Val)
            } else {
                mtemp[item.Pos] = []int{item.Node.Val}
            }
            
            if item.Node.Left != nil {
                atemp = append(atemp, pair{
                    Node: item.Node.Left,
                    Pos: item.Pos - 1,
                })
            }
            
            if item.Node.Right != nil {
                atemp = append(atemp, pair{
                    Node: item.Node.Right,
                    Pos: item.Pos + 1,
                })
            }
        }
        
        for key, val := range mtemp {
            sort.Ints(val)
            if _, ok := m[key]; ok {
                m[key] = append(m[key], val...)
            } else {
                m[key] = val
            }
        }
        
        stack = atemp
    }
    
    for i := minv; i <= maxv; i++ {
        ans = append(ans, m[i])
    }
    
    return ans
}