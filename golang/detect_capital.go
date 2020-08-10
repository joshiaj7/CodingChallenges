package golang

// leetcode

func detectCapitalUse(word string) bool {
    isCorrect := true
    
    if len(word) < 2 {
        return isCorrect
    }
    
    wordType := ""
    // allLower, allUpper, capitalize
    if len(word) > 1 {
        if word[0] >= 65 && word[0] <= 90 {
            if word[1] >= 65 && word[1] <= 90 {
                wordType = "allUpper"
            } else {
                wordType = "capitalize"
            }
        } else {
            wordType = "allLower"
        }
    }
    
    for i:= 0; i < len(word); i++ {
        if wordType == "allUpper" {
            if word[i] > 90 {
                isCorrect = false
            }
        } else if wordType == "capitalize" {
            if i > 1 && word[i] <= 90 {
                isCorrect = false
            }
        } else if wordType == "allLower" {
            if word[i] <= 90 {
                isCorrect = false
            }
        }
    }
    
    return isCorrect
}