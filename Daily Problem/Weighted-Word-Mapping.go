1func mapWordWeights(words []string, weights []int) string {
2    var res string
3
4    for _, word := range words {
5        w := 0
6        
7        for _, c := range word {
8            w += weights[c - 'a']
9        }
10
11        res += string(rune('z' - (w % 26)))
12    }
13
14    return res
15}