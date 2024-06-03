import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    var lenn = section.count
    var current = 0
    var count = 0
    
    while current < lenn {
        let curVal = section[current]
        
        while current < lenn && section[current] < curVal + m {
            current += 1
        }
        
        count += 1
    }
    
    return count
}