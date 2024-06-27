import Foundation

func solution(_ n:Int) -> Int {

    var a = 0
    var b = 1
    var c = 0
    
    if n == 0 {
        return 0
    }
    if n == 1 {
        return 1
    }
    
    for _ in 2...n {
        c = (a + b) % 1234567
        a = b
        b = c
    }
    
    return c
}