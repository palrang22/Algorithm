import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int {
    var current = n
    var halfCurr = current / 2
    var newa = a
    var newb = b
    
    while current > 1 {
    
        print(newa, newb)
        
        if ( newa <= halfCurr && newb <= halfCurr) {
            current = halfCurr
            halfCurr = current / 2
        } else if newa > halfCurr && newb > halfCurr {
            newa -= halfCurr
            newb -= halfCurr
        } else {
            break
        }
        
    }
    
    return Int(log(Double(current)) / log(2.0))
}