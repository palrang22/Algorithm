import Foundation

func solution(_ n:Int) -> Int {
    
    var num = n
    var sum = 0

    if num % 2 == 1 {
        num -= 1
    }
    
    while num > 0 {
        sum += num
        num -= 2
    }
    
    return sum
}