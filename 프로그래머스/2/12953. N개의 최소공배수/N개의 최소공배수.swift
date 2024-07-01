import Foundation

func solution(_ arr:[Int]) -> Int {
    return arr.reduce(1){lcm($0, $1)}
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