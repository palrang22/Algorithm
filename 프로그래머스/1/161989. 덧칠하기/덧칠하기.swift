import Foundation

func solution(_ n:Int, _ m:Int, _ section:[Int]) -> Int {
    let len = section.count
    var current = 0
    var count = 0
    
    while current < len {
        let curVal = section[current]
        
        while current < len && section[current] < curVal + m {
            current += 1
        }
        
        count += 1
    }
    
    return count
}