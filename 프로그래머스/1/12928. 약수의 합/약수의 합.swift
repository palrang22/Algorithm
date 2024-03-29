import Foundation

func solution(_ n:Int) -> Int {
    
    let num = n
    var a = 1
    var lst : [Int] = []
    
    while a <= Int(sqrt(Double(n))) {
        if n % a == 0 {
            lst.append(a)
            lst.append(n/a)
        }
        a += 1
    }
    
    let setlst = Set(lst)
    
    return setlst.reduce(0,+)
}