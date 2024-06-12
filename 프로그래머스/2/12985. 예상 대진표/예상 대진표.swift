import Foundation

func solution(_ n:Int, _ a:Int, _ b:Int) -> Int {
    var aup = a
    var bup = b
    var count = 0
    
    while true {
        if aup == bup {
            break
        } else {
            aup = (aup+1) / 2
            bup = (bup+1) / 2
            count += 1
        }
    }
    
    return count
}