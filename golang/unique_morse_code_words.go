package golang

func uniqueMorseRepresentations(words []string) int {
    truth := []string{".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."}
    
    hashmap := make(map[string]int)
    n := len(words)
    
    for i := 0; i < n; i++ {
        var morse string
        for j := 0; j < len(words[i]); j++ {
            morse += truth[words[i][j]-97]
        }
        if _, ok := hashmap[morse]; ok {
            hashmap[morse]++
        } else {
            hashmap[morse] = 1
        }
    }
    
    return len(hashmap)
}