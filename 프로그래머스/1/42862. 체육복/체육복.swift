import Foundation

func solution(_ n:Int, _ lost:[Int], _ reserve:[Int]) -> Int {
    var uniform = Array(repeating: true, count: n)
    var newReserve = reserve
    lost.forEach { i in uniform[i-1] = false }
    for i in lost {
        if newReserve.contains(i) {
            uniform[i-1] = true
            newReserve.removeAll {$0 == i}
        }
    }
    newReserve.sort(by: <)
    
    for j in newReserve {
        if j-2 >= 0 && uniform[j-2] == false {
            uniform[j-2] = true
        } else if j < n && uniform[j] == false {
            uniform[j] = true
        }
    }
    return uniform.filter {$0 == true}.count
}