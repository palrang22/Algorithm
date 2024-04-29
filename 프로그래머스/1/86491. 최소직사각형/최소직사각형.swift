import Foundation

func solution(_ sizes:[[Int]]) -> Int {
    var big = 0
    var small = 0
    
    for i in sizes {
        var (a, b) = (i[0], i[1])
        (a, b) = (max(a,b), min(a,b))
        
        big = max(big, a)
        small = max(small,b)
    }
    
    return big*small
}