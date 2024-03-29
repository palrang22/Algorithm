import Foundation

func solution(_ n: Int) -> Int {
    var lst : Set<Int> = Set()
    var a = 1

    while a <= Int(sqrt(Double(n))) {
        if n % a == 0 {
            lst.insert(a)
            lst.insert(n/a)
        }
        a += 1
    }
    return lst.reduce(0, +)
}