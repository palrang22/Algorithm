import Foundation

func solution(_ arr:[Int]) -> Int {
    var lcmAll = 1
    for i in arr {
        lcmAll = lcm(i, lcmAll)
    }
    return lcmAll
}

func gcd(_ x: Int, _ y: Int) -> Int {
    var (a, b) = (x, y)
    var tmp = a % b
    while tmp != 0 {
        (a, b) = (b, tmp)
        tmp = a % b
    }
    return b
}

func lcm(_ x: Int, _ y: Int) -> Int {
    return x*y/gcd(x, y)
}